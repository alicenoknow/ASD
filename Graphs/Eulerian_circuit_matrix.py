'''
undirected graph
go through edges until cycle found, add passed vertices to stack and remove passed edges
add visited vertex to eulerian circuit (visited - does not have any edges)
when cycle found, pop last vertex from stack if it has any edges start finding new cycle else pop next vertex
'''


def has_edges(G, v):
    for i in range(len(G[v])):
        if G[v][i] == 1:
            return True
    return False


def DFS_visit(G, s, u, stack, circuit):
    for n in range(len(G[u])):
        if G[u][n] == 1:
            '''removing edge'''
            G[u][n] = 0
            G[n][u] = 0
            if n != s:
                stack.append(n)
                DFS_visit(G, s, n, stack, circuit)
    circuit.append(u)

def exists(G):
    for i in range(len(G)):
        sum = 0
        for j in range(len(G[i])):
            sum += G[i][j]
        if j%2 == 1:
            return False
    return True

# s - starting vertex
def Eulerian_circuit(G,s):
    if not exists(G):
        print("No eulerian circuit!")
        return

    circuit = [s]
    stack = [s]
    while stack:
        u = stack.pop()
        if has_edges(G, u):
            DFS_visit(G, u, u, stack, circuit)
    return circuit


G = [[0, 1, 1, 0, 0],
     [1, 0, 1, 1, 1],
     [1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [0, 1, 0, 1, 0]]
print(Eulerian_circuit(G, 0))