# test_blockchain.py

from blockchain import Blockchain

def test_blockchain():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1  # Check if the genesis block is created
    print("Blockchain test passed!")
