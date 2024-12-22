def compareChild(heap, i , N):
    large=i
    if((2*i+1)<N and heap[2*i+1]<heap[large]): large=2*i+1
    if((2*i+2)<N and heap[2*i+2]<heap[large]): large=2*i+2
    return large

def HeapDown(heap, indices, i, N):
    large = compareChild(heap, i, N)
    if(large!=i):
        heap[large],heap[i] = heap[i],heap[large]
        indices[heap[i][1]],indices[heap[large][1]] = indices[heap[large][1]],indices[heap[i][1]]
        HeapDown(heap, indices, large, N)

def HeapUp(heap, indices, i, N):
    if(i!=0):
        small=i
        if(heap[small] < heap[(i-1)//2]): small = (i-1)//2
        if(small!=i):
            heap[small],heap[i] = heap[i],heap[small]
            indices[heap[i][1]],indices[heap[small][1]] = indices[heap[small][1]],indices[heap[i][1]]
            HeapUp(heap, indices, small, N)
    
def BuildHeap(heap, indices, N):
    for i in range(N//2-1, -1, -1):
        HeapDown(heap, indices, i, N)

def listCollisions(M=[],x=[],v=[],m=0,T=0):
    N = len(x)
    if(N==0 or m==0 or T==0): return []
    collisions,heap,indices = [],[],[]
    for i in range (0,N-1):
        coltime = 0
        if(v[i] == v[i+1]): coltime = T+1
        else: coltime = (x[i+1]-x[i])/(v[i]-v[i+1])
        if(coltime<0): coltime = T+1
        heap.append([coltime,i,x[i],v[i],M[i],0])
        indices.append(i)
    heap.append([T+1,N-1,x[N-1],v[N-1],M[N-1],0])
    indices.append(N-1)
    BuildHeap(heap, indices, N)
    t = 0
    while(m>0):
        if(heap[0][0]>T): break
        # large=compareChild(heap, 0, N)
        # if(large!=0):
        #     heap[large],heap[0] = heap[0],heap[large]
        #     indices[heap[0][1]],indices[heap[large][1]] = indices[heap[large][1]],indices[heap[0][1]]
        m-=1
        t = heap[0][0]
        in0 = heap[0][1]
        in1 = indices[in0+1]
        newx = heap[0][2]+heap[0][3]*(t-heap[0][5])
        v0new = ((heap[0][4]-heap[in1][4])/(heap[0][4]+heap[in1][4]))*heap[0][3] + ((2*heap[in1][4])/(heap[0][4]+heap[in1][4]))*heap[in1][3]
        v1new = ((2*heap[0][4])/(heap[0][4]+heap[in1][4]))*heap[0][3] - ((heap[0][4]-heap[in1][4])/(heap[0][4]+heap[in1][4]))*heap[in1][3]
        collisions.append((round(t,4),in0,round(newx,4)))
        if(in0 != 0):
            inb = indices[in0-1] 
            if(v0new != heap[inb][3]):
                newt1 = (newx - heap[inb][2] - heap[inb][3]*(t-heap[inb][5]))/(heap[inb][3]- v0new)
                if(newt1<0): 
                    heap[inb][0]=T+1
                    HeapDown(heap, indices, inb, N)
                else: 
                    heap[inb][0]=t+newt1
                    HeapUp(heap, indices, inb, N)
        heap[indices[in0+1]][0] = T+1
        heap[indices[in0+1]][3] = v1new
        heap[indices[in0+1]][2] = newx
        heap[indices[in0+1]][5] = t
        if(in0 != N-2):
            in1 = indices[in0+1]
            ina = indices[in0+2]
            if(v1new != heap[ina][3]):
                newt2 = (heap[ina][2] + heap[ina][3]*(t-heap[ina][5]) - newx)/(v1new - heap[ina][3])
                if(newt2<0): 
                    heap[in1][0]=T+1
                    HeapDown(heap, indices, in1, N)
                else: 
                    heap[in1][0]=t+newt2
                    HeapUp(heap, indices, in1, N)
        heap[indices[in0]][0] = T+1
        heap[indices[in0]][2] = newx
        heap[indices[in0]][3] = v0new
        heap[indices[in0]][5] = t
        HeapDown(heap, indices, indices[in0], N)
    return collisions