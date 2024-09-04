from src.graph import Grpah


g = Grpah()
g.addConnectionType("friend")
g.addConnectionType("coworker")



people = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kathy", "Linda", "Mindy", "Nancy", "Oscar", "Penny", "Quincy", "Ruth", "Sarah", "Tom", "Ursula", "Victor", "Wendy", "Xavier", "Yvonne", "Zara", "Zoe"]

g.addVertex("Alice")
g.addVertex("Bob")
g.addVertex("Carol")
g.addVertex("David")

g.addConnection("Alice", "Bob", "friend")
g.addConnection("Alice", "Carol", "friend")


g.addConnection("Carol", "Frank", "coworker")
g.addConnection("Bob", "David", "coworker")



print(g.expand("Alice", ["friend", "coworker", "po"]))