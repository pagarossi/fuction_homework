
# Это первое домащнее задание с функициями где нужно было завернуть
# значения в обертки.

#____________________
from os import system
system ('clear')
#°°°°°°°°°°°°°°°°°°°

# 1 функция
def wrap_brackest(text):
    return  "(" + text + ")"

# 2 функция
def kvadrat (wrap_brackest):
    return "[[[" + wrap_brackest + "]]]"

# 3 функция
def bolshemenishe (kvadrat):
    return "<<<" + kvadrat + ">>>"
print ()
print (bolshemenishe(kvadrat(wrap_brackest("12345"))))
print ()


