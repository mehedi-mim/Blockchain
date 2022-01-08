from chain import Chain


chain = Chain(20)

while(True):
    data = input('Insert data to be hashed:')
    chain.add_to_pool(data)
    chain.mine()

    for item in chain.blocks:
        hash = item.hash
        data = item.data
        print(data,hash.hexdigest())
