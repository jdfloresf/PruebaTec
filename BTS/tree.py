from node import Node

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def __recursive_add(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.left is None:
                nodo.left = Node(dato)
            else:
                self.__recursive_add(nodo.left, dato)

        else:
            if nodo.right is None:
                nodo.right = Node(dato)
            else:
                self.__recursive_add(nodo.right, dato)

    def __recursive_inorder(self, nodo):
        if nodo is not None:
            self.__recursive_inorder(nodo.left)
            print(nodo.dato, end=", ")
            self.__recursive_inorder(nodo.right)

    def __recursive_preorder(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__recursive_preorder(nodo.left)
            self.__recursive_preorder(nodo.right)

    def __recursive_postorder(self, nodo):
        if nodo is not None:
            self.__recursive_postorder(nodo.left)
            self.__recursive_postorder(nodo.right)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato ==  busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.left, busqueda)
        else:
            return self.__buscar(nodo.right, busqueda)
        
    def add(self, dato):
        self.__recursive_add(self.root, dato)

    def inorder(self):
        print("Recorrido inorder")
        self.__recursive_inorder(self.root)
        print("")
    
    def preorder(self):
        print("Recorrido preorder")
        self.__recursive_preorder(self.root)
        print("")
    
    def postorder(self):
        print("Recorrido postorder")
        self.__recursive_postorder(self.root)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.root, busqueda)
