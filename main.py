from binary_search_tree import BinarySearchTree
numeros: BinarySearchTree[str] = BinarySearchTree()
numeros.insert("h")
numeros.insert("z")
numeros.insert("a")
numeros.insert("d")
numeros.insert("e")
numeros.insert("f")
numeros.insert("g")
numeros.insert("h")
numeros.insert("i")
numeros.insert("z")
numeros.insert("a")


print(numeros.preorder())
print("Nodo maximo: ")
print(numeros.max())
print("Nodo minimo: ")
print(numeros.min())


if "jaan" < "jeen":
    print("si")

