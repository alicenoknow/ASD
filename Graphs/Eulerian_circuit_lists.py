'''
undirected graph
go through edges until cycle found, add passed vertices to stack and remove passed edges
add visited vertex to eulerian circuit (visited - does not have any edges)
when cycle found, pop last vertex from stack if it has any edges start finding new cycle else pop next vertex
'''


def has_edges(G, v):
    return len(G[v]) > 0

def exists(G):
    for i in range(len(G)):
        if len(G[i]) % 2 == 1:
            return False
    return True

def remove_edge(G, v, u):
    for i in range(len(G[v])):
        if G[v][i] == u:
            G[v].pop(i)
            break
    for i in range(len(G[u])):
        if G[u][i] == v:
            G[u].pop(i)
            break


def DFS_visit(G, s, u, stack, circuit):
    for n in G[u]:
        remove_edge(G, u, n)
        if n != s:
            stack.append(n)
            DFS_visit(G, s, n, stack, circuit)
    circuit.append(u)


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


G = [[1,2],
     [0,2,3,4],
     [0,1],
     [1,4],
     [1,3]]
print(Eulerian_circuit(G, 0))