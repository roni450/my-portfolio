def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        score = float(input("Enter your score (0-100): "))
        if score < 0 or score > 100:
            print("Please enter a valid score between 0 and 100.")
            return
        grade = calculate_grade(score)
        print(f"Your grade is: {grade}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
