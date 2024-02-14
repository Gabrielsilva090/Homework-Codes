'''def todas_substrings(string):
    n = len(string)
    
    for i in range(n):
        for j in range(i+1, n+1):
            substring = string[i:j]
            print(substring)

# Exemplo de uso:
string = "rum"
todas_substrings(string)'''

def todas_substrings(string):
    n = len(string)
    i = 0

    while i < n:
        j = i + 1
        while j <= n:
            substring = string[i:j]
            print(substring)
            j += 1
        i += 1

string = "careca"
todas_substrings(string)