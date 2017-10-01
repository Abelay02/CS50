# Questions

## What's `stdint.h`?

A header file in C that declares sets of integer types as having specified widths

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Provide standard width definitions of integer types

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1 byte, 4 bytes, 8 bytes, 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Characters B and M

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the bitmap file including headers, biSize is the number of bytes required by the structure

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

If the input file is of the wrong format, or doesn't exist.
If the output file is of the wrong format

## Why is the third argument to `fread` always `1` in our code?

Tells the program to read 1 time from the stream pointed to by inptr

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

1

## What does `fseek` do?

Moves the file pointer to a new location

## What is `SEEK_CUR`?

An integer which can be passed to fseek to request positioning relative to the current position
