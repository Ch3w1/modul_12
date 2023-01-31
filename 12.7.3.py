per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму:"))
L = []
for x in per_cent: L.append(int(per_cent[x] * money / 100))
max_deposit = max(L)
print("deposit=" + str(L))
print("Максимальная сумма которую вы можете заработать:" + str(max_deposit))
