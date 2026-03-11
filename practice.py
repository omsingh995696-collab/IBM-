#def num(n):
    #if n == 1:
        #print("1")
        #return 
    #num(n-1)
    #print(n)
    #um(n-1)
#num(3)

def num(n):
    if n == 1:
        return
    num(n-1)
    num(n-1)
    print(n)
num(3)

