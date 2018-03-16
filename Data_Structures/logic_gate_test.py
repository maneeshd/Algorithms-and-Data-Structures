"""
Created on: 16-Mar-2018
Created by: Maneesh D
"""
from Data_Structures.LogicGate import AndGate, OrGate, NotGate, Connector


if __name__ == '__main__':
    # Circuit Design:
    #  1,0--AND1---CON1---\ 0         1
    #                      OR1---CON3---NOT1---> 0
    #  1,1--AND2---CON2---/ 1

    and_1 = AndGate("AND1")
    and_2 = AndGate("AND2")
    or_1 = OrGate("OR1")
    not_1 = NotGate("NOT1")
    con_1 = Connector(and_1, or_1)
    con_2 = Connector(and_2, or_1)
    con_3 = Connector(or_1, not_1)
    print("\nCircuit Output:", not_1.get_output())
