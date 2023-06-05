# Python_B1_2_DmitrievaOA_1432_05

s = input("Enter the string: ") # Введите строку:

for i in range(len(s)):
    if i == 2:
        continue
    if s[i] == 'c':
        print(" Found symbol c") # Найден символ c:
    print(s[i], end='')

print("\nLine length:", len(s)-1) # Длина строки:
