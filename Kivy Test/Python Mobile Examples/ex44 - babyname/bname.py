# bname.py

def rlists(year):
    M=[]
    F=[]
    with open('data/yob'+str(year)+'.txt') as f:
        A=f.readlines()
    for a in A:
        if ',F,' in a:
            F.append((a.split(',')[0],int(a.split(',')[-1])))
        else:
            M.append((a.split(',')[0],int(a.split(',')[-1])))
    F=[f[0]+" : " + str(f[1]) for f in F]
    M=[m[0]+" : " + str(m[1]) for m in M]
    return M[:100],F[:100]

if __name__=='__main__':
    m,f=rlists(2001)
    print(m)