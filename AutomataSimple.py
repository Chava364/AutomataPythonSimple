class Automata:
    def __init__(self):
        self.estado_actual = 'q0'  # Estado inicial
        self.estados_aceptacion = {'q1', 'q2'}  # Estados de aceptación
    
    def transicion(self, simbolo):
        """Realiza la transición según el símbolo de entrada."""
        if self.estado_actual == 'q0':
            if simbolo == 'a':
                self.estado_actual = 'q1'
            elif simbolo == 'b':
                self.estado_actual = 'q2'
        elif self.estado_actual == 'q1':
            if simbolo == 'a' or simbolo == 'b':
                self.estado_actual = 'q1'  # q1 se mantiene en sí mismo con a o b
        elif self.estado_actual == 'q2':
            if simbolo == 'a':
                self.estado_actual = 'q0'  # Regresa a q0 con a
            elif simbolo == 'b':
                self.estado_actual = 'q2'  # Se mantiene en q2 con b
    
    def procesar_cadena(self, cadena):
        """Procesa toda la cadena de entrada y retorna si fue aceptada o no."""
        for simbolo in cadena:
            self.transicion(simbolo)
        return self.estado_actual in self.estados_aceptacion

    def reiniciar(self):
        """Reinicia el autómata al estado inicial."""
        self.estado_actual = 'q0'

# Ejemplo de uso:
automata = Automata()

# Probar varias cadenas:
cadenas = ["abba", "abab", "baba", "bbb", "aaaa"]

for cadena in cadenas:
    automata.reiniciar()  # Reiniciar la máquina para cada cadena
    if automata.procesar_cadena(cadena):
        print(f"La cadena '{cadena}' es aceptada por el autómata.")
    else:
        print(f"La cadena '{cadena}' es rechazada por el autómata.")
