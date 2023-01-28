# 1번
from itertools import combinations as cb

heights = []

for _ in range(9):
    heights.append(int(input()))

list_cb = list(cb(heights,7))

for numbers in list_cb:
    if sum(numbers) == 100:
        numbers = list(numbers)
        numbers.sort()
        for number in numbers:
            print(number)
        break
      
     
# 2번
from itertools import permutations as pm

# 소수 판별
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,i)
            return False
    return True

# map 함수를 위한 함수
def func_join(x):
    return int("".join(x))

# solution 함수
def solution(numbers):
    numbers = list(numbers)
    list_pm = []
    for i in range(1,len(numbers)+1):
        list_pm += list(pm(numbers,i))
    list_pm = list(set(list(map(func_join,list_pm))))
    answer = 0
    print(list_pm)
    for number in list_pm:
        if prime_number(number):
            answer += 1
    return answer
