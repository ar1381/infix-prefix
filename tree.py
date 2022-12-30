import pydot
import uuid
#u should install pydot and graphviz

# graph = pydot.Dot(graph_type='graph', strict=True)
# x= pydot.Node(name = 'a',label = "1", style='filled',fillcolor='green')
# graph.add_node(x)
# x= pydot.Node(name = 'b',label = "1", style='filled',fillcolor='green')
# graph.add_node(x)
# x= pydot.Node('d', style='filled',fillcolor='green')
# graph.add_node(x)
# x= pydot.Node('d', style='filled',fillcolor='green')
# graph.add_node(x)
# x= pydot.Node('e', style='filled',fillcolor='green')
# graph.add_node(x)
# edge = pydot.Edge('a','b')
# graph.add_edge(edge)
# edge = pydot.Edge('a','c')
# graph.add_edge(edge)
# edge = pydot.Edge('c','e')
# graph.add_edge(edge)
# graph.write_png('10.png')
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