class MooreAutomaton:
    def __init__(self):
        self.state = 'S0'  # Estado inicial
        self.output = []   # Lista para almacenar la salida

    def transition(self, input_bit):
        if self.state == 'S0':
            if input_bit == '0':
                self.output.append('0')
                self.state = 'S0'
            elif input_bit == '1':
                self.output.append('1')
                self.state = 'S1'

        elif self.state == 'S1':
            if input_bit == '0':
                self.output.append('0')
                self.state = 'S0'
            elif input_bit == '1':
                self.output.append('0')
                self.state = 'S2'

        elif self.state == 'S2':
            self.output.append('0')
            if input_bit == '0':
                self.state = 'S0'
            elif input_bit == '1':
                self.state = 'S1'

    def process_input(self, input_sequence):
        for bit in input_sequence:
            self.transition(bit)
        return ''.join(self.output)

# Ejemplo de uso
input_sequence = "11011011"
automaton = MooreAutomaton()
output_sequence = automaton.process_input(input_sequence)
print(f"Entrada: {input_sequence}")
print(f"Salida: {output_sequence}")