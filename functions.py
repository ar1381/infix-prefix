import tkinter as tk
def isInfix(inp):
    if (inp[0] == '(' or not isOperator(inp[0])) and (inp[-1] == ')' or not isOperator(inp[-1])):
        return True
    else:
        return False

def isPrefix(inp):
    if isOperator(inp[0]):
        return True
    else:
        return False

def isPostfix(inp):
    if isOperator(inp[-1]):
        return True
    else:
        return False

def isOperator(ch):
    if ch in {'+', '-', ' /' , '*', '^' , "%"}:
        return True
    else:
        return False
OpLevel = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}
def infixToPrefix(inp):
    output = ""
    stack = []
    inp = inp[::-1]

    for ch in inp:
        if ch not in ['+', '-', '*', '/', '(', ')', '^']:
            output += ch
        elif ch == ')':
            stack.append(ch)
        elif ch == '(':
            while stack and stack[-1] != ')':
                output += stack.pop()
            stack.pop()
        else:
            if stack and ch == stack[-1] and ch == '^':
                output += stack.pop()

            while stack and stack[-1] != ')' and OpLevel[ch] < OpLevel[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output[::-1]
def prefixToInfix(inp):
    a = ""
    b = ""
    stack = []

    inp = inp[::-1]

    for ch in inp:
        if ch not in ['+', '-', '*', '/', '(', ')', '^']:
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            b += ch
            stack.append(")" + b+a + "(")
            a = ""
            b = ""

    return stack[0][::-1]
def postfixToPrefix(inp):
    a = ""
    b = ""
    stack = []

    for ch in inp:
        if ch not in ['+', '-', '*', '/', '(', ')', '^']:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            a = ch+a
            stack.append(a+b)
            a = ""
            b = ""

    return stack[0]
def prefixToPostfix(expr):
    stack = [] 
    for char in expr: 
        if (char.isalpha()): 
            stack.append(char) 
        else: 
            op1 = stack.pop() 
            op2 = stack.pop() 
            stack.append(op1 + op2 + char) 
    return ''.join(stack)
def infixToPostfix(expression):
    stack = []
    output = ""

    for character in expression:
        if character not in ['+', '-', '*', '/', '(', ')', '^']:
            output += character
        elif character == '(':
            stack.append(character)
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and OpLevel[character] <= OpLevel[stack[-1]]:
                output += stack.pop()
            stack.append(character)
    while stack:
        output += stack.pop()

    return output
def postfixToInfix(inp):
    a = ""
    b = ""
    stack = []

    for ch in inp:
        if ch not in {'+', '-', '*', '/', '(', ')', '^'}:
            stack.append(ch)
        else:
            b += stack.pop()
            a += stack.pop()
            a += ch
            stack.append("(" + a+b + ")")
            a = ""
            b = ""

    return stack[0]
# def draw_expression_tree(postfix_expression):
#     window = tk.Tk()
#     expTree = tk.Canvas(window, width=400, height=400)
#     expTree.pack()
#     x = 200
#     y = 20


#     for i in range(len(postfix_expression)):
#         if postfix_expression[i] == "+":
#             # Draw the "+" sign
#             expTree.create_text(x, y, text="+", font=("Arial", 20))

#             leftX = x - 60
#             leftY = y + 50
#             rightX = x + 60
#             rightY = y + 50

#             expTree.createline(x, y, leftX, leftY) 
#             expTree.createline(x, y, rightX, rightY)
#             x = leftX 
#             y = leftY
#             # drawexpressiontree(postOrderTraversal[:i]) 
#             # drawexpressiontree(postOrderTraversal[i+1:])
