from bisect import bisect_left
from hashlib import md5
from struct import unpack_from

NODE_COUNT = 100
DATA_ID_COUNT = 100000
VNODE_COUNT = 1000

vnode_range_starts = []
vnode2node = []

for vnode_id in xrange(VNODE_COUNT):
    vnode_range_starts.append(DATA_ID_COUNT /
                            VNODE_COUNT *vnode_id)
    vnode2node.append(vnode_id%NODE_COUNT)

new_vnode2node = list(vnode2node)

new_node_id = NODE_COUNT 
NEW_NODE_COUNT = NODE_COUNT + 1

vnodes_to_reassign = VNODE_COUNT / NEW_NODE_COUNT
while  vnodes_to_reassign > 0:
    for node_to_take_from  in xrange(NODE_COUNT):
        for vnode_id, node_id in enumerate(new_vnode2node):
            if node_id == node_to_take_from:
                new_vnode2node[vnode_id] = new_node_id
                vnodes_to_reassign -= 1
                if vnodes_to_reassign <=0:
                    break
        if vnodes_to_reassign <= 0:
            break

moved_ids = 0
for data_id in xrange(DATA_ID_COUNT):
    data_id = str(data_id)
    hsh = unpack_from('>I',md5(data_id).digest())[0]
    vnode_id = bisect_left(vnode_range_starts,
                        hsh%DATA_ID_COUNT)%VNODE_COUNT

    node_id = vnode2node[vnode_id]
    new_node_id = new_vnode2node[vnode_id]
    if node_id != new_node_id:
        moved_ids +=1

percent_moved = 100.0 * moved_ids / DATA_ID_COUNT
print '%d ids moved %.02f%%'%(moved_ids,percent_moved)



