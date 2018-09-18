#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# a, b = 0, 1
#
# while b < 100:
#     print(b, end=' ')
#     a, b = b, a+b


i = 1
print("-" * 50)

while i < 11:
    n = 1
    while n <= 10:
        # print("{:4d}".format(i * n), end=" ")
        print("%s * %s = %s " %  i, n, (i * n)
        n += 1
    print()
    i += 1
print('-' * 50)
