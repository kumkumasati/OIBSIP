"""
BMI Calculator - Beginner Tier
------------------------------
A command-line tool that:
  1. Prompts the user for weight (kg) and height (m)
  2. Calculates BMI = weight / (height ** 2)
  3. Classifies the result into standard health categories
  4. Displays the BMI rounded to 2 decimal places, with the category
  5. Validates input: rejects non-numeric and negative/zero values,
     re-prompting with a helpful error message until valid input is given

Run:
    python bmi_calculator.py

Type "exit" at any prompt to quit.
"""

import sys


def get_positive_float(prompt: str) -> float:
    """
    Repeatedly prompt the user until a valid positive number is entered.
    Typing 'exit' or 'quit' ends the program.
    """
    while True:
        raw = input(prompt).strip()

        if raw.lower() in ("exit", "quit"):
            print("Goodbye!")
            sys.exit(0)

        try:
            value = float(raw)
        except ValueError:
            print(f"  ⚠️  '{raw}' is not a valid number. Please enter numbers only (e.g. 65.5).")
            continue

        if value <= 0:
            print("  ⚠️  Value must be greater than zero. Please try again.")
            continue

        return value


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kilograms and height in metres."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """Return the standard health category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 45)
    print("           BMI CALCULATOR")
    print("=" * 45)
    print("Enter your details below (type 'exit' to quit).\n")

    while True:
        weight = get_positive_float("Enter your weight in kilograms (kg): ")
        height = get_positive_float("Enter your height in metres (e.g. 1.75): ")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print("\n" + "-" * 45)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category:    {category}")
        print("-" * 45)

        print("\nReference ranges:")
        print("  Underweight   : < 18.5")
        print("  Normal weight : 18.5 – 24.9")
        print("  Overweight    : 25 – 29.9")
        print("  Obese         : ≥ 30")

        again = input("\nCalculate another BMI? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
