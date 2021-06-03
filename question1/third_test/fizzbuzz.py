# program fizbuzz
# Deiscription: input multiple of 3, return Fizz
#               input multiple of 5, return Buzz
#               input multiple of 15, return FizzBuzz
# Goal: practise Test-Driven Development skills

def fizzBuzz(num):
    if(num%15 == 0):
        return "FizzBuzz"
    elif(num%3 == 0):
        return "Fizz" 
    elif(num%5 == 0):
        return "Buzz"
    else: 
        return "not multiple of 3, 5, 15"     
   
        
def main():
        for num in range (1,100):
            temp = fizzBuzz(num)
            print(temp)

if __name__ == "__main__":
    main()