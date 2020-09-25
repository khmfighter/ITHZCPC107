arr=[4,6,3,78,45,64,34,23]
#冒泡排序（从小到大）
def pop_sort(arr):
    length=len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j]>arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
    print(arr)

pop_sort(arr)
