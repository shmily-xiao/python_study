#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime as date
from Block import Block

def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", '0')



def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

if __name__ == '__main__':
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # how many blocks should we add to the chain
    # after the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        # Tell everyone adout it!
        print  "Block #{0} has been added to the blockchain! ".format(block_to_add.index)
        print "Hash: {0} \n".format(block_to_add.hash)