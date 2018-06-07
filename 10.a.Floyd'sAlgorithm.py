import numpy as np

if __name__ == '__main__':
    graph = np.array([[0,10,20,30,0,0],
                      [0,0,0,0,0,7],
                      [0,0,0,0,0,5],
                      [0,0,0,0,10,0],
                      [2,0,0,0,0,4],
                      [0,5,7,0,6,0]
                     ])
    v = len(graph)
    p = np.zeros(graph.shape)
    for i in range(0,v):
        for j in range(0,v):
            p[i,j] = i
            if (i != j and graph[i,j] == 0):
                p[i,j] = -30000
                graph[i,j] = 30000 # set zeros to any large number which is bigger then the longest way
    for k in range(0,v):
        for i in range(0,v):
            for j in range(0,v):
                if graph[i,j] > graph[i,k] + graph[k,j]:
                    graph[i,j] = graph[i,k] + graph[k,j]
                    p[i,j] = p[k,j]
    print(p)
