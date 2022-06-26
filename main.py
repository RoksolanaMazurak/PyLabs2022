from dbList import Dblist
from employee import Employee


if __name__ == "__main__":
    db_list = Dblist()
    employee = Employee("Andrii", "Mykolenko", "none", "none", 13, 1995)
    employee1 = Employee("Natalia", "Melnyk", "none", "none", 8, 1995)
    employee2 = Employee("Roksolana", "Mazurak", "Lviv National Polytechnic University ",  "none", 0, 2004)
    employee3 = Employee("Oleg", "Mazurak", "Lviv National University", "none", 5, 1995)

    db_list.add(employee)
    db_list.add(employee1)
    db_list.add(employee2)
    db_list.add(employee3)
    db_list.print_by_surname("Mazurak")
    print()

    db_list.incertion_sort()

    for e in db_list:
        print(e)



