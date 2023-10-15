class BlockChain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    # Creates a new block and adds it to the chain
    ...

  def new_transactions(self, sender: str, recipient: str, amount: int) -> int:
    # Adds a new transaction to the list of transactions
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })
    return self.last_block['index'] + 1

  @staticmethod
  def hash(block):
    # Hashes a block
    ...

  @property
  def last_block(self):
    # Returns the last block in the chain
    ...
