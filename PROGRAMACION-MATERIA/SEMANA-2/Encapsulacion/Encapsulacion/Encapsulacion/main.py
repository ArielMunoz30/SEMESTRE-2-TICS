from persona import Persona

p = Persona("Carlos", 20)

print("Nombre:", p.get_nombre())
print("Edad:", p.get_edad())

p.set_edad(22)
print("Nueva edad:", p.get_edad())
