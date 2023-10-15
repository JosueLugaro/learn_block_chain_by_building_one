import hashlib
import json
from time import time
from typing import Union


class BlockChain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    # Create the genesis block
    self.new_block(previous_hash=1, proof=100)

  @property
  def last_block(self):
    # Returns the last block in the chain
    return self.chain[-1]

  def new_block(self, proof: int, previous_hash: Union[None, int] = None) -> dict:
    # Creates a new block and adds it to the chain
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1])
    }

    self.current_transactions = []
    self.chain.append(block)
    return block

  def new_transactions(self, sender: str, recipient: str, amount: int) -> int:
    # Adds a new transaction to the list of transactions
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })
    return self.last_block['index'] + 1

  @staticmethod
  def hash(block: dict) -> str:
    # Hashes a block
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  def proof_of_work(self, last_proof: int) -> int:
    proof = 0

    while self.validate_proof(last_proof, proof) is False:
      proof += 1

    return proof

  @staticmethod
  def validate_proof(last_proof: int, proof: int) -> bool:
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"
