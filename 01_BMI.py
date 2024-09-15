weight = float(input('Podaj swoją wagę w kg (zapis xx.x): '))
height = float(input('Podaj swój wzrost w m (zapis x.xx): '))
BMI = weight / (height ** 2)
print(f'Twoje  BMI wynosi: {BMI:.2f} ')