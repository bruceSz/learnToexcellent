from array import array
from hashlib import md5
from struct import unpack_from

REPLICAS = 3
PARTITION_POWER = 16
PARTITION_SHIFT = 32 - PARTITION_POWER
PARTITION_MAX = 2 ** PARTITION_POWER - 1
NODE_COUNT = 256
DATA_ID_COUNT = 1000000

part2node = array('H')
for part in xrange(2**PARTITION_POWER):
    part2node.append(part % NODE_COUNT)

node_counts = [0]*NODE_COUNT
for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)
    part = unpack_from('>I',md5(data_id).digest())[0]>>PARTITION_SHIFT
    node_ids = [part2node[part]]
    node_counts[node_ids[0]] += 1
    for replica in xrange(1,REPLICAS):
        while part2node[part] in node_ids:
            part += 1
            if part > PARTITION_MAX:
                part = 0
        node_ids.append(part2node[part])
        node_counts[node_ids[-1]] += 1

desired_count = DATA_ID_COUNT / NODE_COUNT * REPLICAS
print '%d: Desired data ids per node' %desired_count
max_count = max(node_counts)
over = 100.0*(max_count - desired_count)/desired_count
print '%d: Most data ids on one node,%0.2f%% over'%(max_count,over)

min_count = min(node_counts)
under = 100.0*(desired_count - min_count)/desired_count
print '%d:Least data ids on one node,%.02f%% under'%(min_count,under)




