

def lines(a, b):
    """Return lines in both a and b"""

    # converting the strings a and b into lists of their lines
    list1 = a.splitlines()
    list2 = b.splitlines()
    t = []

    alen = len(list1)
    blen = len(list2)

    # iterating across the length (number of lines) in list 1
    for i in range(alen):

        # iterating each list 1 line against every list 2 line
        for j in range(blen):

            # checking if any 2 given lines are the same
            if list1[i] == list2[j]:

                # adding that substring to the list
                t.append(list1[i])

    # a set gets rid of duplicates
    s = list(set(t))

    return s


def sentences(a, b):
    """Return sentences in both a and b"""

    from nltk.tokenize import sent_tokenize

    # converting strings a and b into lists of their sentences
    list1 = sent_tokenize(a)
    list2 = sent_tokenize(b)
    t = []

    alen = len(list1)
    blen = len(list2)

    for i in range(alen):

        for j in range(blen):

            # checking if any 2 given sentences are the same
            if list1[i] == list2[j]:

                # adding that substring to the list
                t.append(list1[i])

    # set gets rid of duplicates
    s = list(set(t))

    return s


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    list1 = []
    list2 = []
    t = []

    # making a list of all substrings of length n in a
    for i in range(len(a) + 1 - n):
        j = i + n
        list1.append(a[i:j])

    # making a list of all substrings of length n in b
    for i in range(len(b) + 1 - n):
        j = i + n
        list2.append(b[i:j])

    alen = len(list1)
    blen = len(list2)

    for i in range(alen):

        for j in range(blen):

            # checking if any 2 given substrings are the same
            if list1[i] == list2[j]:

                # adding that substring to the list
                t.append(list1[i])

    # set gets rid of duplicates
    s = list(set(t))
    return s
