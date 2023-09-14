per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму целым числом:"))

deposit = list(map(lambda x: round(x*money/100), per_cent.values()))

#print (deposit)

max_value = max(deposit)

print ("Максимальная сумма, которую вы можете заработать — ", max_value)
