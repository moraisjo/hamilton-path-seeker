# 🧩 Hamilton Path Seeker

### 📘 Sobre o Projeto
O **Hamilton Path Seeker** é um programa em **Python** que implementa o **algoritmo para encontrar um Caminho Hamiltoniano** em um grafo **não orientado**, utilizando a técnica de **backtracking**.

Um **Caminho Hamiltoniano** é um percurso que **visita cada vértice do grafo exatamente uma vez**.  
Esse é um problema clássico da **teoria dos grafos**, relacionado ao famoso **Problema do Caixeiro Viajante (TSP)**.

---

### 🎯 Objetivo
Implementar uma solução simples e didática para **verificar se um Caminho Hamiltoniano existe** em um grafo e, em caso afirmativo, **exibir o caminho encontrado**.

#### Descrição rápida do algoritmo
Descrição rápida do algoritmo

hamiltonian_path(graph, path, visited)

Se o caminho atual já contém todos os vértices (len(path) == len(graph)), há sucesso.
Pega o último vértice do caminho e percorre seus vizinhos.
Para cada vizinho ainda não visitado: marca como visitado, adiciona ao caminho e chama a função recursivamente.
Se a chamada recursiva retornar sucesso, propaga True. Caso contrário, desfaz a escolha (backtracking) removendo o vértice do caminho e do conjunto visitado.
Se nenhum vizinho levar a uma solução, retorna False.
find_hamiltonian_path(graph)

Tenta iniciar o caminho em cada vértice do grafo.
Para cada vértice inicial, cria path e visited com esse vértice.
Chama hamiltonian_path. Se encontrar caminho, retorna a lista.
Se nenhum vértice inicial produzir resultado, retorna None.


Bloco if __name__ == "__main__":
Define um grafo não orientado como dicionário de adjacências.
Chama find_hamiltonian_path.
Se encontrar caminho, imprime a lista. Senão, avisa que não há caminho Hamiltoniano.

---

### 💻 Execução do Programa

#### **1. Clone o repositório**
```bash
git clone https://github.com/moraisjo/hamilton-path-seeker.git
cd hamilton-path-seeker
```

#### **2. Execute o programa**
```bash
python3 main.py
```

### Exemplo de grafo utilizado:
No arquivo main.py, o grafo é representado por um dicionário de listas, onde as chaves são os vértices e os valores são os vértices vizinhos:

```python
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
```

O grafo acima possui um caminho hamiltoniano possível, como: `0 → 1 → 3 → 2`

#### **3. Saída Esperada**
Ao executar o programa, a saída será:
```bash
Caminho Hamiltoniano encontrado: [0, 1, 3, 2]
```

ou, se não existir caminho:
```bash
Não existe Caminho Hamiltoniano neste grafo.
```

### 🔍 Detalhes Técnicos
- Linguagem: Python 3
- Método utilizado: Backtracking
- Tipo de grafo: Não orientado
- Complexidade: O(n!) no pior caso (problema NP-completo)