number = input("Введите число:")
quantity = len(number)
copy = number
number = int(number)
word = set()
som = ["а если тут", "mb da"]

for rank in range(1, quantity):
	dis = copy[rank:quantity]
	if dis[0] != "0":	
		dis = int(dis)
		result = number - dis
		number -= result
		print("Разряд номер " + str(rank) + " :" + str(result))
		dis = str(dis)
		for factor in range(1, result + 1):
			if not result % factor:
				for i in range(1, factor + 1):
					if not factor % i:
						
						word.add(i)
						if factor == i and word:
							
							if len(word) == 2:
								print("Простым множителем числа " + str(result) + " является: "+ str(i))
								word.clear()
							elif len(word) != 2:
								word.clear()
						elif factor == i and not word:
							word.clear()

		if len(dis) == 1:
			print("Разряд номер " + str(rank) + " :" + str(dis))
			dis = int(dis)
			for factor in range(1, dis + 1):
				if not dis % factor:
					for i in range(1, factor + 1):
						if not factor % i:
							
							word.add(i)
							if factor == i and word:
								
								if len(word) == 2:
									print("Простым множителем числа " + str(dis) + " является: "+ str(i))
									word.clear()
								if len(word) != 2:
									word.clear()
							elif factor == i and not word:
								word.clear()
