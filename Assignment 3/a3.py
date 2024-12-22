class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class PointDatabase:

    def __init__(self, pointlist):
        self.len = len(pointlist)
        if(self.len == 0): return
        self.xsorted = sorted(pointlist)
        self.ysort = [[] for i in range(len(pointlist))]
        self.xsort = self.createxsort(0, self.len-1)
        self.createysort(self.xsort)

    def createxsort(self, low, high):
        ptr = Node((low+high)//2)
        if(low == high):
            if(low == self.len-1): return ptr
            else: return None
        ptr.left = self.createxsort(low, (low+high)//2)
        ptr.right = self.createxsort((low+high)//2 + 1, high)
        return ptr

    def createysort(self, ptr):
        if(ptr == None): return []
        mo = self.createysort(ptr.left)
        m = []
        n = self.createysort(ptr.right)
        i=0;m=[]
        if(len(mo) == 0): m.append(self.xsorted[ptr.data])
        else:
            while(i<len(mo) and mo[i][1] < self.xsorted[ptr.data][1]):
                m.append(mo[i]) 
                i+=1
            m.append(self.xsorted[ptr.data])
            while(i<len(mo)):
                m.append(mo[i]) 
                i+=1
        c1 = c2 = i = 0
        C = [0 for m in range (len(m) + len(n))]
        while(i < len(m) + len(n)):
            if(c1 < len(m) and c2 < len(n)):
                if(m[c1][1] <= n[c2][1]):
                    C[i] = m[c1]
                    c1 += 1
                else:
                    C[i] = n[c2]
                    c2 += 1
            elif(c1 == len(m) and c2 != len(n)):
                C[i] = n[c2]
                c2 += 1
            elif(c2 == len(n) and c1 != len(m)):
                C[i] = m[c1]
                c1 += 1
            i += 1
        self.ysort[ptr.data] = C
        return C

    def findYPoints(self, ind, q, d, queryans):
        low=0; high=len(self.ysort[ind])
        while(low != high):
            median = (low+high)//2
            if(self.ysort[ind][median][1] >= q[1]-d): high=median
            elif(self.ysort[ind][median][1] < q[1]-d): low=median+1
        lowi = low
        low=0; high=len(self.ysort[ind])
        while(low != high):
            median = (low+high)//2
            if(self.ysort[ind][median][1] > q[1]+d): high=median
            elif(self.ysort[ind][median][1] <= q[1]+d): low=median+1
        highi = high
        for i in range(lowi, highi):
            # if(abs(self.ysort[ind][i][1]-q[1])<d): queryans.append(self.ysort[ind][i])
            queryans.append(self.ysort[ind][i])

    def leftChild(self, ptr, q, d, queryans):
        if(ptr == None): return
        if(abs(self.xsorted[ptr.data][0]-q[0]) <= d):
            self.leftChild(ptr.left, q, d, queryans)
            if(abs(self.xsorted[ptr.data][1]-q[1]) <= d): queryans.append(self.xsorted[ptr.data])
            if(ptr.right): self.findYPoints(ptr.right.data, q, d, queryans)
        else:
            self.leftChild(ptr.right, q, d, queryans)

    def rightChild(self, ptr, q, d, queryans):
        if(ptr == None): return
        if(abs(self.xsorted[ptr.data][0]-q[0]) <= d):
            self.rightChild(ptr.right, q, d, queryans)
            if(abs(self.xsorted[ptr.data][1]-q[1]) <= d): queryans.append(self.xsorted[ptr.data])
            if(ptr.left): self.findYPoints(ptr.left.data, q, d, queryans)
        else:
            self.rightChild(ptr.left, q, d, queryans)
    
    def searchNearby(self, q, d):
        if(self.len == 0): return []
        ptr = self.xsort
        queryans = []
        while(ptr):
            if(abs(self.xsorted[ptr.data][0]-q[0]) <= d):
                if(abs(self.xsorted[ptr.data][1]-q[1]) <= d): queryans.append(self.xsorted[ptr.data])
                self.leftChild(ptr.left, q, d, queryans)
                self.rightChild(ptr.right, q, d, queryans)
                break
            elif(self.xsorted[ptr.data][0]>q[0]+d): ptr=ptr.left
            elif(self.xsorted[ptr.data][0]<q[0]-d): ptr=ptr.right
        return queryans