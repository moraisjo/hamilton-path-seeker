# main.py

def hamiltonian_path(graph, path, visited):
    if len(path) == len(graph):
        return True

    last_vertex = path[-1]

    for neighbor in graph[last_vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)

            if hamiltonian_path(graph, path, visited):
                return True

            # Backtrack
            path.pop()
            visited.remove(neighbor)

    return False

def find_hamiltonian_path(graph):
    for start_vertex in graph:
        path = [start_vertex]
        visited = {start_vertex}

        if hamiltonian_path(graph, path, visited):
            return path

    return None

if __name__ == "__main__":
    # Exemplo de grafo não orientado representado como dicionário
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    path = find_hamiltonian_path(graph)

    if path:
        print("Caminho Hamiltoniano encontrado:", path)
    else:
        print("Não existe Caminho Hamiltoniano neste grafo.")
