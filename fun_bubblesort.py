#file containing bubble sort function
def bubble_sort(items):
    flag = 'true'
    x = len(items)-1
    while flag=='true':
        flag = 'false'
        while (x > 0):
            if items[x] < items[x-1]:
                items[x], items[x-1] = items[x-1], items[x]
                flag = 'true'
            x -= 1
        x = len(items)-1
    return items

table = list(input("Enter the list for sort: "))

print (bubble_sort(table))
