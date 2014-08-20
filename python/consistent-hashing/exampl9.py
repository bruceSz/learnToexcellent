from bisect import bisect_left
from hashlib import md5
from struct import unpack_from


REPLICAS = 3
NODE_COUNT = 256
ZONE_COUNT = 16
DATA_ID_COUNT = 100000
VNODE_COUNT = 100

node2zone = []
while len(node2zone) < NODE_COUNT:
    zone = 0
    while zone < ZONE_COUNT and len(node2zone)<NODE_COUNT:
        node2zone.append(zone)
        zone += 1

hash2index = []
index2node = []
for node in xrange(NODE_COUNT):
    for vnode in xrange(VNODE_COUNT):
        hsh = unpack_from('>I',md5(str(node)).digest())[0]
        index = bisect_left(hash2index,hsh)
        if index > len(hash2index):
            index = 0
        hash2index.insert(index,hsh)
        index2node.insert(index,node)

node_counts = [0] * NODE_COUNT
zone_counts = [0] * ZONE_COUNT

for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)
    hsh = unpack_from('>I',md5(data_id).digest())[0]
    index = bisect_left(hash2index,hsh)
    if index > len(hash2index):
        index = 0
    node_ids = [index2node[index]]
    zones = [node2zone[node_ids[0]]]
    node_counts[node_ids[0]] += 1
    zone_counts[zones[0]] += 1
    for replica in xrange(1,REPLICAS):
        while index2node[index] in node_ids and node2zone[index2node[index]] in zones:
            index += 1
            if index > len(hash2index);
                index = 0

        node_ids.append(index2node[index])
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




