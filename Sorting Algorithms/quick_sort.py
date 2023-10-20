def partition(arr,low,high):
    #function partitions the array into groups of numbers which are
    #less than the number at the pivot and numbers which are greater than
    #or equal to the pivot
    pivot=high
    i=low-1
    for j in range(low,high):
        if(arr[j]<arr[pivot]):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[pivot]=arr[pivot],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    #sorts the array recursively
    if(low<high):
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
arr=[6,5,4,3,2,1]
quick_sort(arr,0,5)
for i in range(len(arr)):
    print(arr[i],end=' ')
