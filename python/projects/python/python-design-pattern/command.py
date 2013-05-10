import os
class MoveFileCommand(object):
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest
    def execute(self):
        self()
    def __call__(self):
        print ('renaming {} to {}'.format(self.src,self.dest))
    
    def undo(self):
        print('renaming {} to {}'.format(self.dest,self.src))

if __name__ == '__main__':
    undo_stack = []
    ren1 = MoveFileCommand('foo.txt','bar.txt')
    ren2 = MoveFileCommand('bar.txt','baz.txt')
    for cmd in ren1,ren2:
        undo_stack.append(cmd)

    for cmd in undo_stack:
        cmd.execute()
        
    for cmd in undo_stack:
        undo_stack.pop().undo()
        undo_stack.pop().undo()
