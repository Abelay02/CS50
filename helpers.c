// Helper functions for music

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    //getting the numerator as the int x, and the denominator as the int y
    // - '0' because the values are stored as char. This brings them to int value
    int x = fraction[0] - '0';
    int y = fraction[2] - '0';


    int d = (8 * x) / y;
    return d;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{

    char letter = note[0];
    char octave;
    char accidental;
    int L;
    int O;
    int n;
    int Hertz;

    //defining variables if there is an accidental
    if (note[1] == '#' || note[1] == 'b')
    {
        octave = note[2];
        accidental = note[1];
    }

    //defining variables if there isn't an accidental
    else
    {
        octave = note[1];
    }

    //determining how many semitones to add (L), based on relative position to A
    if (letter == 'A')
    {
        L = 0;
    }

    if (letter == 'B')
    {
        L = 2;
    }

    if (letter == 'C')
    {
        L = -9;
    }

    if (letter == 'D')
    {
        L = -7;
    }

    if (letter == 'E')
    {
        L = -5;
    }

    if (letter == 'F')
    {
        L = -4;
    }

    if (letter == 'G')
    {
        L = -2;
    }

    //determining how many semitones to add (O), based on relative position to the 4th octave
    //multiply difference by 12 because of 12 semitones in each octave
    O = octave - '0';
    O = O - 4;
    O = 12 * O;

    //accounting for accidentals in semitone shifts
    //if a sharp, up one semitone
    if (note[1] == '#')
    {
        n = L + O + 1;
    }

    //if a flat, down one semitone
    else if (note[1] == 'b')
    {
        n = L + O - 1;
    }

    //no shift
    else
    {
        n = L + O;
    }

    Hertz = round(440 * pow(2.00, n / 12.00));

    return Hertz;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (iscntrl(s[0]))
    {
        return true;
    }
    else
    {
        return false;
    }
}

