#This code uses the page rank algorithm with damping factor consideration to find the page rank of sparesly connected pages.  Note: the sum of total page ranks is not normalized to 1

import random

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key, rank):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key, rank)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

class Vertex:
    def __init__(self,key, rank):
        self.ident = key,
	self.pagerank = rank
        self.connectedTo = {}

    def setRank(self, rank):
	self.pagerank = rank

    def getRank(self):
	return self.pagerank

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.ident) + ' connectedTo: ' + str([x.ident for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo

    def getID(self):
        return self.ident

def getRanks(n,graph):
	numpages = n
	ranks = graph
        connections = []
        tempRank = 0

        for i in range(numpages):
                temp = ranks.getVertex(i)
                connections = temp.getConnections()
                if connections is not None:
                        L = len(connections)
                        #compute page rank
                        for x in connections:
                                tempRank += x.getRank()/L
	                tempRank = (1-damping)/numpages + damping * tempRank
                        temp.setRank(tempRank)
                tempRank = 0
                numConnections = 0
                for j in range(len(temp.getConnections())):
                        numConnections += 1
                print i, temp.getRank(), numConnections

def initGraph(sign, n, graph):
	numpages = n
	#Normalize values such that the sum of all vertexs is equal to 1
	for i in range(numpages):
                #fills graph with page ranks (edge weights) and connects some vertices
                graph.addVertex(i, (sign)**i*random.random())
                temp = graph.getVertex(i)
                print i, temp.getRank()
                if i is 0:
                        root = temp
                        lastvert3 = root
                        lastvert2 = root
                if i % 3 == 0:
                        lastvert3.addNeighbor(temp)
                        lastvert3 = temp
                if i % 2 ==  0:
                        lastvert2.addNeighbor(temp)
                        lastvert2 = temp
	return graph

if __name__ == "__main__":
	negativeRanks = Graph()
	positiveRanks = Graph()
	damping = .85
	numpages = 10

	positiveRanks = initGraph(1,numpages, positiveRanks)	
	getRanks(numpages, positiveRanks)

#	negativeRanks = initGraph(-1,numpages, negativeRanks)
#	getRanks(numpages, negativeRanks)
