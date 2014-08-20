from bisect import bisect_left
from hashlib import md5
from struct import unpack_from


NODE_COUNT = 100
NEW_NODE_COUNT = 101
DATA_ID_COUNT = 1000000

node_range_starts = []
for node_id in xrange(NODE_COUNT):
    node_range_starts.append(DATA_ID_COUNT/
                            NODE_COUNT*node_id)
new_node_range_starts = []
for new_node_id in xrange(NEW_NODE_COUNT):
    new_node_range_starts.append(DATA_ID_COUNT/
                                NEW_NODE_COUNT*new_node_id)

moved_ids = 0
for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)
    hsh = unpack_from('>I',md5(data_id).digest())[0]
    node_id = bisect_left(node_range_starts,hsh%DATA_ID_COUNT)%NODE_COUNT
    new_node_id = bisect_left(new_node_range_starts,hsh%DATA_ID_COUNT)%NEW_NODE_COUNT
    if node_id != new_node_id:
        moved_ids += 1

percent_moved = 100.0* moved_ids/DATA_ID_COUNT
print '%d ids moved, %.02f%%' %(moved_ids,percent_moved)


