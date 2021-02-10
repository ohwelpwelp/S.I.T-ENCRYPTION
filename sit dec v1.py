from PIL import Image
import time
img = Image.open('SIT code.png', 'r')
pix_val = list(img.getdata())
for i in range(0,len(pix_val)):
    if pix_val[i]==(0,0,0):
        pix_val.pop(i)
        pix_val.insert(i,"1")
for i in range(0,len(pix_val)):
    if pix_val[i]==(255,255,255):
        pix_val.pop(i)
        pix_val.insert(i,"0")
pix_val="".join(pix_val)
pix_val=[pix_val[i:i+8] for i in range(0, len(pix_val), 8)]
pix=[]
for i in range(0,len(pix_val)):
    pix.append(chr(int(pix_val[i],2)))
print("".join(pix))
time.sleep(len(pix)/2)
