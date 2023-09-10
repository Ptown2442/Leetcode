import math
from math import sqrt




def duplicates(nums, target):
    ans = 0
    try:
        ans = nums.index(target)
    except ValueError:
        for i in nums:
            if i < target:
                ans += 1

    return ans

target = 5
nums = [4, 7, 8]


def plus_one(digits):
    lengthn = len(digits)
    digits[lengthn-1] += 1
    for i in range(0,lengthn):
        val = lengthn - 1 - i
        if digits[val] >= 10 and i == (lengthn - 1):
            digits[val] -= 9
            digits.append(0)
        elif digits[val] >= 10:
            digits[val] -= 10
            digits[val-1] += 1
        else:
            pass

    return digits



digits = [3, 4, 4, 5]



def roman_maker(num):
    store = num
    rep = ''
    m = 'M'
    i = 'I'
    iv = 'IV'
    v = 'V'
    ix = 'IX'
    x = 'X'
    xl = 'XL'
    l = 'L'
    xc = 'XC'
    c = 'C'
    cd = 'CD'
    d = 'D'
    cm = 'CM'
    while store > 0:
        if store >= 1000:
            rep += m
            store -= 1000
        elif store >= 900:
            rep += cm
            store -= 900
        elif store >= 500:
            rep += d
            store -= 500
        elif store >= 400:
            rep += cd
            store -= 400
        elif store >= 100:
            rep += c
            store -= 100
        elif store >= 90:
            rep += xc
            store -= 90
        elif store >= 50:
            rep += l
            store -= 50
        elif store >= 40:
            rep += xl
            store -= 40
        elif store >= 10:
            rep += x
            store -= 10
        elif store >= 9:
            rep += ix
            store -= 9
        elif store >= 5:
            rep += v
            store -= 5
        elif store >= 4:
            rep += iv
            store -= 4
        else:
            rep += i
            store -= 1

    return rep


num = 321

def delete_n(ans, n):

    amount = len(ans)
    for i in range(0, amount):
        if i == (amount - n):
            ans.remove(ans[i])

    return ans



head = [1, 3, 7, 6, 8, 9]
n = 3


def reverse(x):
    x = x
    tempx = x
    ans = 0
    count = 0
    negative = False
    if x < 0:
        negative = True
        x *= -1
        tempx *= -1
    else:
        pass

    list = []
    while tempx >= 10:
        tempx /= 10
        count += 1


    for i in range(0,count):
        temp_val = x
        val = (temp_val - (int(temp_val/10)* 10))
        list.append(val)
        x = int(x/10)

    list.append(x)

    for l in range(0,count + 1):
        index = count - l
        val = list[l] * (10 ** index)
        ans += val

    if negative: ans *= -1
    ans = int(ans)

    if (-2 ** 31) < ans < ((2 ** 31) -1):
        ans = ans
    else:
        ans = 0


    return ans







z = 1534236469
y = 9646324351

def matrix_rotate(matrix):
    clone = matrix
    matrix = matrix
    i = 0
    count = len(matrix)
    while i < count:
        for items in matrix:
            matrix[i][(count - 1 - items)] = clone[i][items]
            i += 1

        return matrix





leads = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]


def link_list_add_reverse(l1, l2):
    count1 = 0
    count2 = 0
    ans = []
    for x in l1:
        count1 += 1

    for y in l2:
        count2 += 1

    if count1 > count2:
        smallest = count2
        largest = count1
    else:
        smallest = count1
        largest = count2

    difference = largest - smallest

    for i in range(0,smallest):
        val = l1[i] + l2[i]
        ans.append(val)

    if difference >= 1:
        if l1[smallest]:
            for finisher in range(0,difference):
                ans.append(l1[finisher + smallest])
        else:
            for finisher in range(0,difference):
                ans.append(l2[finisher + smallest])


    return ans

def buddy_str(s,goal):
    amount = len(s)
    go = len(goal)
    ref = []
    val = 0
    if goal == s and go == 2:
        if goal[0] != goal[1]:
            return False
        else:
            pass
    elif go == 2 and (goal[0] != s[1] or s[0] != goal[1]):
        return False
    elif amount != go:
        return False

    for i in range(amount):
        if val == 2 and goal[i] != s[i]:
            return False
        elif val == 1 and goal[i] != s[i]:
            if goal[i] != ref[0]:
                return False
            else:
                val += 1
        elif val == 0 and goal[i] != s[i]:
            ref.append(s[i])
            val += 1
        else:
            pass

    return True

getit = 'badc'
x = 'abcd'
print(buddy_str(x,getit))