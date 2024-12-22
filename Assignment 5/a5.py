class Heap:
    def __init__(self):
        self.heap = []

    def HeapUp(self, i):
        if(i != 0):
            if(self.heap[i] > self.heap[(i-1)//2]):
                self.heap[i],self.heap[(i-1)//2] = self.heap[(i-1)//2],self.heap[i]
                self.HeapUp((i-1)//2)

    def HeapDown(self, i):
        large = i
        if((2*i+1<len(self.heap)) and (self.heap[large] < self.heap[2*i+1])): large = 2*i+1
        if((2*i+2<len(self.heap)) and (self.heap[large] < self.heap[2*i+2])): large = 2*i+2
        if(large != i):
            self.heap[i],self.heap[large] = self.heap[large],self.heap[i]
            self.HeapDown(large)

    def insert(self, data):
        self.heap.append(data)
        self.HeapUp(len(self.heap)-1)

    def deleteMax(self):
        data = self.heap[0]
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
        self.heap.pop()
        self.HeapDown(0)
        return data

def adjListMaker(links:list, adjlist:list):
    for each in links:
        adjlist[each[0]].append((each[2],each[1]))
        adjlist[each[1]].append((each[2],each[0]))

def findMaxCapacity(n:int, links:list, s:int, t:int):
    adjList = [[] for _ in range (0,n)]
    adjListMaker(links, adjList)
    costList = [None for _ in range(0,n)]
    visited = [False for _ in range(0,n)]
    pathList = Heap()
    for each in adjList[s]:
        pathList.insert(each)
        costList[each[1]] = (each[0],s)
    vertex = pathList.deleteMax()
    visited[s] = True
    while(vertex[1] != t):
        if(visited[vertex[1]]): 
            vertex = pathList.deleteMax()
            continue
        for each in adjList[vertex[1]]:
            if(visited[each[1]]): continue
            pathList.insert((min(vertex[0], each[0]), each[1]))
            if(costList[each[1]] != None):
                if(costList[each[1]][0] < min(vertex[0], each[0])):
                    costList[each[1]] = (min(vertex[0], each[0]), vertex[1])
            else: costList[each[1]] = (min(vertex[0], each[0]), vertex[1])
        visited[vertex[1]] = True
        vertex = pathList.deleteMax()
    path = [t]
    route = t
    while(route != s):
        route = costList[route][1]
        path.append(route)
    path.reverse()
    return (vertex[0], path)

# print(findMaxCapacity(7,[(0,1,10),(0,2,5),(1,3,20),(2,3,11),(3,4,100),(3,5,100),(4,6,100),(5,6,100)] ,0,6))
# print(findMaxCapacity(6,[(0,1,12),(0,4,7),(0,5,4),(1,2,8),(1,4,9),(2,3,5),(2,5,7),(3,4,6),(3,5,13)],0,3))