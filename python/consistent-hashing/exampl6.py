from array import array
from hashlib import md5
from struct import unpack_from

PARTITION_POWER = 23
PARTITION_SHIFT = 32 - PARTITION_POWER
NODE_COUNT = 65535
DATA_ID_COUNT = 100000000

part2node = array('H')
for part in xrange(2**PARTITION_POWER):
    part2node.append(part%NODE_COUNT)

node_counts = [0]*NODE_COUNT
for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)
    part = unpack_from('>I',md5(data_id).digest())[0]>>PARTITION_SHIFT
    node_id = part2node[part]
    node_counts[node_id]+=1


desired_count = DATA_ID_COUNT / NODE_COUNT
print '%d: Desired data ids per node' %desired_count
max_count = max(node_counts)
over = 100.0*(max_count - desired_count)/desired_count
print '%d: Most data ids on one node,%0.2f%% over'%(max_count,over)

min_count = min(node_counts)
under = 100.0*(desired_count - min_count)/desired_count
print '%d:Least data ids on one node,%.02f%% under'%(min_count,under)


