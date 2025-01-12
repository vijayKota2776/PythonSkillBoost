import random

def knuth_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i) 
        lst[i], lst[j] = lst[j], lst[i]
lst = [1, 2, 3, 4, 5]
print("Original list:", lst)

knuth_shuffle(lst)

print("Shuffled list:", lst)
