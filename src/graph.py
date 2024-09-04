class Grpah:
    def __init__(self):
        self.connectionTypes = []
        self.vertexes = {}


    def addConnectionType(self, name):
        self.connectionTypes.append(name)
        for vertex in self.vertexes:
            self.vertexes[vertex][name] = []

    def addVertex(self, name):
        self.vertexes[name] = {connection: [] for connection in self.connectionTypes}


    def addConnection(self, fromVertex, toVertex, connectionType):
        if connectionType not in self.connectionTypes:
            raise Exception("Connection type not found")
        self.vertexes[fromVertex][connectionType].append(toVertex)

    def display(self):
        for key, value in self.__dict__.items():
            print(key, value)

