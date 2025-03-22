def Bubble_sort(a):
    l = len(a)
    for i in range(l):
        for j in range(l-i-1):
            if a[j]>a[j+1]:
#                 a[j] = a[j+1]
#                 a[j+1] =a[j]
                a[j], a[j+1] = a[j+1], a[j]   ## tuple unpacking and packing



def Bubble_sort1(a):
    l = len(a)
    for i in range(l):
        for j in range(l-i-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index (i) has the minimum value
        min_index = i

        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)


def merged(a1, a2):
    result = []
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
            k += 1
        else:
            result.append(a2[j])
            j += 1
            k += 1
    if i == len(a1):
        return result + a2[j:]
    if j == len(a2):
        return result + a1[i:]


def merged_sort(a):  ### giving incorrect ouptut
    if len(a) == 0 or len(a) == 1:
        return
    l = len(a)
    mp = len(a) // 2
    a1 = a[0:mp]
    a2 = a[mp:l]
    merged_sort(a1)
    merged_sort(a2)
    x = merged(a1, a2)
    return x


def merged_second_approach(a1, a2, a):
    i = 0
    j = 0
    k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1

    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1


def merged_sort_second_approach(a):
    if len(a) == 0 or len(a) == 1:
        return
    l = len(a)
    mp = len(a) // 2
    a1 = a[0:mp]
    a2 = a[mp:l]
    merged_sort_second_approach(a1)
    merged_sort_second_approach(a2)
    merged_second_approach(a1, a2, a)


def partition(a, si, ei):
    pivot = a[si]
    c = 0
    for i in range(si, ei + 1):
        if a[i] < pivot:
            c += 1
    a[si + c], a[si] = a[si], a[si + c]

    pivot_index = si + c

    i = si
    j = ei

    while i < j:
        if a[i] < pivot:
            i += 1
        elif a[j] >= pivot:
            j -= 1


        else:
            a[i], a[j] = a[j], a[i]

            i += 1
            j -= 1

        return pivot_index


def quick_sort(a, si, ei):
    if si >= ei:
        return
    pivot_index = partition(a, si, ei)
    quick_sort(a, si, pivot_index - 1)
    quick_sort(a, pivot_index + 1, ei)