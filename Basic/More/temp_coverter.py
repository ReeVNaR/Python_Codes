def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").strip().upper()
temp = float(input("Enter temperature: "))

if choice == 'C':
    print("Fahrenheit:", celsius_to_fahrenheit(temp))
elif choice == 'F':
    print("Celsius:", fahrenheit_to_celsius(temp))
else:
    print("Invalid choice!")
