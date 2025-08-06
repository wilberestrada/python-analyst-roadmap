try:
    
    name = input("Enter your name: ")   # str
    year = int(input("Birth year (YYYY): "))    # casting str to int
    current_year = 2025

    if(1900 <= year <= current_year):
        age_years = current_year - year
        age_years = age_years * 365

        print(f"Hi {name}! Your are about {age_years} days old.")
    
    else:
        print(f"Age must be between 1900 and {current_year}")

except ValueError:
    print("Please enter a valid number.")