# BMI Calculator (Beginner Tier)

A simple command-line Python program that calculates your Body Mass Index
(BMI) and tells you which standard health category it falls into.

## Project Structure

```
bmi_calculator/
├── bmi_calculator.py   # main program
└── README.md           # this file
```

## Features

- ⌨️ Prompts for weight (kg) and height (m) via the command line
- 🧮 Calculates BMI using the formula: `BMI = weight / (height ** 2)`
- 🏷️ Classifies the result into standard categories:
  - Underweight: < 18.5
  - Normal weight: 18.5 – 24.9
  - Overweight: 25 – 29.9
  - Obese: ≥ 30
- 🎯 Displays BMI rounded to 2 decimal places, with the category
- ✅ Input validation — rejects non-numeric and non-positive input with a
  helpful error message and re-prompts until valid input is given
- 🔁 Lets you calculate BMI for multiple people in one session
- 🚪 Type `exit` or `quit` at any prompt to leave immediately

## Requirements

- Python 3.7+ (no external libraries needed — pure standard library)

## Setup Instructions

### 1. Install Python
Download and install Python from https://www.python.org/downloads/ if you
don't already have it. Confirm it's installed:

```bash
python --version
```

### 2. Get the project files
Place `bmi_calculator.py` and this `README.md` in a folder on your computer
(you already have this from the download).

### 3. Run the program

No dependencies to install — just run it directly:

```bash
cd bmi_calculator
python bmi_calculator.py
```

(On some systems you may need `python3` instead of `python`.)

## Example Session

```
=============================================
           BMI CALCULATOR
=============================================
Enter your details below (type 'exit' to quit).

Enter your weight in kilograms (kg): 70
Enter your height in metres (e.g. 1.75): 1.75

---------------------------------------------
Your BMI is: 22.86
Category:    Normal weight
---------------------------------------------

Reference ranges:
  Underweight   : < 18.5
  Normal weight : 18.5 – 24.9
  Overweight    : 25 – 29.9
  Obese         : ≥ 30

Calculate another BMI? (y/n): n
Goodbye!
```

## Input Validation Examples

| Input entered | What happens |
|---|---|
| `abc` | "⚠️ 'abc' is not a valid number. Please enter numbers only (e.g. 65.5)." — re-prompts |
| `-70` | "⚠️ Value must be greater than zero. Please try again." — re-prompts |
| `0` | Same as above — re-prompts |
| `exit` or `quit` | Program exits immediately |

## Next Steps (Advanced Tier Ideas)

Want to extend this into the advanced build? Consider adding:
- **A GUI** using `tkinter` or `PyQt5` instead of command-line prompts
- **Data persistence** — save each entry (date, weight, height, BMI) to a
  `sqlite3` database or CSV file
- **Trend visualization** — plot BMI history over time using `matplotlib`
- **Unit toggle** — support pounds/inches in addition to kg/metres
- **Multiple user profiles** — track BMI history separately per person

Each of these builds naturally on the existing `calculate_bmi()` and
`classify_bmi()` functions in `bmi_calculator.py`.
