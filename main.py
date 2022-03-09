def insertion_sort(list, n):
    i = 1
    for i in range(n):
        j = i
        while(j > 0 and list[j] < list[j - 1] ):
            temp = list[j - 1]
            list[j - 1] = list[j]
            list[j] = temp
            j = j-1
    return list

if __name__ == '__main__':
    list = [ 4, 8, 7, 12, 3, 24]
    insertion_sort(list, len(list))
    print(list)
    list = ["this", "is", "a", "list", "of", "words"]
    insertion_sort(list, len(list))
    print(list)
