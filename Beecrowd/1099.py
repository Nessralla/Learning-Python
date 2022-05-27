# For each test case, print the sum of all odd values between X and Y, not including them.

tCase = int(input())



for i in range(tCase):
    somaProv = 0
    a,b = list(map(int,input().split()))
    if a > b:
        for j in range(b+1,a):
            if j % 2 != 0:
                somaProv += j
    else:
        for j in range(a+1,b):
            if j % 2 != 0:
                somaProv +=j
    print(somaProv)