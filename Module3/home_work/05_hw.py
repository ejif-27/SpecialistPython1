# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

import random
names = ["Иван", "Ирина", "Вячеслав", "Вrчеслав", "Болеслав", "Василий", "Автандил", "Петр" , "Ульманас"]
max_len_str = 0
for name in names:
    if len(name) > max_len_str:
        max_len_str = len(name)
        max_name = name
    elif len(name) == max_len_str:
        max_name_list = [name, max_name]
        max_name = random.choice(max_name_list)
print(max_name)

# TODO: your code here
