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
    holder1 = ""
    holder2 = ""
    stack = []

    inp = inp[::-1]

    for chracter in inp:
        if chracter not in ['+', '-', '*', '/', '(', ')', '^']:
            stack.append(chracter)
        else:
            holder1 = stack.pop()
            holder2 = stack.pop()
            holder2 += chracter
            stack.append(")" + holder2+holder1 + "(")
            holder1 = ""
            holder2 = ""

    return stack[0][::-1]
def postfixToPrefix(inp):
    holder1 = ""
    holder2 = ""
    stack = []

    for character in inp:
        if character not in ['+', '-', '*', '/', '(', ')', '^']:
            stack.append(character)
        else:
            holder2 = stack.pop()
            holder1 = stack.pop()
            holder1 = character+holder1
            stack.append(holder1+holder2)
            holder1 = ""
            holder2 = ""

    return stack[0]
def prefixToPostfix(inp):
    holder1 = ""
    holder2 = ""
    stack = []

    inp = inp[::-1]

    for character in inp:
        if character not in ['+', '-', '*', '/', '(', ')', '^']:
            stack.append(character)
        else:
            holder1 = stack.pop()
            holder2 = stack.pop()
            holder2 = holder2+character
            stack.append(holder1+holder2)
            holder1 = ""
            holder2 = ""

    return stack[0]
def infixToPostfix(inp):
    stack = []
    output = ""

    for character in inp:
        if character not in ['+', '-', '*', '/', '(', ')', '^']:
            output += character
        elif character == '(':
            stack.append(character)
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
            while stack and stack[-1] != '(' and OpLevel[character] <= OpLevel[stack[-1]]:
                output += stack.pop()
            stack.append(character)

    while stack:
        output += stack.pop()

    return output
def postfixToInfix(inp):
    holder1 = ""
    holder2 = ""
    stack = []

    for character in inp:
        if character not in ['+', '-', '*', '/', '(', ')', '^']:
            stack.append(character)
        else:
            holder2 += stack.pop()
            holder1 += stack.pop()
            holder1 += character
            stack.append("(" + holder1+holder2 + ")")
            holder1 = ""
            holder2 = ""

    return stack[0]