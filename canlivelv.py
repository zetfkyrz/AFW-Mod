with open("./history/pops/1861.4.14/Mexico.txt") as f:
    prov = list(map(int,input().split()))
    s = f.read()
    for i in range(len(prov)):
        
        n = s.find("\n" +str(prov[i]) + " =")
        m = s.find("#",n)
        while(n < m):
            if prov[i] == 6:
                print(n,m,m1)
            n = s.find("size =",n + 6)
            m1 = s.find('\n',n)
            s = s[:m1] + '0' + s[m1:]
        print(prov[i])

with open("./history/pops/1861.4.14/Mexico.txt", 'w') as f:
    f.write(s)
n = 0
m = 0
m1 = 0
s = ""
with open("./history/pops/1861.4.14/United States.txt") as f:
    s = f.read()
    for i in range(len(prov)):
        
        n = s.find("\n" + str(prov[i]) + " =")
        if not n: 
            continue
        
        m = s.find("#",n)
        while(n < m):
            n = s.find("size =",n + 6)
            m1 = s.find('\n',n)
            s = s[:m1] + '0' + s[m1:]
        print(prov[i])

with open("./history/pops/1861.4.14/United States.txt",'w') as f:
    f.write(s)
n = 0
m = 0
m1 = 0
s = ""
with open("./history/pops/1861.4.14/Canada.txt") as f:
    s = f.read()
    for i in range(len(prov)):
        
        n = s.find("\n" + str(prov[i]) + " =")
        m = s.find("#",n)
        while(n < m):
            n = s.find("size =",n + 6)
            m1 = s.find('\n',n)
            s = s[:m1] + '0' + s[m1:]
        print(prov[i])
with open("./history/pops/1861.4.14/Canada.txt",'w') as f:
    f.write(s)
