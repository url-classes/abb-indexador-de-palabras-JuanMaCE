from line_text import LineText
from binary_search_tree import BinaryTree
from leerarchivo.main import leer_archivo

vec_text = []
for i in range(10):
    nombre_archivo = str(i + 1) + ".txt"
    contenido = leer_archivo(nombre_archivo)
    vec_text.append(str(contenido))
text = []
print(" ")
result = ""
procedencia = 1
for x in vec_text:
    for i in x:
        if i != " ":
            result += i
        else:
            text.append(LineText(result, procedencia))
            result = ""
    procedencia += 1

arbol = BinaryTree()
for i in text:
    arbol.insertar(i.data, str(i.procedencia))

arbol.Preorder()
