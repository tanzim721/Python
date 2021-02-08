"""
Name : Tanzimul Islam
Roll : 180636
Session : 2017-18
E-mail : tanzimulislam799@gmail.com
Blog : https://tanzim36.blogspot.com/
Dept.of ICE, Pabna University of Science and Technology
"""
#Problem-6: Write a program to sort a linear array using the Selection Sort algorithm
from array import *
#Selection sorting
def selectionSort(arr):
    for i in range(len(arr)):
        mi = i
        for j in range(i+1, len(arr)):
            if arr[mi] > arr[j]:
                mi = j
        arr[i], arr[mi] = arr[mi], arr[i]

#for printing
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

#main function
while True:
    n = int(input("Enter the number : "))
    arr = array('i',[])
    print("Enter the array elements : ")
    for i in range(0,n):
        x = int(input())
        arr.append(x)

    print("Given an array : ")
    printList(arr)
    selectionSort(arr)
    print("\nAfter sorting an array : ")
    printList(arr)