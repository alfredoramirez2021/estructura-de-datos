advanced_features_content = """ import heapq

class ColaEmergencias: def init(self): self.cola = []

def agregar(self, amenaza, peligro):
    heapq.heappush(self.cola, (-peligro, amenaza))

def atender(self):
    return heapq.heappop(self.cola)[1]
class GrafoRutas: def init(self): self.nodos = {}

def agregar_nodo(self, nodo):
    if nodo not in self.nodos:
        self.nodos[nodo] = []

def conectar_nodos(self, nodo1, nodo2, distancia):
    self.nodos[nodo1].append((nodo2, distancia))
    self.nodos[nodo2].append((nodo1, distancia))
def dfs(grafo, nodo_inicial, nodo_objetivo, visitados=None): if visitados is None: visitados = set() if nodo_inicial == nodo_objetivo: return [nodo_inicial] visitados.add(nodo_inicial) for vecino, _ in grafo.nodos[nodo_inicial]: if vecino not in visitados: ruta = dfs(grafo, vecino, nodo_objetivo, visitados) if ruta: return [nodo_inicial] + ruta return None

from collections import deque

def bfs(grafo, nodo_inicial, nodo_objetivo): visitados = set() cola = deque([nodo_inicial]) padre = {nodo_inicial: None}

while cola:
    nodo = cola.popleft()
    if nodo == nodo_objetivo:
        ruta = []
        while nodo is not None:
            ruta.insert(0, nodo)
            nodo = padre[nodo]
        return ruta
    for vecino, _ in grafo.nodos[nodo]:
        if vecino not in visitados:
            visitados.add(vecino)
            padre[vecino] = nodo
            cola.append(vecino)
return None
