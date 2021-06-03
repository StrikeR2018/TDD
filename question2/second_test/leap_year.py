
def leap_year(year):
    if year < 0:
        return "Not a good value for year!"

    
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return "This is a leap year."
    else:
        return "This is not a leap year."

def main():
    leap_year()

if __name__ == "__main__":
    main()