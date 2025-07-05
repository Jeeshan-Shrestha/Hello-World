questions = [
    {
        "question": "1. What is the correct way to create a variable in Python?\n",
        "options": ["A. int x = 5", "B. x = 5", "C. let x = 5", "D. var x = 5"]
    },
    {
        "question": "2. Which of these is a valid Python list?\n",
        "options": ["A. (1, 2, 3)", "B. {1, 2, 3}", "C. [1, 2, 3]", "D. <1, 2, 3>"]
    },
    {
        "question": "3. What does '==' do in Python?\n",
        "options": ["A. Assigns value", "B. Checks equality", "C. Adds numbers", "D. None of the above"]
    },
    {
        "question": "4. How do you define a function in Python?\n",
        "options": ["A. function myFunc():", "B. def myFunc():", "C. func myFunc():", "D. define myFunc():"]
    },
    {
        "question": "5. Which loop is used to iterate over a sequence?\n",
        "options": ["A. repeat", "B. for", "C. loop", "D. foreach"]
    },
    {
        "question": "6. What is the output of: print(2 ** 3)?\n",
        "options": ["A. 6", "B. 8", "C. 9", "D. 23"]
    },
    {
        "question": "7. What is the correct way to write an if statement?\n",
        "options": ["A. if x > 5 then:", "B. if (x > 5) {}", "C. if x > 5:", "D. if x > 5 then"]
    },
    {
        "question": "8. What data type is the result of: type(3.14)?\n",
        "options": ["A. int", "B. float", "C. double", "D. decimal"]
    },
    {
        "question": "9. Which of the following is immutable?\n",
        "options": ["A. list", "B. dictionary", "C. set", "D. tuple"]
    },
    {
        "question": "10. How do you import a module in Python?\n",
        "options": ["A. #include <math>", "B. import math", "C. using math", "D. load math"]
    }
] #  List of dictionary

answers = ['B', 'C', 'B', 'B', 'B', 'B', 'C', 'B', 'D', 'B']
userAnswers = ''
score = 0
i = 0 #iterator
for question in questions:
    print(question["question"])
    for options in question["options"]:
        print(options)
    userAnswers = input("Enter the option")
    if (userAnswers.upper() == answers[i]):
        score+=1
        print("Correct")
    else:
        print("Incorrect")
    i+=1


print(score)