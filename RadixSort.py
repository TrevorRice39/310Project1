from Array_Queue import ArrayQueue
import math


def radix_sort(a):
    q = [ArrayQueue() for i in range(10)]  # initializing containers (0 - 9)
    max_digits = 0
    for i in range(len(a)):  # finding the number of digits in the largest number
        d = int(math.ceil(math.log(a[i], 10)))
        if d > max_digits:
            max_digits = d

    # main for loop
    for i in range(max_digits):
        for j in range(len(a)):  # scans the list of numbers
            #  (a[j]//10**i) % 10 is the index of the correct container
            q[(a[j]//10**i) % 10].enqueue(a[j])  # enqueuing the number in the correct container (0 - 9)
        index = 0
        for j in range(10):  # copying the elements in each container back into the list
            while not q[j].is_empty():
                a[index] = q[j].dequeue()
                index += 1


# main
a = [35, 53, 55, 33, 52, 32, 25]

print('Unsorted: ')
for i in range(len(a)):  # printing the original list of numbers
    print(a[i], end=' ')
print()
print()
radix_sort(a)
print('Sorted: ')
for i in range(len(a)):  # printing the sorted list
    print(a[i], end=' ')





















