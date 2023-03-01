def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            # if not in proper order swap it
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[3 ,1,4,6,9]
bubblesort(arr)

for i in range(len(arr)):
    print(arr[i])