"""
Created on: 16-Mar-2018
Created by: Maneesh D
"""


class LogicGate(object):
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a is None:
            pin_inp = int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
            return 0 if pin_inp == 0 else 1
        else:
            self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b is None:
            pin_inp = int(input("Enter Pin B input for gate " + self.get_label() + "-->"))
            return 0 if pin_inp == 0 else 1
        else:
            self.pin_b.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_a is None:
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            pin_inp = int(input("Enter Pin input for gate " + self.get_label() + "-->"))
            return 0 if pin_inp == 0 else 1
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, label):
        super(AndGate, self).__init__(label)

    def perform_gate_logic(self):
        inp1 = self.get_pin_a()
        inp2 = self.get_pin_b()
        if inp1 == 1 and inp2 == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        super(OrGate, self).__init__(label)

    def perform_gate_logic(self):
        inp1 = self.get_pin_a()
        inp2 = self.get_pin_b()
        if inp1 == 0 and inp2 == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, label):
        super(NotGate, self).__init__(label)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector(object):
    def __init__(self, fron_gate, to_gate):
        self.from_gate = fron_gate
        self.to_gate = to_gate
        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate
