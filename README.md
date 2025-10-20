# 🧩 Hamilton Path Seeker

### 📘 Sobre o Projeto
O **Hamilton Path Seeker** é um programa em **Python** que implementa o **algoritmo para encontrar um Caminho Hamiltoniano** em um grafo **não orientado**, utilizando a técnica de **backtracking**.

Um **Caminho Hamiltoniano** é um percurso que **visita cada vértice do grafo exatamente uma vez**.  
Esse é um problema clássico da **teoria dos grafos**, relacionado ao famoso **Problema do Caixeiro Viajante (TSP)**.

---

### 🎯 Objetivo
Implementar uma solução simples e didática para **verificar se um Caminho Hamiltoniano existe** em um grafo e, em caso afirmativo, **exibir o caminho encontrado**.

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