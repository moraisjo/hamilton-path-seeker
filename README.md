# 🧩 Hamilton Path Seeker

### 📘 Sobre o Projeto
O **Hamilton Path Seeker** é um programa em **Python** que implementa o **algoritmo para encontrar um Caminho Hamiltoniano** em um grafo **não orientado**, utilizando a técnica de **backtracking**.

Um **Caminho Hamiltoniano** é um percurso que **visita cada vértice do grafo exatamente uma vez**.  
Esse é um problema clássico da **teoria dos grafos**, relacionado ao famoso **Problema do Caixeiro Viajante (TSP)**.

---

### 🎯 Objetivo
Implementar uma solução simples e didática para **verificar se um Caminho Hamiltoniano existe** em um grafo e, em caso afirmativo, **exibir o caminho encontrado**.

#### Descrição rápida do algoritmo
O programa percorre cada vértice como possível ponto de partida, inicializando a lista `path` e o conjunto `visited` com esse vértice. A função recursiva `hamiltonian_path` tenta estender o caminho visitando vizinhos ainda não explorados: adiciona o vértice ao caminho, marca como visitado e continua a busca. Quando o comprimento de `path` atinge o número total de vértices, um caminho hamiltoniano é encontrado. Caso uma ramificação não leve à solução, o algoritmo desfaz a última escolha (backtracking) e testa a próxima alternativa. Se nenhuma tentativa completar o caminho, `find_hamiltonian_path` retorna `None`, informando que o grafo não possui caminho hamiltoniano.

##### Explicação linha a linha (`main.py`)
- `def hamiltonian_path(graph, path, visited):` declara a função recursiva responsável por construir o caminho.
- `if len(path) == len(graph): return True` conclui a busca com sucesso quando todos os vértices foram incluídos.
- `last_vertex = path[-1]` obtém o vértice mais recente para inspecionar seus vizinhos.
- `for neighbor in graph[last_vertex]:` percorre cada vizinho diretamente conectado.
- `if neighbor not in visited:` evita visitar o mesmo vértice mais de uma vez.
- `visited.add(neighbor)` e `path.append(neighbor)` registram a nova escolha antes da chamada recursiva.
- `if hamiltonian_path(...): return True` propaga o sucesso quando uma ramificação completa o caminho.
- `path.pop()` e `visited.remove(neighbor)` desfazem a escolha durante o backtracking.
- `return False` indica que nenhum vizinho levou a uma solução partindo desse prefixo.
- `def find_hamiltonian_path(graph):` declara a função que tenta cada vértice como ponto de partida.
- `for start_vertex in graph:` itera sobre todas as possíveis origens do caminho.
- `path = [start_vertex]` e `visited = {start_vertex}` inicializam as estruturas para a tentativa atual.
- `if hamiltonian_path(...): return path` retorna imediatamente o caminho válido encontrado.
- `return None` sinaliza que não há caminho hamiltoniano no grafo.
- Bloco `if __name__ == "__main__":` garante a execução do exemplo apenas quando o script é chamado diretamente.
- `graph = {...}` define o grafo de exemplo utilizado para o teste.
- `path = find_hamiltonian_path(graph)` busca o caminho hamiltoniano no grafo definido.
- `if path:` escolhe entre imprimir o caminho encontrado ou relatar a ausência dele.

### Relatório técnico
#### Análise da complexidade computacional
- **Classes de Complexidade**
  - `P`: problemas de decisão resolvidos em tempo polinomial (ex.: ordenação, busca em BFS).
  - `NP`: problemas cuja solução candidata pode ser verificada em tempo polinomial; inclui todos de `P`.
  - `NP-completo`: problemas em `NP` para os quais qualquer outro problema em `NP` reduz em tempo polinomial; são os “mais difíceis” de `NP`.
  - `NP-difícil`: problemas pelo menos tão difíceis quanto os `NP-completos`; não precisam pertencer a `NP` (podem nem ser de decisão).
- **Caminho Hamiltoniano**
  - Versão de decisão (“existe caminho que visita todos os vértices uma única vez?”) está em `NP`, porque verificar um caminho fornecido é checar cada aresta, algo polinomial.
  - Também é `NP-completo`. Há reduções clássicas (por exemplo, de Hamiltonian Cycle ou de problemas SAT) que mostram que resolver Caminho Hamiltoniano permitiria resolver qualquer outro problema em `NP` com overhead polinomial.
  - A versão de busca (encontrar o caminho explicitamente) é `NP-difícil`, pois resolveria a versão de decisão como subcaso.
  - Resumo: Caminho Hamiltoniano (decisão) ∈ `NP` e é `NP-completo`; a forma de busca é `NP-difícil`.

**Justificativa**: 
Em `NP`, basta conferir rapidamente cada aresta do caminho sugerido, característica típica de problemas onde a verificação é polinomial. O TSP em versão de decisão (“existe um tour com custo ≤ K?”) é `NP-completo`. Quando atribuímos peso 1 a cada aresta do TSP, transformamos a pergunta em “existe um ciclo que visita cada cidade uma vez?”, que é o Problema do Ciclo Hamiltoniano; desse ciclo obtemos diretamente o Caminho Hamiltoniano. Assim, como o TSP reduz-se ao problema hamiltoniano, este herda a dificuldade `NP-completa`. Já encontrar o caminho explicitamente é `NP-difícil`, pois entregar o caminho resolve de imediato a decisão – exatamente como entregar o tour resolve o TSP.

#### Análise da complexidade assintótica de tempo
- **Complexidade temporal**: `O(n!)` no pior caso, onde `n` é o número de vértices.
- **Método utilizado**: contagem de operações baseada nas permutações possíveis. A cada passo, o backtracking escolhe um vértice ainda não visitado e aprofunda a busca, formando uma árvore que, em grafos densos, pode explorar quase todas as `n!` ordens de visita. Esse raciocínio corresponde a estimar o custo pelo número de sequências distintas que o algoritmo potencialmente percorre.
- **Aplicação do Teorema Mestre**: não se aplica, pois a recorrência do backtracking não assume a forma `T(n) = a·T(n/b) + f(n)`. A cada chamada exploramos subproblemas com tamanhos irregulares definidos pelos vizinhos disponíveis, sem divisão equilibrada nem fator fixo de redução sobre `n`, inviabilizando o uso direto do teorema.

#### Análise dos casos de complexidade
- **Pior caso**: ocorre quando o grafo não possui caminho hamiltoniano (ou o caminho só aparece na última tentativa), obrigando o algoritmo a explorar praticamente todas as permutações de vértices; complexidade aproximada `O(n!)`.
- **Caso médio**: depende da estrutura do grafo. Para grafos moderadamente conectados, muitas ramificações ainda são exploradas antes de encontrar (ou descartar) um caminho, resultando em tempo exponencial (`≈ O(k^n)`, com `k` próximo ao grau médio). Mesmo assim, tende a ser menor que o pior caso fatorial.
- **Melhor caso**: acontece quando o primeiro ponto de partida já gera um caminho válido sem retrocessos significativos; nesse cenário, a busca visita cada vértice uma única vez e executa trabalho quase linear (`O(n)` ou, considerando arestas inspecionadas, `O(n + m)`).

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
