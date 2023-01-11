def pattern(n):
    x = 65
    for i in range(1,n+1):
        print(chr(x)*i)
        x += 1
pattern(5)