"""Arbol AVL"""
#David Gerardo Diaz Gomez
#Javier Alejandro Sanchez Salamanca
from __future__ import print_function
"""Declaramos la clase "nodo", con cada una de sus propiedades."""


class Nodo:

  def __init__(self, label):
    self.label = label
    self._padre = None
    self._izquierda = None
    self._derecha = None
    self.altura = 0

  @property
  def derecha(self):
    return self._derecha

  @derecha.setter
  def derecha(self, nodo):
    if nodo is not None:
      nodo._padre = self
      self._derecha = nodo

  @property
  def izquierda(self):
    return self._izquierda

  @izquierda.setter
  def izquierda(self, nodo):
    if nodo is not None:
      nodo._padre = self
      self._izquierda = nodo

  @property
  def padre(self):
    return self._padre

  @padre.setter
  def padre(self, nodo):
    if nodo is not None:
      self._padre = nodo
      self.altura = self.padre.altura + 1
    else:
      self.altura = 0


# Clase AVL
class AVL:

  def __init__(self):
    self.root = None
    self.tamano = 0
    """
        Inserción de nodos en el arbolt.
        """

  def insertar(self, value):
    nodo = Nodo(value)

    if self.root is None:
      self.root = nodo
      self.root.altura = 0
      self.tamano = 1
    else:
      nodo_padre = None
      curr_nodo = self.root

      while True:
        if curr_nodo is not None:

          nodo_padre = curr_nodo

          if nodo.label < curr_nodo.label:
            curr_nodo = curr_nodo.izquierda
          else:
            curr_nodo = curr_nodo.derecha
        else:
          nodo.altura = nodo_padre.altura
          nodo_padre.altura += 1
          if nodo.label < nodo_padre.label:
            nodo_padre.izquierda = nodo
          else:
            nodo_padre.derecha = nodo
          self.rebalance(nodo)
          self.tamano += 1
          break

    # Operación de rotación
  def rebalance(self, nodo):
    n = nodo

    while n is not None:
      altura_derecha = n.altura
      altura_izquierda = n.altura

      if n.derecha is not None:
        altura_derecha = n.derecha.altura

      if n.izquierda is not None:
        altura_izquierda = n.izquierda.altura

      if abs(altura_izquierda - altura_derecha) > 1:
        if altura_izquierda > altura_derecha:
          izquierda_hijo = n.izquierda
          if izquierda_hijo is not None:
            h_derecha = (izquierda_hijo.derecha.altura if
                       (izquierda_hijo.derecha is not None) else 0)
            h_izquierda = (izquierda_hijo.izquierda.altura if
                      (izquierda_hijo.izquierda is not None) else 0)
          if (h_izquierda > h_derecha):
            self.rotacion_izquierda(n)
            break
          else:
            self.doble_rotacion_derecha(n)
            break
        else:
          derecha_hijo = n.derecha
          if derecha_hijo is not None:
            h_derecha = (derecha_hijo.derecha.altura if
                       (derecha_hijo.derecha is not None) else 0)
            h_izquierda = (derecha_hijo.izquierda.altura if
                      (derecha_hijo.izquierda is not None) else 0)
          if (h_izquierda > h_derecha):
            self.doble_rotacion_izquierda(n)
            break
          else:
            self.rotacion_derecha(n)
            break
      n = n.padre

  def rotacion_izquierda(self, nodo):
    aux = nodo.padre.label
    nodo.padre.label = nodo.label
    nodo.padre.derecha = nodo(aux)
    nodo.padre.derecha.altura = nodo.padre.altura + 1
    nodo.padre.izquierda = nodo.derecha

  def rotacion_derecha(self, nodo):
    aux = nodo.padre.label
    nodo.padre.label = nodo.label
    nodo.padre.izquierda = nodo(aux)
    nodo.padre.izquierda.altura = nodo.padre.altura + 1
    nodo.padre.derecha = nodo.derecha

  def doble_rotacion_izquierda(self, nodo):
    self.rotacion_derecha(nodo.getderecha().getderecha())
    self.rotacion_izquierda(nodo)

  def doble_rotacion_derecha(self, nodo):
    self.rotacion_izquierda(nodo.getizquierda().getizquierda())
    self.rotacion_derecha(nodo)

  def empty(self):
    if self.root is None:
      return True
    return False

  def preVisualizar(self, curr_nodo):
    if curr_nodo is not None:
      self.preVisualizar(curr_nodo.izquierda)
      print(curr_nodo.label, end=" ")
      self.preVisualizar(curr_nodo.derecha)

  def preorder(self, curr_nodo):
    if curr_nodo is not None:
      self.preVisualizar(curr_nodo.izquierda)
      self.preVisualizar(curr_nodo.derecha)
      print(curr_nodo.label, end=" ")

  def getRoot(self):
    return self.root

class ConstruccionArbolAVL:
    def __init__(self):
        self.__add_count__ = None
        self.__names__ = None

    def graficar(self):
        import matplotlib.pyplot as plt
        import numpy as np

        an = np.linspace(0, 2 * np.pi, 100)
        fig, axs = plt.subplots()

        fig.set_size_inches(8, 6)
        axs.clear()
        axs.set_axis_off()

        def text(px, py, _text):
            axs.text(px, py, _text, backgroundcolor="white", ha='center', va='top', color='black')

        correction = 0

        plt.show()
        for i in self.__names__:
            #Numero de nodo
            #(i[1])
            #Posicion en x
            #(i[2])
            #Posicion en y
            #(i[3])
            #Altura de arbol
            #(i[4])
            if i[2] == 0 and i[3] == 0:
                axs.plot(0 + .4 * np.cos(an), 0 + .4 * np.sin(an))
                # RAIZ
                text(0, 0, "%s %s" % (i[0], i[1]))
                plt.pause(.15)
                continue
            # RAMA DERECHA
            if i[5] == "r":
                correction = self.__add_count__ - 1
            # RAMA IZQUIERDA
            elif i[5] == "l":
                correction = - self.__add_count__ + 1

            x2 = i[2] + correction
            y2 = i[3]
            # -- PRIMERA RAMA
            if y2 == -1:
                x1 = i[4]
            else:
                x1 = i[4] + correction
            y1 = y2 + 1
            # DIBUJA CIRCULOS
            axs.plot(x2 + .4 * np.cos(an), y2 + .4 * np.sin(an))
            text(x2, y2, "%s %s" % (i[0], i[1]))
            plt.pause(.15)
            axs.plot([x1, x2], [y1, y2])
            plt.pause(.15)

if __name__ == '__main__':
  t = AVL()
  arbol1 = ConstruccionArbolAVL()
  t.insertar(5)
  t.insertar(9)
  t.insertar(13)
  t.insertar(10)
  t.insertar(17)
  t.preVisualizar(t.root)
  arbol1.graficar()
