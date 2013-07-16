typedef struct {
    void* elems;
    int elemSize;
    int logicLenth;
    int allocLenth;
}stack;
void StackNew(stack *s,int elemSize);
void StackDispose(stack* s);
void StackPush()

