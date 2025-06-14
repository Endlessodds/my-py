def calculate_bmi(weight, height, unit='metric'):
    if unit == 'metric':
        bmi = weight / (height ** 2)
    elif unit == 'imperial':
        bmi = 703 * weight / (height ** 2)
    else:
        raise ValueError("Unit must be 'metric' or 'imperial'")
    return round(bmi, 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    unit = input("Choose unit system (metric/imperial): ").strip().lower()
    
    if unit == 'metric':
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    elif unit == 'imperial':
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
    else:
        print("Invalid unit system.")
        return

    bmi = calculate_bmi(weight, height, unit)
    category = categorize_bmi(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()
