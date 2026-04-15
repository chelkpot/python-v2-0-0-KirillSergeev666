X, Y, Z = map(int, input().split())

# Цены
price_pencil = 3
price_pen = price_pencil + 2      # 5 рублей
price_marker = price_pen + 7      # 12 рублей

# Общая стоимость покупки
total_cost = X * price_pencil + Y * price_pen + Z * price_marker

# Вывод результата
print(total_cost)