def f1(eps):
    s=1
    i=0
    while(1):
        for j in range(i+1):
            fz=1
            fm=1
            for k in range(j+1):
                fz*=(k+1)
                fm*=(2*k+3)
            if(fz/fm<eps):
                print(s*2)
                return
        s+=fz/fm
        i+=1

def f2(eps):
    s=1
    i=1
    while(1):
        fz=1
        fm=2*i+1
        if(fz/fm<eps):
            print(s*4)
            return
        if(i%2==1): s-=fz/fm
        else: s+=fz/fm
        i+=1 

eps=float(input())
f1(eps)
f2(eps)