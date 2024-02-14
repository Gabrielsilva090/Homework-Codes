def mdc(a,b):
    if b>a:
        a,b = b,a
    if b == 0:
        return a
    else:
        return mdc(b,a%b)
    

print(mdc(20,24))

