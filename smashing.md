# Stack Smashing

## Questions

1. TODO
A stack canary is a small integer value placed before the stack return pointer.
If this value is overwritten by the buffer, this signifies a stack overflow.
Stack canaries are used for detecting this type of overflow.

2. TODO
Because of its similarity to canaries that would be taken into coal mines
to be early detectors of carbon monoxide or other dangers for the miners.

3. TODO

int main(void)
{
    //create an array of length 1
    char buffer[1];
    //copying a string that's too long into that array
    strcpy (buffer, "hello i am going to overflow");
}

## Debrief

1. TODO
https://en.wikipedia.org/wiki/Stack_buffer_overflow#Stack_canaries
https://www.techopedia.com/definition/16157/stack-smashing
https://stackoverflow.com/questions/5296758/stack-vs-buffer

2. TODO
30 minutes
