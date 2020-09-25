'''
插入排序
维持最前面的顺序不变，后面依次比较

'''
def insert_sort(arr):
    length=len(arr)
    for i in range(1,length):
        print("第",i,"轮")


        for j in range(i,0,-1):
            flag = False
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                flag=True
            if flag==False:
                #print(arr)
                break
            print(arr)
    return arr
print(insert_sort([54,26,93,17,77,31,44,55,20]))
