
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
main.py contiene las implementaciones de las clases básicas y estructuras que modelan las estaciones de defensa y las naves, además de un árbol binario de búsqueda utilizado para organizar las estaciones. Aquí te detallo su contenido:

1. Clases principales
Estacion
Representa una estación de defensa:

nombre: el nombre de la estación.
posicion: sus coordenadas (x, y) en el espacio.
rango: el rango de alcance de la estación.
Nave
Representa una nave espacial:

id_nave: el identificador único de la nave.
velocidad: la velocidad a la que puede desplazarse.
potencia: la potencia que puede generar o utilizar.

2. Árbol Binario de Defensa
NodoEstacion
Cada nodo del árbol contiene:

Una referencia a una estación (estacion).
Dos referencias a nodos hijos (izquierda y derecha).
ArbolDefensa
Un árbol binario que organiza las estaciones según su rango:

Método insertar: Permite agregar estaciones al árbol, ordenándolas por rango.
Método buscar_mayor_rango: Busca la estación con el mayor rango en el árbol (se encuentra en el extremo derecho).
3. Árbol General para Naves
NodoNave
Representa un nodo de un árbol general:

Contiene una nave (nave) y una lista de hijos (hijos).
Método agregar_hijo: Permite añadir otros nodos como hijos.
Este archivo define las bases para organizar y administrar las estaciones y naves. Las estaciones están estructuradas en un árbol binario para facilitar la búsqueda por rango, mientras que las naves están organizadas como nodos en un árbol general, que permite más flexibilidad para representar jerarquías o relaciones complejas.

# Contenido del archivo advanced_features.py
El archivo advanced_features.py incluye estructuras de datos y algoritmos más avanzados utilizados en el proyecto, como colas de prioridad, grafos y búsquedas (DFS y BFS)

1. Cola de Emergencias (Cola de Prioridad)
Clase ColaEmergencias
Implementa una cola de prioridad usando el módulo estándar heapq de Python.

Métodos:
agregar(amenaza, peligro): Agrega una amenaza a la cola con su nivel de peligro. El nivel de peligro tiene prioridad alta cuando su valor es mayor (se almacena como negativo para usar el comportamiento de min-heap).
atender(): Elimina y devuelve la amenaza con el nivel de peligro más alto.
3. Grafo de Rutas
Clase GrafoRutas
Representa un grafo no dirigido donde los nodos son estaciones o puntos clave y las aristas tienen una distancia asociada.

Métodos:
agregar_nodo(nodo): Añade un nodo al grafo si no existe.
conectar_nodos(nodo1, nodo2, distancia): Conecta dos nodos con una distancia específica.

4. Algoritmos de Búsqueda
DFS (Depth-First Search)
Función dfs(grafo, nodo_inicial, nodo_objetivo, visitados=None):
Realiza una búsqueda en profundidad para encontrar una ruta entre dos nodos.
Usa un conjunto visitados para evitar ciclos.
Devuelve una lista con la ruta encontrada o None si no hay conexión.
BFS (Breadth-First Search)
Función bfs(grafo, nodo_inicial, nodo_objetivo):
Realiza una búsqueda en anchura para encontrar la ruta más corta (en términos de número de nodos) entre dos nodos.
Utiliza:
Una cola (deque) para gestionar los nodos por explorar.
Un diccionario padre para reconstruir la ruta una vez encontrado el nodo objetivo.
Devuelve una lista con la ruta o None si no hay conexión.
Propósito del archivo
Cola de Emergencias: Gestionar amenazas espaciales priorizando aquellas más peligrosas.
Grafo de Rutas: Modelar las conexiones entre estaciones o naves, permitiendo encontrar caminos eficientemente.
DFS y BFS: Facilitar la navegación en el grafo, ya sea para explorar todas las rutas (DFS) o para encontrar la ruta más corta (BFS).

Conclusión Final
Síntesis del proyecto:
"El trabajo práctico Sistema de Defensa Planetaria logró integrar múltiples conceptos avanzados de programación para abordar un problema que simula escenarios reales de gestión y protección. A través de estructuras como árboles, colas de prioridad y grafos, se diseñó un sistema eficiente y escalable capaz de coordinar recursos de defensa de manera óptima."

Impacto de las estructuras de datos y algoritmos:
"Este proyecto destaca la importancia de elegir las estructuras de datos adecuadas para resolver problemas específicos. Por ejemplo, el árbol binario permitió organizar y buscar estaciones de defensa por rango de forma eficiente, mientras que el grafo fue esencial para modelar y explorar rutas espaciales."

Aprendizajes clave:

Optimización y eficiencia:
"Comprendimos cómo estructuras bien diseñadas pueden reducir significativamente la complejidad de búsqueda y gestión."
Resolución de problemas complejos:
"Aplicar algoritmos como BFS y DFS nos ayudó a resolver desafíos de navegación y priorización en contextos dinámicos."
Simulación práctica:
"Este tipo de proyecto refuerza cómo la teoría se traduce en soluciones reales aplicables a diversos campos, desde la defensa hasta la logística."
Relevancia en el mundo real:
"Aunque se trata de un trabajo practico, los conceptos empleados tienen aplicaciones prácticas en áreas como la planificación de rutas, la gestión de emergencias y la asignación de recursos en sistemas complejos."

Cierre:
"Finalmente, este trabajo no solo consolidó conocimientos técnicos, sino que también planteó nuevos desafíos que podrían explorarse en futuros proyectos,
Muchas gracias por su atención.





