package main

import (
	"fmt"
	"bytes"
	"crypto/sha256"
)

type Wand struct {
	materials []Material
}


type Material struct {
	Hash 	 []byte
	Data 	 []byte
	PrevHash []byte
}

func (block *Material) DeriveHash() { 	//receiving a pointer to a imcomplete block and creating a hash based on the data and the hash of the previous block
	info := bytes.Join([][]byte{block.Data, block.PrevHash}, []byte{}) //joining 2 slices of data and prevhash into 1 slice
	hash := sha256.Sum256(info) 		//creating a hash
	block.Hash = hash[:]				//putting the hash into the struct of the block, making into a complete block
}

func CreateBlock(data string, prevHash []byte) *Material {  //create a block
	block := &Material{[]byte{}, []byte(data), prevHash} 	//using the constructor of the block struct
	block.DeriveHash()										//finishing the block
	return block
}

type BlockChain struct { //BlockChain of the materials
	blocks []*Material //array of pointers to blocks
}

//getting a pointer for a blockchain and takes the data string to create a block to add to the block chain
func (chain *BlockChain) addMaterial(data string) {
	prevBlock := chain.blocks[len(chain.blocks)- 1] //taking the last block 
	newBlock := CreateBlock(data, prevBlock.Hash)			//creating a new block
	chain.blocks = append(chain.blocks, newBlock)	//adding to the blockchain
}

func Genesis() *Material {	//first block of the blockchain, every block has a reference to the previous block, so it must have a first reference
	return CreateBlock("Genesis",[]byte{}) //a genesis block with a empty prevHash
}

func initBlockChain() *BlockChain { //creating a blockchain with only one block(genesis)
	return &BlockChain{[]*Material{Genesis()}}
}

func main() {

	chain := initBlockChain()

	chain.addMaterial("carvalho")
	chain.addMaterial("pena de pheonix")
	chain.addMaterial("carvalho")
	chain.addMaterial("sabugueiro")

	for _, block := range chain.blocks {
		fmt.Printf("Previous Hash: %x\n", block.PrevHash)
		fmt.Printf("Data in Block: %x\n", block.Data)
		fmt.Printf("Hash:          %x\n", block.Hash)
	}
}