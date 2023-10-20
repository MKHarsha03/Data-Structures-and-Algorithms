def insertion_sort(arr):
    #runs from the second element of the array to the last element
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        #Compares the key to every element before it and copies the
        #value of the previous element in the correct spot
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        #key is placed in the correct spot
        arr[j+1]=key
#An example array to check if the function sorts the array
arr=[6,5,4,3,2,1]
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')

