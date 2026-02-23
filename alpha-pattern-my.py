n=5
for i in range(n):

    #spaces
    for k in range(n-i-1):
        print("-",end="-")
    
    #pyramid
    for j in range(i+1):
        print(chr(65+n-j-1),end="-")
    
    #pyramid
    for j in range(i,0,-1):
        if n-j!=n-1:
            print(chr(65+n-j),end="-")
        else:
            print(chr(65+n-j),end="")

    #spaces
    for k in range(n-i-1):
        print("-",end="-")
    
    print()

for i in range(n-2,-1,-1):

    #spaces
    for k in range(n-i-1):
        print("-",end="-")
    
    #pyramid
    for j in range(i+1):
        print(chr(65+n-j-1),end="-")
    
    #pyramid
    for j in range(i,0,-1):
        if n-j!=n-1:
            print(chr(65+n-j),end="-")
        else:
            print(chr(65+n-j),end="")

    #spaces
    for k in range(n-i-1):
        print("-",end="-")
    
    print()
