#5. Escriure un programa que converteixi un valor donat en graus Fahrenheit a graus Celsius. Recordeu que la fórmula per a la conversió és:

farenheit = float(input("Temperatura en F: "))
celsius = (farenheit-32) * 5/9
print(f"{celsius:.2f}")