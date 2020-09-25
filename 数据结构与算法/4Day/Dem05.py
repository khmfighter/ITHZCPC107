'''
选择排序
经过第一轮比较之后，找到最大值，放到最后一位
经过第二轮比较之后，找到最大值，放到倒数第二位
以此类推
'''

def select_sort(arr):
    length=len(arr)
    for i in range(length-1):
        #max=arr[0]
        index=0
        print("第",i,"轮")
        print(arr)
        for j in range(1,length-i):
            if arr[index]<arr[j]:
                #max=arr[j]
                index=j
        if index != length-1-i:
            arr[length-i-1], arr[index] = arr[index], arr[length-i-1]
    return arr
print(select_sort([4,5,8,3,12,6,2]))