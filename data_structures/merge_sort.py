def merge(a1,a2,a):## this function will be used  in the merge sort function

    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            k=k+1
            i=i+1

        else :
            a[k]=a2[j]
            k=k+1
            j=j+1

    while i<len(a1):
        a[k]=a1[i]
        k=k+1
        i=i+1

    while j<len(a2):
        a[k]=a2[j]
        k = k + 1
        j=j+1

    # return a




def merge_sort(a):
    l = len(a)

    if l==0 or l==1:
        return

    mid_point = l//2

    a1 = a[0:mid_point]
    a2 = a[mid_point:]
    merge_sort(a1)
    merge_sort(a2)
    merge(a1,a2,a)



l = [2,5,1,4,5,6]

print(merge_sort(l))

print(l)




