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
