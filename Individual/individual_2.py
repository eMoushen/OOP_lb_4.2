#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    MAX_SIZE = 10

    def __init__(self):
        self.bills = []
        self.size = self.MAX_SIZE
        self.count = 0

    def get_size(self):
        return self.size

    def add_bill(self, denomination, count):
        if self.count + count > self.size:
            print("Превышен максимальный размер списка")
            return

        for bill in self.bills:
            if bill["denomination"] == denomination:
                bill["count"] += count
                break
        else:
            self.bills.append({"denomination": denomination, "count": count})
        self.count += count

    def total_amount(self):
        total = 0
        for bill in self.bills:
            total += bill["denomination"] * bill["count"]
        return total

    def __add__(self, other):
        if isinstance(other, Money):
            new_money = Money()
            new_money.bills = [bill.copy() for bill in self.bills]

            for bill in other.bills:
                if new_money.count + bill["count"] > new_money.size:
                    print(f"Превышен максимальный размер списка ({bill['denomination']})")
                    return self

                new_money.add_bill(bill["denomination"], bill["count"])

            return new_money
        else:
            raise TypeError("Неверный тип операнда")

    def __getitem__(self, index):
        if 0 <= index < len(self.bills):
            return self.bills[index]["denomination"]
        else:
            raise IndexError("Индекс вне диапазона")

    def print_money(self, label):
        print(f"\n{label}:")
        print("\n".join([f"{bill['denomination']}: {bill['count']} шт." for bill in self.bills]))


if __name__ == "__main__":
    money1 = Money()
    money1.add_bill(10, 5)
    money1.add_bill(50, 3)
    money1.add_bill(100, 2)

    money2 = Money()
    money2.add_bill(10, 5)
    money2.add_bill(50, 1)
    money2.add_bill(100, 2)
    money2.add_bill(20, 2)

    money1.print_money("Текущий состав денег (money1)")
    money2.print_money("Текущий состав денег (money2)")

    money3 = money1 + money2
    money3.print_money("Сумма денег (money1 + money2)")

    print(f"\nРазмер списка (money1): {money1.get_size()}")
