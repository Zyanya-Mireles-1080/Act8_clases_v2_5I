class Informacion:
    
    def mi_lista(self):
        lista_NomPerros = ["Boby","Dollar","Fany \n"]
        for x in lista_NomPerros:
            print(x)

    def mi_tupla(self):
        tupla_ColorPerros = ("Negro","Café","Blanco \n")
        for y in tupla_ColorPerros:
            print(y)
            
    def mi_conjunto(self):
        conjunto_razasPerros = {"Bulldog", "Beagle", "Poodle"}
        for z in conjunto_razasPerros:
            print(z)
            
    def mi_diccionario(self):
        diccionario_datosPerros = {
            "Boby" : "De raza Bulldog, color negro",
            "Dollar" : "De raza Beagle, color café",
            "Fany" : "De raza Poodle, color blanco"
        }
        for a,b in diccionario_datosPerros.items():
            print(a,b)
            
# Creando el objeto         
datos = Informacion()
print("Listado de nombres de perros")
datos.mi_lista()

print("Tupla de los colores de los perros")
datos.mi_tupla()

print("Conjunto de las razas de los perros")
datos.mi_conjunto()

print("\nDiccionario de los datos de los perros")
datos.mi_diccionario()