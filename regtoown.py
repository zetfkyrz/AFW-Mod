import glob
country = input()

prov = list(map(int,input().split()))

for i in range(len(prov)):
    files = glob.glob('./history/provinces/*/'+ str(prov[i]) + ' *')
    print(files)
    with open(files[0],'r' ) as f:
        s = f.read()
        n = s.find("owner =")
        m = s.find("\n",n)
        s = s[:n] + "owner = " + country + s[m:]
        n = s.find("controller =")
        m = s.find("\n",n)
        s = s[:n] + "controller = " + country + s[m:]
        n = s.find("add_core =")
        m = s.find("\n",n)
        s = s[:n] + "add_core = " + country + s[m:]

        scan = s.find("1861")
        if scan:
            n = s.find("owner =",scan)
            m = s.find("\n",n)
            s = s[:n] + "owner = " + country + s[m:]
            n = s.find("controller =",scan)
            m = s.find("\n",n)
            s = s[:n] + "controller = " + country + s[m:]
            n = s.find("add_core =",scan)
            m = s.find("\n",n)
            s = s[:n] + "add_core = " + country + s[m:]



                
        n = s.rfind("}")
        s = s[:n+1]
    with open(files[0],'w') as f: 
        f.write(s)
        
        
