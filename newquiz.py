from os import system

_ = system('clear')

name =  input('What is your name? \n')

print('\n Hi '+ name + '! Get Ready For the quiz!\n')
print('You will be tested on 10 questions and for each question you get four choices.\n\nYou select which is the correct answer in numbers.\n')

input("Press Enter to Continue...")

score = 0
score = int(score) 

print('Question 1. How to pass argument to a script?\n')
print('1. ./script argument')
print('2. /.script argument')
print('3. :scrpit argument')
print('4. //script argument')

Q1answer = "1"
Q1response = input('Your answer: ')

if (Q1response != Q1answer):
    print('That is incorrect the correct option in 1!')
else:
    print('Well done!'+ Q1response +' is correct!')
    score = score + 1

print()
print()

print('Question 2. How to calculate number of passed arguments?\n')
print('1. $#\n 2. #$\n 3. $\n 4.$0')

Q2answer = "1"
Q2response = input('Your answer: ')

if (Q2response != Q2answer):
    print('That is incorrect the correct option is 1!')
else:
    print('Well done!'+ Q2response +' is  correct!')
    score = score + 1

print()
print()

print('Question 3. How to get script name inside a script?\n')
print('1. $name\n 2. $script name\n 3. $1\n 4. $0')
Q3answer = "4"
Q3response = input('Your answer: ')

if (Q3response != Q3answer):
    print('That is the incorrect option The correct option is 4!')
else:
    print('Well done!'+ Q3response +' is  correct!')
    score = score + 1

print()
print()

print('Question 4. How to check if previous command run successful?\n')
print('1. $!\n 2. $$\n 3. $?\n 4. $#')
Q4answer = "3"
Q4response = input('your answer: ')

if (Q4response != Q4answer):
    print('That is the incorrect option The correct option is 3!')
else:
    print("Wll done!"+ Q4response +' is correct')
    score = score + 1

print()
print()

print('Question 5. How to get last line from a file?\n')
print('1. end-l\n 2. line-end\n 3. tail-l\n 4. tail-1')
Q5answer = "4"
Q5response = input('your answer: ')

if (Q5response != Q5answer):
    print('That is the incorrect option The correct option is 4')
else:
    print('Well done'+ Q5response +' is  correct')
    score = score + 1

print()
print()

print('Question 6. How to debug bash script\n')
print('1. Add +xv to #!/bin/bash\n 2. Add -xv to #!/bin/bash\n 3. Add +vx to #!bin/bash\n 4. Add -xv to #!bin/bash')
Q6answer = "2"
Q6response = input('your answer: ')

if (Q6response != Q6answer):
    print('That is the incorrect option The correct option is 2')
else:
    print('Wll done you have choosen correct option')
    score = score + 1

print()
print()

print('Question 7. How to get 10th line from the text file?\n')
print('1. text-10file|text-1\n 2. head-10 file|tail-1\n 3. head-10file|head-l\n 4. tail-10file|tail-1')
Q7answer = "2"
Q7response = input('your aswer: ')

if (Q7response != Q7answer):
    print('That is the incorrects answer The correct option is 2')
else:
    print('correct option is choosen')
    score = score + 1

print()
print()

print('Question 8. What "chmod 500 script" do?\n')
print('1. Makes script 500 times larger\n 2. Makes 500 numbers in script\n 3.  makes script excuatable for script owner\n 4. Makes script to public')
Q8answer = "3"
Q8response = input('Your answer: ')

if (Q8response != Q8answer):
    print('incorrect option cjolsen The correct option is 3')
else:
    print('Correct option')
    score = score + 1

print()
print()


print('Question 9. Which command replaces string to uppercase?\n')
print('1. ch''[:lower:]''[:upper:]''\n 2. tr''[:lower:]''''[:upper:]''')
Q9answer = "2"
Q9response = input('Your answer: ')

if (Q9response != Q9answer):
    print('incorrect option chossen The correct option is 2')
else:
    print('correct')
    score = score + 1

print()
print()


print('Question 10. How to print PID of the current shell?\n')
print('1. echo$#\n 2. echo@$\n 3. echo $#\n 4. echo$$')
Q10answer = "3"
Q10response = input('Your answer: ')

if (Q10response != Q10answer):
    print('incorrect option The correct option is 3')
else:
    print('correct option choosen')
    score = score + 1



print("yout score is "+ str(score))



  

