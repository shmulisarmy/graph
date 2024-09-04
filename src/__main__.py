from src.graph import Grpah

g = Grpah()
g.addConnectionType("friend")
g.addConnectionType("coworker")

g.addVertex("Alice")
g.addVertex("Bob")
g.addVertex("Carol")

g.addConnection("Alice", "Bob", "friend")
g.addConnection("Alice", "Carol", "coworker")

g.display()

    