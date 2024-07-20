import torch
from torch import nn
import torch.nn.functional as F
import numpy as np
from tqdm import tqdm
import warnings
import subprocess
from time import time, sleep

# 乱数シードの設定
np.random.seed(42)
torch.manual_seed(42)
torch.cuda.manual_seed(42)

# ワーニングを無視
warnings.simplefilter('ignore')

# CUDA環境の確認
print("CUDA環境の確認: ", torch.cuda.is_available())
# CUDAが利用できない場合のエラーハンドリングを検討する

######################
# GPT decorder
######################

class PreLNGPTDecoderLayer(nn.Module):
    """
    Pre Layer Normalization GPT Decoder Layer（事前レイヤー正規化GPTデコーダ層）。

    引数:
        embedding_dim (int): 各埋め込みベクトルのサイズ。
        ffn_dim (int): フィードフォワードネットワークモデルの次元数。
        num_heads (int): マルチヘッドアテンションモデルのヘッド数。
        drop_out_rate (float, optional): ドロップアウト率。デフォルトは0.0。
        layer_eps (float, optional): LayerNormのためのイプシロン値。デフォルトは1e-05。
        batch_first (bool, optional): Trueの場合、入力および出力テンソルは(batch, seq, feature)として提供されます。デフォルトはFalse。
    """
    def __init__(self, embedding_dim, ffn_dim, num_heads, drop_out_rate = 0., layer_eps=1e-05, batch_first = False):
        super().__init__()
        self.masked_multihead_attention = nn.MultiheadAttention(embedding_dim, num_heads, batch_first=batch_first)
        self.dropout_self_attn = nn.Dropout(p=drop_out_rate)
        self.layer_norm_self_attn = nn.LayerNorm(embedding_dim, eps=layer_eps)

        self.ffn = nn.Sequential(
            nn.Linear(embedding_dim, ffn_dim), 
            nn.GELU(), 
            nn.Linear(ffn_dim, embedding_dim)
        )
        self.layer_norm_ffn = nn.LayerNorm(embedding_dim, eps=layer_eps)
        self.dropout_ffn = nn.Dropout(p=drop_out_rate)

    def forward(self, x, pad_mask_self=None, mask_self=None):
        """
        レイヤーのフォワードパス。

        引数:
            x: 入力テンソル。
            pad_mask_self: 自己アテンションのためのパディングマスク。
            mask_self: 自己アテンションのためのアテンションマスク。

        戻り値:
            GPTデコーダ層を通過した後のテンソル。
        """
        attention_input = self.layer_norm_self_attn(x)
        attention_output, _ = self.masked_multihead_attention(
            attention_input, attention_input, attention_input,
            key_padding_mask=pad_mask_self, attn_mask=mask_self
        )
        attention_output = self.dropout_self_attn(attention_output)
        x = x + attention_output

        ffn_input = self.layer_norm_ffn(x)
        ffn_output = self.dropout_ffn(self.ffn(ffn_input))
        x = x + ffn_output

        return x
    

    #######################
    # GPT model implementation
    ######################

    class GPT(nn.Module):
    def __init__(self, vocab_size, embedding_dim, ffn_dim, num_heads, drop_out_rate = 0.,\
                  layer_eps=1e-05, batch_first = False, T = 10000, N = 1):
        super().__init__()
        #Tはmax_lenを表している
        self.embedding = nn.Embedding(vocab_size, embedding_dim,)
        self.positional_embedding = nn.Embedding(T, embedding_dim)
        self.decoder = nn.ModuleList([PreLNGPTDecoderLayer(embedding_dim, ffn_dim, num_heads, drop_out_rate,\
                                                               layer_eps, batch_first) for _ in range(N)])
        self.linear = nn.Linear(embedding_dim, vocab_size, bias = False)
        self.vocab_size = vocab_size
    def forward(self, x, y = None,pad_mask_self = None, mask_self=None):
        """
        yはxを1つだけずらしたデータである
        x = data[a:b]なら、y = data[a+1:b+1]となる。
        """
        x = self.embedding(x)
        pos = torch.arange(0,x.size(1),dtype=torch.long).unsqueeze(0).to(x.device)
        pos = self.positional_embedding(pos)
        x = x + pos
        for layer in self.decoder:
            x = layer(x, pad_mask_self = pad_mask_self, mask_self = mask_self)
        x = self.linear(x)
        if y != None:
            loss = F.cross_entropy(x.view(-1, x.size(-1)), y.view(-1), ignore_index=-1)
            #ignore_index=-1はyをonehotベクトル化しないでcross_entropyを使うために使用
            pred = x.argmax(dim = -1).detach().cpu()
            return loss,pred
        loss = None
        pred = x[:,[-1],:]
        return loss, pred
    def create_mask(self, x: torch.tensor, x_pad: int, device: str):
        """
        (batch_size, sequence_length, embedding_dim)の入力を想定
        """
        """
        Trueが無視される値であることに注意すること
        """
        seq_len = x.size(1)
        #srcのマスク制作
        padding_mask = (x == x_pad)
        mask = torch.triu(torch.ones(size = (seq_len, seq_len))==1).transpose(0,1) #下三角行列を作る
        mask = mask.float().masked_fill(mask == 0, float("-inf")).masked_fill(mask==1.,float(0.0)).to(device)
        return padding_mask, mask

    @torch.no_grad()
    def generate(self,bos: str, sentence_size, tokenizer, device):
        self.eval()
        bos_tokenized = tokenizer.encode_ordinary(bos)
        bos_tokenized = bos_tokenized[-sentence_size:]
        bos_tokenized = torch.LongTensor([bos_tokenized])
        _, add_sentence = self(bos_tokenized.to(device))
        self.train()
        return add_sentence

    @torch.no_grad()
    def generate_sentence(self, bos: str, sentence_size, generate_tokens, tokenizer, device, top_K = None, temperature = 1.0):
        return_sentence = bos
        for i in range(generate_tokens):
            add_sentence = self.generate(return_sentence, sentence_size, tokenizer,device)
            add_sentence = add_sentence[:,-1,:] / temperature #(1, vocab_size)
            if top_K is not None:
                v, _ = torch.topk(add_sentence, min(top_K, add_sentence.size(-1)))
                #v[:, [-1]]がtopkの中でも最小値を取る。これより小さいやつは予想に含めない。
                add_sentence[add_sentence < v[:, [-1]]] = -float('Inf')
            probs = F.softmax(add_sentence, dim = -1)
            idx_next = torch.multinomial(probs, num_samples=1)
            return_sentence += tokenizer.decode_batch(idx_next.tolist())[0]
        return return_sentence
    

    #################################
    # GPT model instance generation
    #################################


    device = "cuda" if torch.cuda.is_available() else "cpu"
x = torch.tensor([[2, 10, 20, 100, 512, 3], [2, 10, 20, 100, 512, 3], [2, 10, 20, 100, 512, 3]], dtype=torch.long).to(device)
# x = x.reshape(3, 6)  # 
embedding_size = 768
num_heads = 12
# Parameters set based on Karpathy's minGPT
gpt = GPT(50257, embedding_size, embedding_size * 4, num_heads, 0.1, batch_first=True, T=1024, N=12).to(device)






###
######
###


# 前提として、xは適切に前処理されたシーケンシャルデータである必要があります。
padding_mask, mask = gpt.create_mask(x[0:2], 0, device)

# x[0:2] を入力とし、x[1:3] をターゲットとして使用
loss, pred = gpt(x[0:2], x[1:3], padding_mask, mask)

# loss が None でない場合にのみ出力
if loss is not None:
    print("Loss: \n", loss.item())  # loss.item() は、もし loss がテンソルの場合に値を取得するために使用
print("Pred: \n", pred)


###
####
###

count_params = 0
for params in gpt.parameters():
    count_params += params.contiguous().view(-1).size(0)
print("The number of parameters is ", count_params)


