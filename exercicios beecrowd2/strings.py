def todas_substrings(string, i=0, j=1):
    n = len(string)

    if i < n:
        if j <= n:
            substring = string[i:j]
            print(substring)
            todas_substrings(string, i, j+1)
        else:
            todas_substrings(string, i+1, i+2)

string = "careca"
todas_substrings(string)