def max_heapify(arr,size,i):
    greatest=i
    left=2*i+1
    right=2*i+2
    if(left<size and arr[left]>arr[greatest]):
        greatest=left
    if(right<size and arr[right]>arr[greatest]):
        greatest=right
    if(greatest!=i):
        arr[i],arr[greatest]=arr[greatest],arr[i]
        max_heapify(arr,size,greatest)
def heap_sort(arr,size):
    for i in range(size//2-1,-1,-1):
        max_heapify(arr,size,i)
    for i in range(size-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,i,0)
arr=[6,5,4,3,2,1]
heap_sort(arr,len(arr))
for i in range(len(arr)):
    print(arr[i],end=' ')
