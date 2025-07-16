def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("📏🧪 Welcome to Unit Converter 🧪📏")
    print("1. cm to inch")
    print("2. inch to cm")
    print("3. kg to lb")
    print("4. lb to kg")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Exit")

    while True:
        choice = input("\nChoose an option (1-7): ")

        if choice == '1':
            cm = float(input("Enter length in cm: "))
            print(f"{cm} cm = {cm_to_inch(cm):.2f} inches")
        elif choice == '2':
            inch = float(input("Enter length in inches: "))
            print(f"{inch} inches = {inch_to_cm(inch):.2f} cm")
        elif choice == '3':
            kg = float(input("Enter weight in kg: "))
            print(f"{kg} kg = {kg_to_lb(kg):.2f} lb")
        elif choice == '4':
            lb = float(input("Enter weight in lb: "))
            print(f"{lb} lb = {lb_to_kg(lb):.2f} kg")
        elif choice == '5':
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
        elif choice == '6':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
        elif choice == '7':
            print("👋 Exiting the converter. Bye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
