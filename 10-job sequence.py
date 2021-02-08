"""
Name : Tanzimul Islam
Roll : 180636
Session : 2017-18
E-mail : tanzimulislam799@gmail.com
Blog : https://tanzim36.blogspot.com/
Dept.of ICE, Pabna University of Science and Technology
"""
#Problem-10: Write a program using greedy method to solve this problem when no of job 𝑛 = 5, profits (𝑃1, 𝑃2, 𝑃3, 𝑃4, 𝑃5)=(3,25,1,6,30) and deadlines (𝑑1,𝑑2, 𝑑3, 𝑑4, 𝑑5)=(1,3,2,1,2).
def printJobScheduling(arr, t):
    # length of array
    n = len(arr)
    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # To keep track of free time slots
    result = [False] * t
    # To store result (Sequence of jobs)
    job = ['-1'] * t
    # Iterate through all given jobs
    for i in range(len(arr)):

        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    # print the sequence
    print(job)

# main function
arr = [['a', 1, 3],
       ['b', 3, 25],
       ['c', 2, 1],
       ['d', 1, 6],
       ['e', 2, 30]]
print("Following is maximum profit sequence of jobs")
# Function Call
printJobScheduling(arr, 3)