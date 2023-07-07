print("Evaluacion N°1 Programacion y redes Virtualizadas:")
print("Integrantes: Diego Torres y Paloma Torrijo:")
def info_usuario(usuario):
    valor = input("Ingrese su " + usuario + ": ")
    if len(valor) == 0:
        print("Debe ingresar su " + usuario)
        return info_usuario(usuario)
    else:
        return valor