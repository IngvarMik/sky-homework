

year=input("введите год :")# запрос года инпут
year=int(year) # устанавливаем  число интегер
if (year%4==0): # делим на 4 -- високосный
    print(f"год   {year} : Trye") # если без остатка то високосный
else: # иначе
     print(f"год  {year} : False") # невисокосный
     
         
        