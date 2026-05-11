import numpy as np

class LangevinMemory:
    def __init__(self, dim, mu=0.001, sigma=0.01):
        self.dim = dim
        self.state = np.zeros(dim)
        self.mu = mu
        self.sigma = sigma
    def update(self, v_in, alpha):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.dim)
        self.state += drift + diffusion + alpha * v_in
        self._normalize()
    def _normalize(self):
        norm = np.linalg.norm(self.state)
        if norm > 0: self.state /= norm

class LevyFlightMemory(LangevinMemory):
    def __init__(self, dim, mu=0.001, sigma=0.01, jump_prob=0.02, jump_scale=0.5):
        super().__init__(dim, mu, sigma)
        self.jump_prob = jump_prob
        self.jump_scale = jump_scale
    def update(self, v_in, alpha):
        drift = -self.mu * self.state
        diffusion = np.random.normal(0, self.sigma, self.dim)
        if np.random.rand() < self.jump_prob:
            diffusion += np.random.standard_cauchy(self.dim) * self.jump_scale
        self.state += drift + diffusion + alpha * v_in
        self._normalize()

class KuramotoMemory:
    def __init__(self, dim, K=0.1):
        self.dim = dim
        self.K = K
        self.active_memories = [] # list of vectors
    def update(self, v_in, alpha):
        v = v_in / np.linalg.norm(v_in) if np.linalg.norm(v_in)>0 else v_in
        if alpha > 0.05: # Phase 18 heuristic baseline
            self.active_memories.append(v)
        if len(self.active_memories) > 1:
            M = np.array(self.active_memories)
            S = np.dot(M, M.T)
            S[S < 0] = 0
            np.fill_diagonal(S, 0)
            sum_S = np.sum(S, axis=1, keepdims=True)
            sync_force = np.dot(S, M) - sum_S * M
            M_new = M + (self.K / len(M)) * sync_force
            norms = np.linalg.norm(M_new, axis=1, keepdims=True)
            norms[norms == 0] = 1
            self.active_memories = list(M_new / norms)
    @property
    def state(self):
        if not self.active_memories: return np.zeros(self.dim)
        m = np.mean(self.active_memories, axis=0) # Main consensus topic
        n = np.linalg.norm(m)
        return m / n if n > 0 else m

class HopfieldMemory:
    def __init__(self, dim, lr=0.1):
        self.dim = dim
        self.W = np.zeros((dim, dim))
        self.lr = lr
        self.current_state = np.zeros(dim)
    def update(self, v_in, alpha):
        v = v_in.reshape(-1, 1)
        self.W += alpha * self.lr * np.dot(v, v.T)
        np.fill_diagonal(self.W, 0)
        self.current_state += alpha * v_in
        self.current_state += 0.05 * np.dot(self.W, self.current_state)
        n = np.linalg.norm(self.current_state)
        if n > 0: self.current_state /= n
    @property
    def state(self):
        return self.current_state

class HybridCognitiveMemory:
    def __init__(self, dim, mu=0.001, sigma=0.01):
        self.dim = dim
        self.langevin = LevyFlightMemory(dim, mu, sigma, jump_prob=0.01)
        self.hopfield = HopfieldMemory(dim)
        self.kuramoto = KuramotoMemory(dim, K=0.1)
    def update(self, v_in, alpha):
        self.langevin.update(v_in, alpha)
        self.hopfield.update(v_in, alpha)
        self.kuramoto.update(v_in, alpha)
        
        # Pull langevin state towards hopfield attractors
        self.langevin.state += 0.05 * np.dot(self.hopfield.W, self.langevin.state)
        
        # Pull langevin state towards main consensus of Kuramoto
        if len(self.kuramoto.active_memories) > 0:
            consensus = self.kuramoto.state
            sim = np.dot(self.langevin.state, consensus)
            if sim > 0:
                self.langevin.state += 0.05 * sim * consensus
                
        self.langevin._normalize()
    @property
    def state(self):
        return self.langevin.state
