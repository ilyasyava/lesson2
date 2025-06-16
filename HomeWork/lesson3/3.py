phone_my_price = float(input("Введите цену закупки телефона: "))

phone_shop_price = phone_my_price * 1.3
phone_discount_5 = phone_shop_price * 0.95
phone_discount_10 = phone_shop_price * 0.90
phone_discount_15 = phone_shop_price * 0.85

print("    ------ Информация по ценам ------\n"
      f'    - Цена телефона без скидок = {phone_shop_price}\n'
      f'    - Цена телефона со скидкой в 5% = {phone_discount_5}\n'
      f'    - Цена телефона со скидкой в 10% = {phone_discount_10}\n'
      f'    - Цена телефона со скидкой в 15% = {phone_discount_15}'
)