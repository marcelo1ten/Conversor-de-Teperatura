def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 1.8) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) / 1.8
  return celsius

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter choice: "))

if choice == 1:
  celsius = float(input("Enter temperature in Celsius: "))
  fahrenheit = celsius_to_fahrenheit(celsius)
  print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
elif choice == 2:
  fahrenheit = float(input("Enter temperature in Fahrenheit: "))
  celsius = fahrenheit_to_celsius(fahrenheit)
  print("Temperature in Celsius: {:.2f}".format(celsius))
else:
  print("Invalid Input")
