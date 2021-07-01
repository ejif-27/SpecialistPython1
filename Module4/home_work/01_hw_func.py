# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
        start = [int(n) for n in str(ticket_number)[0:3]]
        end = [int(n) for n in str(ticket_number)[3:6]]
        if sum(start) == sum(end):
         return("Lucky")
        else:
         return("not Lucky")

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
