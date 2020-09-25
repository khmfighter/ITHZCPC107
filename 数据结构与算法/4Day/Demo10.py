'''
归并排序
'''




def merge_sort(alist):
    if len(alist)==1:
        return alist


    mid=len(alist)//2

    left=merge_sort(alist[:mid])
    right=merge_sort(alist[mid:])

    return merge(left,right)

def merge(left, right):
    list=[]
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            list.append(left[l])
            l += 1
        else:
            list.append(right[r])
            r += 1
    list += left[l:]
    list += right[r:]
    return list


if __name__=="__main__":
    print(merge_sort([67,45,32,24,36,78,43,2]))
