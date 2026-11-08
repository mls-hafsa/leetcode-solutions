"""n=input()
s=dict()

for i in n.split(","):
    if i in s:
        s[i]+=1
    else:
        s[i]=1

p=max(s.values())
out=[]
for key,value in s.items():
    new=int(key)
    if value==p:
        res=new
        out.append(res)

print(min(out))"""
text=input()
with open("task.txt","w")as file:
    file.write("qawsedrftgyhujikol\n")
    print(file)





