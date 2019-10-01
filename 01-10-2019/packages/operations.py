def add(a,b):
    c=a+b
    print("addition",c)

    
    
def prime(n):
    count=0
    for i in range(1,n+1):
       
        if n%i==0:
            count=count+1
    if(count==2):
        print("true")
    else:
        print("false")
        
        
def primefact(n):
    count=0
    for i in range(1,n+1):
       
        if n%i==0:
            count=count+1
            print(i)
    if(count==2):
        print("true")
    else:
        print("false")