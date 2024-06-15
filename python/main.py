#!/usr/bin/python3

int = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def sort(a):
    for i in range (0, len(a) -1):
        t = a[i]
        a[i] = a[i + 1]
        a[i + 1] = a[i]
    return a

print(sort(int))