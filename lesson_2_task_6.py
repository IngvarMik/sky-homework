# создан список , вывести элементы которые 
# делятся на 3 без остатка---  if i%3==0 ? 
# меньше 30 ---  if i<30 ? -- для for?

list=[11,5,8,32,15,3,20,132,21,4,555,9,20] # список
for i in list:  # для i в спсике лист
    if i%3==0 and i<30: # условие -- если i поделить на 3 без остатка и i меньше 30
        print (i) # тогда принт i