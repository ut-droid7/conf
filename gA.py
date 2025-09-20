#бинарный поиск
# def f(s, i):
#     low = 0
#     high = len(s)-1
#     while low <= high:
#         mid = (low + high) // 2
#         if s[mid] > i:
#             high = mid - 1
#         if s[mid] < i:
#             low = mid + 1
#         if s[mid] == i:
#             return mid
#     return None

# def countdown(i):
#   if i <= 0:    Базовый случай
#       return
#   else:
#       print(i)    Рекурсивный случай
#       countdown(i-1)

# s = set()     егэ 23 задание
# def f(a, c):
#     if c == 14:      база
#         s.add(a)
#         return
#     return f(a+4, c+1), f(a*2, c+1), f(a*2 + 1, c+1)   рекурсия
# f(1, 0)
# print(len(s))

# def sm(list):  сумма
#     if list == []:
#         return 0
#     return list[0] + sm(list[1:])
# s = [1, 1,  1, 1 , 45]
# print(sm(s))

#s = [121, 34, 9099, 87, 444]
# def f(x):
#     if len(x) == 2:
#         if x[0] > x[1]:
#             return x[0]
#         else:
#             return x[1]
#     mx = f(x[1:])
#     if mx < x[0]:
#         return x[0]
#     else:
#         return mx
# print(f(s))

#быстрая сортировка
def sort(s):
    if len(s) < 2:
        return s
    else:
        opor = s[0]
        bigger = [i for i in s[1:] if i > opor]
        smaller = [i for i in s[1:] if i < opor]
        return sort(smaller) + [opor] + sort(bigger)
print(sort([1,-3245, 452, 9, 345, 56, 0, 3, -3222]))




