Question 1:

====  Write the test first,  then modify the code  ====
The first commit of question-1: the output of first test
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question1/first_test/results/results-first.png)

 There are some fails based on my code, and my code was:

                    def fizzBuzz(num):
                        if(num%3 == 0):
                            return "Fizz" 

                        if(num%5 == 0):
                            return "Buzz"

                        if(num%15 == 0):
                            return "FizzBuzz"
                    def main():
                            for num in range (1,100):
                                temp = fizzBuzz(num)
                                print(temp)

                    if __name__ == "__main__":
                        main()
                        
Seems the skeleton looks nothing wrong, but the logic of the code is wrong when we take a closer look,
The logic problem is, when we input "num" into this function, the order is:
      1) if(num%3 == 0):
      2) if(num%5 == 0):
      3) if(num%15 == 0):
The problem is, when we pass in the multiple of 15, it will satisfy both 1), 2) and 3) but we expect
only satisfy condition 3)

Then, based on the first-test, modify our code!!
after modification:

         def fizzBuzz(num):
             if(num%15 == 0):
                 return "FizzBuzz"
             elif(num%3 == 0):
                 return "Fizz" 
             elif(num%5 == 0):
                 return "Buzz"
             else: 
                 return "not multiple of 3, 5, 15"     

output of same test file but run with modified code:
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question1/second_test/results/results-second-test.png)
