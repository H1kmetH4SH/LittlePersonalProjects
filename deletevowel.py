a=input("")
a=list(a)
saitler=list("aeiou")
new=[]

for i in a:
    if a in saitler:
        continue
    elif i not in saitler:
        new.append(i)
print("".join(new))