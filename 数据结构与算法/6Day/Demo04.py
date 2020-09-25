num=eval(input())
alist=[]
while num>=1:
    alist.append(input())
    num-=1
print(alist)
for item in alist:
    kvmap={'{':0,'[':0,'(':0,'}':0,']':0,')':0}
    for i in item:
        kvmap[i]+=1
    print(min(kvmap['{'],kvmap['}'])," ",min(kvmap['['],kvmap[']'])," ",min(kvmap['('],kvmap[')']))

