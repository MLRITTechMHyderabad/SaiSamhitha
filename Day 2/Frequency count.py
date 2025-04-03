a = [3,20,3,12,18,18,50,1,3,4,6,4]
b = {}
for c in a:
   if c in b:
     b[c]+= 1
    
   else:
     b[c] = 1
print(b)
