import pydot
import uuid
#u should install pydot and graphviz
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
def postfix_draw(expression):
  stack = []

  for c in expression:
    if c in {'+', '-', ' /' , '*', '^' , "%"}:
      right = stack.pop()
      left = stack.pop()
      stack.append(Node(c, left, right))
    else:
      stack.append(Node(c))
  root = stack.pop()
  return root
def drawTree(root : Node, graph, bool, X : pydot.Node):
    if bool:
        graph.add_node(X)
    if not root.right == None:
        Id=uuid.uuid1().int
        a = pydot.Node(name = uuid.uuid1().int, label = str(root.right), style='filled',fillcolor = 'gold')
        graph.add_node(a)
        edge = pydot.Edge(X, a)
        graph.add_edge(edge)
        drawTree(root.right,graph,False,a)
    if not root.left == None:
        a = pydot.Node(name = uuid.uuid1().int, label = str(root.left), style='filled',fillcolor = 'cyan')
        # print(time.time())
        graph.add_node(a)
        edge = pydot.Edge(X, a)
        graph.add_edge(edge)
        drawTree(root.left,graph,False,a)