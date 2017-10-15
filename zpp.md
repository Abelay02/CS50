# Z++

## Questions

1.

```
function main()
{
    $x <- get()
    $y <- get()

    subtract($x, $y)
}

function subtract($x, $y)
{
    $s <- add($x, -$y)
    return($s)
}


```

2.

```
function main()
{
    $x <- get()
    $y <- get()

    multiply($x, $y)
}

function multiply($x, $y)
{
    $m <- 0

    while (x)
    {
        $m <- add($m, $y)

        $x <- add($x, -1)
    }

    return($m)
}

```

3.

```
function main()
{
    $x <- get()
    $y <- get()

    multiply($x, $y)
}

function multiply($x, $y)
{

    if ($y > 0)
    {
        return($x + multiply($x, add($y, -1)))
    }

    if ($y < 0)
    {
        return(-multiply($x, -$y))
    }

    return(0)
}
```

## Debrief

1. TODO
http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/

2. TODO
30 minutes