from functions import *
userInput = input("put your expression : ")

if isInfix(userInput):
    print("your input is in Infix format\n")
    print("prefix form is : " + str(infixToPrefix(userInput)))
    print("postfix form is : " + str(infixToPostfix(userInput))+"\n")
elif isPostfix(userInput):
    print("your input is in Postfix format\n")
    print("infix form is : " + str(postfixToInfix(userInput)))
    print("prefix form is : " + str(postfixToPrefix(userInput))+"\n")
elif isPrefix(userInput):
    print("your input is in Prefix format\n")
    print("infix form is : " + str(prefixToInfix(userInput)))
    print("postfix form is : " + str(prefixToPostfix(userInput))+"\n")
    