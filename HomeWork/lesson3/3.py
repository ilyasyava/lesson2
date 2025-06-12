phone_my_price = float(input("Введите цену закупки телефона: "))

phone_shop_price = phone_my_price * 1.3
phone_discount_5 = phone_shop_price * 0.95
phone_discount_10 = phone_shop_price * 0.90
phone_discount_15 = phone_shop_price * 0.85

b = phone_shop_price
c = phone_discount_5
d = phone_discount_10
e = phone_discount_15

print("    ------ Информация по ценам ------\n"
      f'    - Цена телефона без скидок = {b}\n'
      f'    - Цена телефона со скидкой в 5% = {c}\n'
      f'    - Цена телефона со скидкой в 10% = {d}\n'
      f'    - Цена телефона со скидкой в 15% = {e}'
      )

