from PIL import Image
b=[]
a=input("string to encrypt:")
d=a
for  i in range(0,len(a)):
    b.append(a[i])
c=[]
for  i in range(0,len(b)):
    c.append(ord(b[i]))
a=[]
for i in range(0,len(c)):
    a.append(bin(c[i]))
b=[]
c=[]
for i in range(0,len(a)):
    if len(str(a[i].replace("b","")))==8:
        c.append(str(a[i].replace("b","")))
    else:
        c.append("0"*(8-len(str(a[i].replace("b",""))))+str(a[i].replace("b","")))
b="".join(c)
c=[]
for i in range(0,len(b)):
    c.append(b[i])
del b
del a
for i in range(0,len(c)):
    if c[i]=="1":
        c.pop(i)
        c.insert(i,(0,0,0))
for i in range(0,len(c)):
    if c[i]=="0":
        c.pop(i)
        c.insert(i,(255,255,255))
img = Image.new("RGB",(8,len(d)),color=(255,255,255))
img.putdata(c)
img.save('SIT code.png')
