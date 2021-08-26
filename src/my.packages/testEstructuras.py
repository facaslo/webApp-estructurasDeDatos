import manageData 
import DataStructures
import time
import math

tipo = "linked"
tamanho = 10000000


usuarios = manageData.cargarUsuarios(tamanho,tipo)

start = time.time()
usuarios.getElement(math.floor((usuarios.count-1)/2))
end = time.time()
print("Tiempo transcurrido: " ,  end-start)

start = time.time()
usuarios.erase(math.floor((usuarios.count-1)/2))
end = time.time()
print("Tiempo transcurrido: " ,  end-start)

""" 
start = time.time()
usuarios.erase(usuarios.Size-1)
end = time.time()
print("Tiempo transcurrido: " ,  end-start) 


elementoParaInsertar.pushBack("a")
elementoParaInsertar.pushBack("1")

start = time.time()
usuarios.pushBack(elementoParaInsertar)
end = time.time()
print("Tiempo transcurrido: " ,  end-start)
"""