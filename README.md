
# Sistema de Defensa Planetaria

## Descripción
El Sistema de Defensa Planetaria es un programa diseñado para coordinar y gestionar recursos de defensa 
para proteger un planeta de amenazas espaciales. Utiliza estructuras de datos avanzadas como árboles, 
colas de prioridad y grafos para modelar estaciones de defensa, naves y rutas espaciales.

## Estructura del Proyecto
- **main.py**: Implementa las clases básicas (Estaciones, Naves) y estructuras como árboles binarios y generales.
- **advanced_features.py**: Contiene la implementación de colas de prioridad, grafos y los algoritmos DFS y BFS.

## Instalación y Uso
1. **Requisitos previos**: Python 3.8 o superior.
2. Instala las dependencias necesarias ejecutando:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta el programa principal con:
    ```bash
    python main.py
    ```

## Dependencias
El proyecto utiliza la biblioteca `heapq` para la cola de prioridad y módulos estándar de Python.

## Ejemplo de Uso
Ejecuta el programa para interactuar con las estructuras y simular escenarios de defensa planetaria.
"""

# Contenido del archivo main.py
main_content = """
class Estacion:
    def __init__(self, nombre, posicion, rango):
        self.nombre = nombre
        self.posicion = posicion  # Coordenadas (x, y)
        self.rango = rango

class Nave:
    def __init__(self, id_nave, velocidad, potencia):
        self.id_nave = id_nave
        self.velocidad = velocidad
        self.potencia = potencia

class NodoEstacion:
    def __init__(self, estacion):
        self.estacion = estacion
        self.izquierda = None
        self.derecha = None

class ArbolDefensa:
    def __init__(self):
        self.raiz = None

    def insertar(self, estacion):
        def _insertar(nodo, estacion):
            if not nodo:
                return NodoEstacion(estacion)
            if estacion.rango < nodo.estacion.rango:
                nodo.izquierda = _insertar(nodo.izquierda, estacion)
            else:
                nodo.derecha = _insertar(nodo.derecha, estacion)
            return nodo

        self.raiz = _insertar(self.raiz, estacion)

    def buscar_mayor_rango(self):
        nodo = self.raiz
        while nodo and nodo.derecha:
            nodo = nodo.derecha
        return nodo.estacion if nodo else None

class NodoNave:
    def __init__(self, nave):
        self.nave = nave
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)
"""

# Contenido del archivo advanced_features.py
advanced_features_content = """
import heapq

class ColaEmergencias:
    def __init__(self):
        self.cola = []

    def agregar(self, amenaza, peligro):
        heapq.heappush(self.cola, (-peligro, amenaza))

    def atender(self):
        return heapq.heappop(self.cola)[1]

class GrafoRutas:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = []

    def conectar_nodos(self, nodo1, nodo2, distancia):
        self.nodos[nodo1].append((nodo2, distancia))
        self.nodos[nodo2].append((nodo1, distancia))

def dfs(grafo, nodo_inicial, nodo_objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    if nodo_inicial == nodo_objetivo:
        return [nodo_inicial]
    visitados.add(nodo_inicial)
    for vecino, _ in grafo.nodos[nodo_inicial]:
        if vecino not in visitados:
            ruta = dfs(grafo, vecino, nodo_objetivo, visitados)
            if ruta:
                return [nodo_inicial] + ruta
    return None

from collections import deque

def bfs(grafo, nodo_inicial, nodo_objetivo):
    visitados = set()
    cola = deque([nodo_inicial])
    padre = {nodo_inicial: None}

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
"""


