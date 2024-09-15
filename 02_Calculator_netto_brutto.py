value_netto = float(input('Podaj wartość netto, aby móc obliczyć wartość brutto przy 23% VAT: '))
tax_VAT = 0.23
value_brutto = (value_netto * tax_VAT)+value_netto
print(f'Wartość brutto wynosi: {value_brutto:.2f}')
