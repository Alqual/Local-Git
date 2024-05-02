package main

//// This is a pen
// T>h>i>s
//i,s,a
// i,

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unsafe"
)

// -- TrieNode --
type TrieNode struct {
	Children    map[string]*TrieNode
	IsEndOfWord bool   // このノードが単語の終わりかどうかを示すフラグ
	Node        string // このノードの文字
}

func NewTrieNode() *TrieNode {
	return &TrieNode{
		Children:    make(map[string]*TrieNode),
		IsEndOfWord: false,
		Node:        "",
	}
}

type Trie struct {
	Root *TrieNode
}

func NewTrie() *Trie {
	return &Trie{
		Root: NewTrieNode(),
	}
}

func (t *Trie) Insert(word string) {
	current := t.Root
	for _, ch := range word {
		chs := string(ch)
		if _, exists := current.Children[chs]; !exists {
			current.Children[chs] = NewTrieNode()
		}
		current = current.Children[chs]
		current.Node = chs
		//fmt.Println(ch, current, current.Node)
	}
	current.IsEndOfWord = true // 単語の終わりとしてマーク
}

// Calculate size of TrieNode recursively
func calculateNodeSize(node *TrieNode) int {
	size := int(unsafe.Sizeof(*node))
	for _, child := range node.Children {
		size += calculateNodeSize(child)
	}
	return size
}

// ----

// -- StdIn/StdOut --

var sc = bufio.NewScanner(os.Stdin)
var buf = make([]byte, 0, 24000)

func Newline() []string {
	sc.Scan()
	return strings.Fields(sc.Text())
}

// ----

func main() {
	ars := Newline()
	fmt.Println(ars)
	Tries := NewTrie()
	var arsize int
	for _, ar := range ars {
		Tries.Insert(ar)
		arsize += len(ar) + int(unsafe.Sizeof(ar))
	}
	//fmt.Println(Tries.Root.Children, Tries.Root, Tries.Root.Children["T"])
	for _, ar := range Tries.Root.Children {
		for _, arss := range ar.Node {
			fmt.Println(string(arss), &arss)
		}
	}
	trieSize := calculateNodeSize(Tries.Root)
	fmt.Println("Total size of Trie in bytes:", trieSize, arsize)
}
