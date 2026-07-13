graph={'A':['B','D'],'B':['C','F'],'C':['E','G','H'],'G':['E','H'],'E':['B','F'],'F':['A'],'D':['F'],'H':
       ['A']}
print("Given graph is ")
print(graph)
def dfs_traversal(input_graph,source):
    stack=list()
    visited_list=list()
    stack.append(source)
    visited_list.append(source)
    while stack:
        vertex=stack.pop()
        print(vertex,end=" ")
        for v in input_graph[vertex]:
            if v not in visited_list:
                stack.append(v)
                visited_list.append(v)
print("DFS Traversal")
dfs_traversal(graph,'G')

