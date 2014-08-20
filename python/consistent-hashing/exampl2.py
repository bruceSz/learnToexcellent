from hashlib import md5
from struct import unpack_from

NODE_COUNT = 100
NEW_NODE_COUNT = 101
DATA_ID_COUNT = 100000

moved_ids = 0
for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)
    hsh = unpack_from('>I',md5(data_id).digest())[0]
    node_id = hsh % NODE_COUNT
    new_node_id = hsh % NEW_NODE_COUNT
    if node_id != new_node_id:
        moved_ids += 1

percent_moved = 100.0 *moved_ids/DATA_ID_COUNT
print '%d ids moved, %.02f%%'%(moved_ids,percent_moved)
        
