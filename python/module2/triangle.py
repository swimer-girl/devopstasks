#!/usr/bin/env python3
from sys import argv
from math import sqrt

if not len(argv) == 4:
    print('Скрипт принимает 3 значения')
a = int(argv[1])
b = int(argv[2])
c = int(argv[3])

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c)/2
    S = sqrt(p * (p - a) * (p-b) * (p-c))
    print(S)
else:
    print('Таких сторон треугольника не существует')



