#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyPair:

    def __init__(self, value1=0.0, value2=0.0):
        value1 = float(value1)
        value2 = float(value2)

        self.__value1 = value1
        self.__value2 = value2

    @property
    def value1(self):
        return self.__value1

    @value1.setter
    def value1(self, value):
        self.__value1 = float(value)

    @property
    def value2(self):
        return self.__value2

    @value2.setter
    def value2(self, value):
        self.__value2 = float(value)

    def __str__(self):
        return f"Value1: {self.__value1}, Value2: {self.__value2}"

    def __mul__(self, factor):
        return MyPair(self.__value1 * factor, self.__value2 * factor)

    def __eq__(self, other):
        return self.__value1 == other.__value1 and self.__value2 == other.__value2

    def __ne__(self, other):
        return self.__value1 != other.__value1 or self.__value2 != other.__value2


if __name__ == '__main__':
    pair = MyPair(3, 2)
    factor = float(input("Введите множитель для умножения: "))
    result_pair = pair * factor
    print(f"Результат умножения: {result_pair}")

    pair2 = MyPair(3, 2)
    print(f"Сравнение пар на равенство: {pair == pair2}")
    print(f"Сравнение пар на неравенство: {pair != pair2}")
