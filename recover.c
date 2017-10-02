#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    char *infile = argv[1];

    BYTE buffer[512];

    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    int num_images = 0;

    FILE *imagemaker;

    bool writing = false;

    //is there another block of 512 bytes left in the file?
    int num_bytes = fread(&buffer, 1, 512, inptr);

    //if there are at least 512 bytes left in the file
    while (num_bytes == 512)
    {
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (writing)
            {
                //close the image maker if at the start of a new jpeg
                fclose(imagemaker);
            }
            else
            {
                writing = true;
            }

            //naming and opening the ouptut jpeg files
            char filename[7];
            sprintf(filename, "%03i.jpg", num_images);

            imagemaker = fopen(filename, "w");

            num_images++;
        }

        if (writing)
        {
            //writing the jpeg
            fwrite(&buffer, 512, 1, imagemaker);
        }

        //redefining num_bytes. Outputs 512 if there are at least 512 bytes left in the file
        num_bytes = fread(&buffer, 1, 512, inptr);
    }

    //if there aren't 512 bytes left in the file, indicates EOF. Close the input/output files
    fclose(inptr);
    fclose(imagemaker);

    return 0;




}
