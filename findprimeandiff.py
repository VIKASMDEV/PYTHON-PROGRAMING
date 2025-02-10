def isprime(num,p):    
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                break
        else:
            p.append(num)
            return p

def checksum(p,d):
    r = []
    for i in p:
        for j in p:
            if abs(i-j == d) and i!=j:
                r.append((i,j))
    return r
    
s=int(input("strt :"))
e=int(input("end :"))
d=int(input("diff : "))
p = []
c=0
for i in range(s,e+1):
    isprime(i,p) 
res = (checksum(p,d))
for i in res:
    c+=1
print(c)

    
    
