print("Clases versión 2 El constructor")
class Perro:
    # funcion constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
        
    # funciones creadas por el usuario
    def muerde(self):
        print("Chale el perro me mordió")
        
    def chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    
    def chatperra(self, mensajepe):
        print(f"Chat perra: {mensajepe}")
        
    def datos(self):
        print(f"Color: {self.color} \nEdad:{self.edad}")
        
# crear el objeto
chihuas = Perro("Negro", 2)

#llamadas a las funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola Boby")
chihuas.chatperro("Quieres ser mi gugguu?")
chihuas.chatperra("grrru.......")
