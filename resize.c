// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: resize (n) infile outfile\n");
        return 1;
    }

    // remember filenames
    int n = atoi (argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];


    if (n >= 100 || n < 1)
    {
        fprintf(stderr, "%i is not a positive integer less than or equal to 100\n", n);
        return 1;
    }

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s. Input file must be the name of a BMP to be resized\n", infile);
        return 1;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s. Output file must be a .bmp.\n", outfile);
        return 1;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 1;
    }

    // determine padding for scanlines
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    int OldWidth = bi.biWidth;
    int OldHeight = abs(bi.biHeight);

    bi.biWidth = bi.biWidth * n;
    bi.biHeight = bi.biHeight * n;

    int newpadding = ((4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4);


    bi.biSizeImage = (bi.biWidth * abs(bi.biHeight)) * sizeof(RGBTRIPLE) + newpadding;
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0; i < OldHeight; i++)
    {
        for (int y = 0; y < n; y++)
        {

            if (y != 0)
            {
                fseek(inptr, (-3 * OldWidth - padding), SEEK_CUR);
            }


            // iterate over pixels in scanline
            for (int j = 0; j < OldWidth; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                for (int x = 0; x < n; x++)
                {
                    // write RGB triple to outfile
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
            }

            // skip over padding, if any
            fseek(inptr, padding, SEEK_CUR);

            // then add it back (to demonstrate how)
            for (int k = 0; k < newpadding; k++)
            {
                fputc(0x00, outptr);
            }

        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
