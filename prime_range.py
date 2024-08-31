a = int(input("Enter the min number:"))
b = int(input("Enter the max number:"))
c = int(input("Enter the number:"))
for n in range(a,b +1):
    i = 2
    f = True
    while(i<=n//2):
        if(n%i==0):
            f = False
            break
        i+=1
    if(f == True):
        print(n,"prime")
              
