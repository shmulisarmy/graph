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

    def expand(self, vertexName, connectionTypes):
        if vertexName not in self.vertexes:
            raise Exception("Vertex not found")
        
        if not connectionTypes:
            return [vertexName]
        
        if not isinstance(connectionTypes, list):
            connectionTypes = [connectionTypes]

        vertexes = []
        using_vertexes = [vertexName]
        next_using_vertexes = []

        try:
            for connectionType in connectionTypes:
                if connectionType not in self.connectionTypes:
                    raise Exception(f"Connection type '{connectionType}' not found")
                for vertex in using_vertexes:
                    next_using_vertexes.extend(self.vertexes[vertex][connectionType])

                using_vertexes = next_using_vertexes
                next_using_vertexes = []
        except Exception as e:
            print(e, "however we'll return all everything up until this point")

        vertexes.extend(using_vertexes)
        return vertexes
    


    

