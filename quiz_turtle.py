import time
import turtle

wn = turtle.Screen()
tr = turtle.Turtle()
wn.setup(1000, 600)
wn.colormode(255)
wn.bgcolor(0, 0, 70)
wn.title("Python Quiz")


#BOX C
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-450, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("red")
for sides in range(3):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#BOX D
turtle.penup()
turtle.goto(25, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(3):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#BOX A
turtle.penup()
turtle.goto(-450, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(3):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#BOX B
turtle.penup()
turtle.goto(25, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(3):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#QB
turtle.penup()
turtle.goto(-480, 120)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(3):
    turtle.fd(625)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#SB
turtle.penup()
turtle.goto(225, 120)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(3):
    turtle.fd(225)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#Question
quest = turtle.Turtle()
quest.speed(0)
quest.hideturtle()
quest.penup()
quest.goto(-425, 150)
for sides in range(2):
    turtle.fd(625)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()

#Score
score1 = turtle.Turtle()
score1.speed(0)
score1.hideturtle()
score1.penup()
score1.goto(250, 125)
for sides in range(3):
    turtle.fd(225)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()
#Creatig Questions
quest = turtle.Turtle()
quest.speed(0)
quest.hideturtle()
quest.penup()
quest.goto(-425, 150)

#creating score
score1 = turtle.Turtle()
score1.speed(0)
score1.hideturtle()
score1.penup()
score1.goto(250, 125)

#Creating Answers AAA
A = turtle.Turtle()
A.speed(0)
A.hideturtle()
A.penup()
A.goto(-425, -50)

#BBB
B = turtle.Turtle()
B.speed(0)
B.hideturtle()
B.penup()
B.goto(50, -50)

#CCC
C = turtle.Turtle()
C.speed(0)
C.hideturtle()
C.penup()
C.goto(-425, -225)

#DDD
D = turtle.Turtle()
D.speed(0)
D.hideturtle()
D.penup()
D.goto(50, -225)


#OPening
quest.write("Welcome to the Quiz", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

quest.write("Press a, b, c, d to answer", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

quest.write("GOOD LUCK!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()



#number of Correct Answer
correctNow = 0

score1.write("Score:()".format(correctNow),font=("Verdana", 30, "bold"))

#Varables
CurrentQ = 1

#Functions

def chooseAnswerA():
    global select
    select = 'A'
    evaluate()

def chooseAnswerB():
    global select
    select = 'B'
    evaluate()

def chooseAnswerC():
    global select
    select = 'C'
    evaluate()

def chooseAnswerD():
    global select
    select = 'D'
    evaluate()

def evaluate():
    global correctNow
    global CurrentQ
    #CurrentQ = 1
    global i
    if correct == select:
        quest.clear()
        quest.write("CORRECT!!!",font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        score1.clear()
        correctNow += 1
        score1.write("Score:{}".format(correctNow), font=("Verdana", 30, "bold"))
        quest.clear()

    else:
        quest.clear()
        quest.write("WRONG ! The Answer was {}".format(correct),font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        quest.clear()

   
    CurrentQ += 1
    clearBoard()
    GetQuestionNum()

def GetQuestionNum():
    if CurrentQ == 2:
        question2()
    elif CurrentQ == 3:
        question3()
    elif CurrentQ == 4:
        question4()
    elif CurrentQ == 5:
        question5()
    elif CurrentQ == 6:
        question6()
    elif CurrentQ == 7:
        question7()
    elif CurrentQ == 8:
        question8()
    elif CurrentQ == 9:
        question9()
    elif CurrentQ == 10:
        question10()
    else:
        exi()

def clearBoard():
    quest.clear()
    A.clear()
    B.clear()
    C.clear()
    D.clear()
    

def question1():
    quest.write("What is the output for −'python ' [-3]?",font=("Verdana", 12, "bold"))
    A.write("A. o",font=("Verdana", 12, "bold"))
    B.write("B. t",font=("Verdana", 12, "bold"))
    C.write("C. h",font=("Verdana", 12, "bold"))
    D.write("D. Negative index error",font=("Verdana", 12, "bold"))
    global correct
    correct = 'C'

def question2():
    quest.write("What is output of following code \n −x = 2 \n y = 10 \n x * = y * x + 1",font=("Verdana", 12, "bold"))
    A.write("A. 42",font=("Verdana", 12, "bold"))
    B.write("B. 41",font=("Verdana", 12, "bold"))
    C.write("C. 40",font=("Verdana", 12, "bold"))
    D.write("D. 39",font=("Verdana", 12, "bold"))
    global correct
    correct = 'A'
def question3():
    quest.write("When the given code is executed how many times ' 'you are \n learning python ' ' will be printed. \n a = 0 \n while a<10: \n print(''you are learning python'') \n pass",font=("Verdana", 12, "bold"))
    A.write("A. 9",font=("Verdana", 12, "bold"))
    B.write("B. 10",font=("Verdana", 12, "bold"))
    C.write("C. 11",font=("Verdana", 12, "bold"))
    D.write("D. Infinet",font=("Verdana", 12, "bold"))
    global correct
    correct = 'D'
def question4():
    quest.write(" Which among them is used to create an object?",font=("Verdana", 12, "bold"))
    A.write("A. A Class",font=("Verdana", 12, "bold"))
    B.write("B. A Method",font=("Verdana", 12, "bold"))
    C.write("C. A Function",font=("Verdana", 12, "bold"))
    D.write("D.  A Constructor",font=("Verdana", 12, "bold"))
    global correct
    correct = 'A'
def question5():
    quest.write("Which one is NOT a legal variable name?",font=("Verdana", 12, "bold"))
    A.write("A. my-var",font=("Verdana", 12, "bold"))
    B.write("B. Myvar",font=("Verdana", 12, "bold"))
    C.write("C. my_var",font=("Verdana", 12, "bold"))
    D.write("D. _myvar",font=("Verdana", 12, "bold"))
    global correct
    correct = 'A'
def question6():
    quest.write("What is a correct syntax to return the first character in a string?",font=("Verdana", 12, "bold"))
    A.write("A. x = ""Hello""[0]",font=("Verdana", 12, "bold"))
    B.write("B. x = sub(""Hello"", 0, 1)",font=("Verdana", 12, "bold"))
    C.write("C. x = ""Hello"".sub(0, 1)",font=("Verdana", 12, "bold"))
    D.write("D. x = ""Hello""(0)",font=("Verdana", 12, "bold"))
    global correct
    correct = 'A'
def question7():
    quest.write("Which method can be used to remove any whitespace from both \n the beginning and the end of a string?",font=("Verdana", 12, "bold"))
    A.write("A. trim()",font=("Verdana", 12, "bold"))
    B.write("B. ptrim()",font=("Verdana", 12, "bold"))
    C.write("C. strip()",font=("Verdana", 12, "bold"))
    D.write("D. len()",font=("Verdana", 12, "bold"))
    global correct
    correct = 'C'
def question8():
    quest.write("Which of these collections defines a LIST?",font=("Verdana", 12, "bold"))
    A.write("A. (""apple"", ""banana"", ""cherry"")",font=("Verdana", 12, "bold"))
    B.write("B. [""apple"", ""banana"", ""cherry""]",font=("Verdana", 12, "bold"))
    C.write("C. {""apple"", ""banana"", ""cherry""}",font=("Verdana", 12, "bold"))
    D.write("D. {""name"": ""apple"", ""color"": ""green""}",font=("Verdana", 12, "bold"))
    global correct
    correct = 'B'
def question9():
    quest.write("Which collection is ordered, changeable, \n and allows duplicate members?",font=("Verdana", 12, "bold"))
    A.write("A. SET",font=("Verdana", 12, "bold"))
    B.write("B. DICTIONARY",font=("Verdana", 12, "bold"))
    C.write("C. TUPLE",font=("Verdana", 12, "bold"))
    D.write("D. LIST ",font=("Verdana", 12, "bold"))
    global correct
    correct = 'D'
def question10():
    quest.write("How do you start writing a while loop in Python?",font=("Verdana", 12, "bold"))
    A.write("A. while(x > y){",font=("Verdana", 12, "bold"))
    B.write("B. while(x > y){",font=("Verdana", 12, "bold"))
    C.write("C. while x > y:",font=("Verdana", 12, "bold"))
    D.write("D. x > y while {",font=("Verdana", 12, "bold"))
    global correct
    correct = 'C'
def exi():
    quest.write("End of Quiz!! You score is {}/10 \n Click Any Where On the Screen to exit".format(correctNow), font=("Verdana", 12, "bold"))
    turtle.exitonclick()


#Key Bindings
wn.listen()
wn.onkeypress(chooseAnswerA, "a")
wn.onkeypress(chooseAnswerB, "b")
wn.onkeypress(chooseAnswerC, "c")
wn.onkeypress(chooseAnswerD, "d")
question1()





