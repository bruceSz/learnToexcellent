from array import array
from hashlib import md5
from random import shuffle
from struct import unpack_from
from time import time

class Ring(object):
    def __init__(self,nodes,part2node,replicas):
        self.nodes = nodes
        self.part2node = part2node
        self.replicas = replicas
        partition_power = 1
        while 2**partition_power < len(part2node):
            partition_power += 1
        if len(part2node) != 2** partition_power:
            raise Exception('part2node" length is not exact 2"s  power')

        self.partition_shift = 32 - partition_power

    def get_nodes(self,data_id):
        data_id = str(data_id)
        part = unpack_from('>I',md5(data_id).digest())[0]>>self.partition_shift
        node_ids = [self.part2node[part]]
TODO:
