money = float(input("Введите сумму покупки: "))

if money > 1000:
    itog = money * 0.9
    print(f"С учетом скидки к оплате: {itog:g}")
else:
    prit(f"К оплате: {money:g}")