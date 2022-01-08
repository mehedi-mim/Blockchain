from block import Block

block = Block("Hello world")
block.mine(20)
print(block.hash.hexdigest())
print(block.nonc)
print(block.data)