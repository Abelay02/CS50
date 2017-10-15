# Now Boarding

## Questions

1.

```c
typedef struct
{
    int head;
    int passenger[capacity];
    int size;
}
pqueue;
```

2. TODO
for passengers of group
if size is less than capacity
store passenger[n] at the tail of the queue [(head + size) % capacity]
increment size

3. TODO
O(n). May have to iterate through the whole passenger list to find a passenger with priority.

4. TODO
if size is greater than 0
move head up 1 place
decrement size


5. TODO
O(1). Only has to shift the head of the queue by 1 space because the queue is already in order.

## Debrief

1. TODO
https://study.cs50.net/queues

2. TODO
1 hour