
my_age=input (" введите возраст  :") # ЗАПРОС через инпут возраста
my_age=int(my_age) # этой строкой мы подтверждаем, что значение возраста не строчное, а цифровое!!! интегер 
print( f" Ваш возраст : { my_age} ") # печать первого возраста

my_age=my_age+1 # ДОБАВКА К ВОЗРАСТУ 1 ГОД -- и здесь my_age воспринимается как строчная, если не ввести команду на строке номер три!!!!
print(f"ваш возраст плюс один год  : {my_age}")# печать 
             
