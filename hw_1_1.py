# Задача №1
# filename: hw_1_1.py
#
# Запросить у пользователя имя и фамилию.
# Поприветсвовать пользователя с использованием его имени и фамилии.
# Запросить День даты рождения (цело число).
# Запросить Месяц даты рождения (цело число).
# Запросить Год даты рождения (цело число).
# Вывести количество прожитых лет (цело число).
# Вывести количество прожитых месяцев (цело число).
# Вывести количество прожитых дней, месяцев, лет до даты начала курса 31.01.2019 - без учёта високосных лет и считая, что среднее количество дней в месяце = 30.



Name = input("enter your name /// ")
Surname = input("enter your surname >>> ")
print('Hello,dear',Name,Surname)
birth_day = int(input('enter your date :  '))
print(birth_day)
birth_month = int(input('enter your month: '))
print(birth_month)
birth_year = int(input('enter your year: '))
print(birth_year)
print('your birstdate >>> ' , birth_year, birth_month, birth_day)


day = 31
month = 1
year = 2019
print(day,month,year)
date = (day-birth_day)
date1 = (((month-birth_month)%12))
date2 = (year-birth_year)
print('days= ',date,'months= ',date1,'years= ',date2)


