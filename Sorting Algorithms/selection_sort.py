def selection_sort(arr):
    #Loops from the first index to the second last
    for i in range(len(arr)-1):
        #saving the value of i as min_idx
        min=i
        for j in range(i+1,len(arr)):
            #min_idx updated every time we hit an element less than that
            #at the min_idx
            if(arr[j]<arr[min]):
                min=j
        #swap places of minimum of unsorted list
        arr[min],arr[i]=arr[i],arr[min]
arr=[6,5,4,3,2,1]
selection_sort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')
