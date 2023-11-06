'''var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)'''

#carry flag to 1
flag_register = 0b100

#set zero flag to 1

flag_register |= 0b100 #|= representa ou

#set the overflow flag to 1

flag_register &= ~0b001 # & representa and, ~ representa negado 
 


