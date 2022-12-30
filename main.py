from tkinter.tix import Tree
from functions import *
from tree import *
import pydot
import uuid
userInput = input("put your expression : ")
graph = pydot.Dot(graph_type='digraph', strict=True)
if isInfix(userInput):
    print("your input is in Infix format\n")
    print("prefix form is : " + str(infixToPrefix(userInput)))
    print("postfix form is : " + str(infixToPostfix(userInput))+"\n")
    root = postfix_draw(infixToPostfix(userInput))
    X = pydot.Node(name = uuid.uuid1().int, label = str(root), style='filled',fillcolor = 'green')
    drawTree(root, graph, True,X)
    graph.write_png(str(uuid.uuid1())+'.png')
elif isPostfix(userInput):
    print("your input is in Postfix format\n")
    print("infix form is : " + str(postfixToInfix(userInput)))
    print("prefix form is : " + str(postfixToPrefix(userInput))+"\n")
    root = postfix_draw(userInput)
    X = pydot.Node(name = uuid.uuid1().int, label = str(root), style='filled',fillcolor = 'green')
    drawTree(root, graph, True,X)
    graph.write_png(str(uuid.uuid1())+'.png')
elif isPrefix(userInput):
    print("your input is in Prefix format\n")
    print("infix form is : " + str(prefixToInfix(userInput)))
    print("postfix form is : " + str(prefixToPostfix(userInput))+"\n")
    root = postfix_draw(prefixToPostfix(userInput))
    X = pydot.Node(name = uuid.uuid1().int, label = str(root), style='filled',fillcolor = 'green')
    drawTree(root, graph, True,X)
    graph.write_png(str(uuid.uuid1())+'.png')
    