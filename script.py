per_cent = {'OP': 2.6, 'Aktia': 1.9, 'Nordea': 2.28, 'S-Bank': 3.0}

money = int(input("Please, enter the amount of money in integer format:"))

deposit = list(map(lambda x: round(x*money/100), per_cent.values()))

#print (deposit)

max_value = max(deposit)

print ("Максимальная сумма, которую вы можете заработать — ", max_value)
