from tree import Tree

tree = Tree("Luis")
tree.add("Maria Jose")
tree.add("Maggie")
tree.add("Leon")
tree.add("Cuphead")
tree.add("Aloy")
tree.add("Jack")
tree.add("Jhon")

tree.preorder()
tree.inorder()
tree.postorder()

#Busqueda
busqueda = input("Buscar elemento: ")
nodo = tree.buscar(busqueda)

if nodo is None:
    print(f"{busqueda} no existe")
else: 
    print(f"{busqueda} si existe")