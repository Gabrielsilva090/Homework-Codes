def todas_substrings(string):
    n = len(string)
    i = 0

    while i < n:
        substr = ""
        for j in range(i, n):
            substr += string[j]
            print(substr)
        i += 1

# Exemplo de uso:
string = "rum"
todas_substrings(string)