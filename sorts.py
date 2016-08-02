def insertion_sort(array):
    for i in xrange(len(array)):
        temp = array[i]
        pointer = i

        while pointer > 0 and temp < array[pointer-1]:
            array[pointer] = array[pointer-1]
            pointer -= 1
        array[pointer] = temp
    return array

print insertion_sort([3,2,7,5,9,1])


def merge_sort(array):
    if len(array) > 1:
        mid = len(array)/2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        l_i = 0
        r_i = 0
        z_i = 0

        while l_i < len(left) and r_i < len(right):
            if left[l_i] < right[r_i]:
                array[z_i] = left[l_i]
                l_i += 1
            elif left[l_i] > right[r_i]:
                array[z_i] = right[r_i]
                r_i += 1
            else:
                array[z_i] = left[l_i]
                z_i += 1
                array[z_i] = right[r_i]
                l_i += 1
                r_i += 1
            z_i += 1

        while l_i < len(left):
            array[z_i] = left[l_i]
            l_i += 1
            z_i += 1

        while r_i < len(right):
            array[z_i] = right[r_i]
            r_i += 1
            z_i += 1

    return array

print merge_sort([3,2,15, 9, 3, 7,5,9,1])
