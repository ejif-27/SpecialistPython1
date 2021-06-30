# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
brands = []
for item in items:
    if item["brand"] not in brands:
        brands.append(item["brand"])
print("Товары на складе представлены брэндами: ",", ".join(brands))

# TODO: your code here
sum_brands = dict.fromkeys(brands, 0)
max_sum = 0
max_brand_list = []
for item in items:
    for brand in sum_brands:
        if item["brand"] == brand:
            sum_brands[brand] += 1
for brand in sum_brands:
    if sum_brands[brand] > max_sum:
        max_sum = sum_brands[brand]
for brand in sum_brands:
    if sum_brands[brand] == max_sum:
        max_brand_list.append(brand + ' = ' + str(max_sum))
print("На складе больше всего товаров брэнда(ов): ",", ".join(max_brand_list))

# TODO: your code here
max_price = 0
max_price_brand_list = []
for item in items:
    if item["price"] > max_price:
        max_price = item["price"]
for item in items:
    if item["price"] == max_price:
        max_price_brand_list.append(item["brand"])

print("На складе самый дорогой товар брэнда(ов): ", ", ".join(max_price_brand_list))
