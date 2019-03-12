from pprint import pprint
import random
import os

def check_square(arr):
    return sum(arr[0:2]) == sum(arr[3:5]) == sum(arr[6:8])\
        == arr[0] + arr[3] + arr[6] \
        == arr[1] + arr[4] + arr[7] \
        == arr[2] + arr[5] + arr[8] \
        == arr[0] + arr[4] + arr[8] \
        == arr[2] + arr[4] + arr[6]

lower = 1
upper = 250

found = False

res_array = []

while not found:
    os.system('clear')
    res_array = []
    for x in range(9):
        num = random.randint(lower, upper)
        while (num * num) in res_array:
            num = random.randint(lower, upper)
        res_array.append(num * num)
    pprint(res_array, width=80)
    found = check_square(res_array)
    del res_array[:]
