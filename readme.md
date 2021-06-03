TDD process (from lecture notes)<br/>
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/cb6bf48f57fb3aa0ff172565cb2930a.png)
<br/>
Recourse from class: [Test Driven Development.pdf](https://github.com/StrikeR2018/TDD/blob/main/Test%20Driven%20Development.pdf)
## Question 1:


* Write the test first,  then modify the code 
The file:
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/first-testfile.png)
* The first commit of question-1: the output of first test
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question1/first_test/results/results-first.png)

 * There are some fails based on my code, and my code was:

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
                        
* Seems the skeleton looks nothing wrong, but the logic of the code is wrong when we take a closer look,
The logic problem is, when we input "num" into this function, the order is:
     *  1) if(num%3 == 0):
     *  2) if(num%5 == 0):
    *   3) if(num%15 == 0):
* The problem is, when we pass in the multiple of 15, it will satisfy both 1), 2) and 3) but we expect
only satisfy condition 3)

* Then, based on the first-test, modify our code!!
* after modification:

         def fizzBuzz(num):
             if(num%15 == 0):
                 return "FizzBuzz"
             elif(num%3 == 0):
                 return "Fizz" 
             elif(num%5 == 0):
                 return "Buzz"
             else: 
                 return "not multiple of 3, 5, 15"     

* output of same test file but run with modified code:
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question1/second_test/results/results-second-test.png)

* Then write more test-cases to avoid any possible blind spot, output:
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question1/third_test/results/final-results.png)

## Question 2:
* Write test first:
* result based on first test and cdoe:
  ![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question2/first_test/results/b8112a3357e61486f1581b738a4cf52.png)
* Then modify code, results after modification:
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question2/second_test/results/ff5e693729d654acc980473823028a2.png)
* add more cases and result:
![Test Message](https://github.com/StrikeR2018/TDD/blob/main/question2/second_test/results/97c06a6aa96ea13d3f906178b31c77e.png)
