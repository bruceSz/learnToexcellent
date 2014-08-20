
from array import array
from hashlib import md5
from struct import unpack_from
from random import shuffle

REPLICAS = 3
PARTITION_POWER = 16
PARTITION_SHIFT = 32 - PARTITION_POWER
PARTITION_MAX = 2 ** PARTITION_POWER - 1
NODE_COUNT = 256
ZONE_COUNT = 16
DATA_ID_COUNT = 1000000

node2zone = []
while len(node2zone)<NODE_COUNT:
    zone = 0
    while zone < ZONE_COUNT and len(node2zone)<NODE_COUNT:
        node2zone.append(zone)
        zone += 1

part2node = array('H')

for part in xrange(2**PARTITION_POWER):
    part2node.append(part % NODE_COUNT)

shuffle(part2node)
node_counts = [0]*NODE_COUNT
zone_counts = [0]*ZONE_COUNT

for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)

    part = unpack_from('>I',md5(data_id).digest())[0]>>PARTITION_SHIFT
    node_ids = [part2node[part]]
    zones = [node2zone[node_ids[0]]]
    node_counts[node_ids[0]] += 1
    zone_counts[zones[0]] += 1
    for replica in xrange(1,REPLICAS):
        while part2node[part] in node_ids \
            and node2zone[part2node[part]] in zones:
            part += 
            if part > PARTITION_MAX:
                part = 0

        node_ids.append(part2node[part])
        zones.append(node2zone[node_ids[-1]])
        node_counts[node_ids[-1]] += 1
        zone_counts[zones[-1]] += 1


desired_count = DATA_ID_COUNT / NODE_COUNT * REPLICAS
print '%d: Desired data ids per node' %desired_count

max_count = max(node_counts)
over = 100.0*(max_count - desired_count)/desired_count
print '%d: Most data ids on one node,%0.2f%% over'%(max_count,over)


min_count = min(node_counts)
under = 100.0*(desired_count - min_count)/desired_count
print '%d:Least data ids on one node,%.02f%% under'%(min_count,under)





