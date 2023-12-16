
from qiskit import *
from qiskit.circuit.library.standard_gates import XGate
from qiskit.circuit.quantumregister import QuantumRegister
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
import random

def circuit_m1():
    #adder,f0~f3  g0~g3 aux(4 qbits)
    qc = QuantumCircuit(12)
    qc.ccx(0,4,8)
    qc.ccx(1,5,10)
    qc.ccx(2,6,11)
    qc.cx(8,9)
    qc.cx(10,8)
    qc.cx(0,1)
    qc.cx(2,3)
    qc.cx(4,5)                               #F_24multiplication       图6
    qc.cx(6,7)
    qc.cx(11,10)
    qc.cx(9,11)
    qc.ccx(3,7,8)
    qc.ccx(1,5,11)
    qc.cx(3,1)
    qc.cx(7,5)
    qc.cx(11,9)
    qc.cx(2,3)
    qc.cx(6,7)
    qc.cx(8,9)
    qc.cx(0,2)
    qc.cx(4,6)
    qc.cx(9,10)
    qc.ccx(3,7,8)
    qc.ccx(2,6,11)
    qc.cx(8,10)
    qc.cx(11,10)
    qc.ccx(1,5,11)
    qc.cx(2,1)
    qc.cx(6,5)
    qc.ccx(1,5,8)
    qc.cx(0,2)
    qc.cx(4,6)
    qc.cx(3,1)
    qc.cx(7,5)
    qc.barrier()
    return qc

def circuit_m2():
    #adder,f0~f3  g0~g3 aux(4 qbits)
    qc = QuantumCircuit(12)
    qc.cx(10,9)
    qc.cx(11,10)
    qc.cx(8,11)
    qc.cx(9,11)
    qc.cx(10,11)
    qc.cx(10,8)
    
    qc.ccx(0,4,8)
    qc.ccx(1,5,10)
    qc.ccx(2,6,11)
    qc.cx(8,9)
    qc.cx(10,8)
    qc.cx(0,1)
    qc.cx(2,3)
    qc.cx(4,5)                               #F_24multiplication       图7
    qc.cx(6,7)
    qc.cx(11,10)
    qc.cx(9,11)
    qc.ccx(3,7,8)
    qc.ccx(1,5,11)
    qc.cx(3,1)
    qc.cx(7,5)
    qc.cx(11,9)
    qc.cx(2,3)
    qc.cx(6,7)
    qc.cx(8,9)
    qc.cx(0,2)
    qc.cx(4,6)
    qc.cx(9,10)
    qc.ccx(3,7,8)
    qc.ccx(2,6,11)
    qc.cx(8,10)
    qc.cx(11,10)
    qc.ccx(1,5,11)
    qc.cx(2,1)
    qc.cx(6,5)
    qc.ccx(1,5,8)
    qc.cx(0,2)
    qc.cx(4,6)
    qc.cx(3,1)
    qc.cx(7,5)
    return qc

def circuit_I():
    # x0~3, aux(1 qbits)   F_24 multiplicative inversion
    qc = QuantumCircuit(5)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.ccx(2, 3, 0)
    qc.ccx(0, 1, 3)
    qc.cx(3, 1)
    qc.cx(2, 0)  # F_24inv  图9
    qc.cx(0, 3)
    qc.ccx(3, 2, 4)
    qc.ccx(4, 1, 0)
    qc.ccx(3, 2, 4)
    qc.ccx(4, 1, 0)
    qc.ccx(0, 3, 2)
    qc.ccx(1, 2, 3)
    qc.cx(3, 1)
    qc.cx(3, 0)
    qc.swap(2, 3)
    qc.swap(1, 2)
    return qc

def circuit_lambda():
    # m -> m^2 * lambda   Fig.14
    qc = QuantumCircuit(4)
    qc.cx(2,3)
    qc.cx(1,2)
    qc.cx(3,1)
    qc.cx(3,0)
    qc.swap(0,2)
    qc.swap(1,3)
    return qc

def circuit_M(): #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    qc = QuantumCircuit(8)
    qc.cx(4, 1)
    qc.cx(6, 7)
    qc.cx(4, 3)
    qc.cx(2, 4)
    qc.cx(3, 6)
    qc.cx(5, 3)
    qc.cx(1, 5)
    qc.cx(5, 0)
    qc.cx(7, 5)
    qc.cx(4, 7)
    qc.cx(6, 7)
    qc.swap(4, 7)
    qc.swap(5, 6)
    qc.swap(3, 5)
    qc.swap(4, 1)
    qc.swap(3, 2)

    return qc

def circuit_A_Minverse(): #xxxxxxxxxxxxxxxxxxxxxxxx
    #A*M^(-1)+c
    qc = QuantumCircuit(8)
    qc.cx(2, 3)
    qc.cx(0, 5)
    qc.cx(1, 3)
    qc.cx(6, 1)
    qc.cx(7, 6)
    qc.cx(4, 2)
    qc.cx(0, 2)
    qc.cx(3, 4)
    qc.cx(3, 0)
    qc.cx(5, 3)
    qc.cx(5, 6)
    qc.cx(4, 7)
    qc.cx(1, 4)
    qc.cx(4, 5)
    qc.swap(2, 7)
    qc.swap(4, 6)
    qc.swap(2, 5)
    qc.swap(0, 4)
    qc.swap(3, 1)


    # qc.swap(0, 1)
    # qc.swap(1, 2)
    # qc.swap(0, 3)
    # qc.swap(1, 4)
    # qc.swap(1, 5)
    # qc.swap(0, 6)
    # qc.swap(7, 5)
    # qc.cx(0, 6)
    # qc.cx(0, 3)
    # qc.cx(5, 0)
    # qc.cx(7, 5)
    # qc.cx(4, 7)
    # qc.cx(6, 4)
    # qc.cx(3, 4)
    # qc.cx(7, 6)
    # qc.cx(2, 7)
    # qc.cx(4, 5)
    # qc.cx(2, 4)
    # qc.cx(1, 2)
    # qc.cx(2, 0)
    # qc.cx(6, 2)
    # qc.cx(4, 1)

    return qc

def circuit_K1(): #xxxxxxxxxxxxxxxxxxxxxxxx
    #K1
    qc = QuantumCircuit(9)
    qc.cx(2,3)
    qc.cx(1,4)
    qc.cx(2,4)
    qc.cx(5,6)
    qc.cx(0,6)
    qc.cx(1,7)
    qc.cx(3,7)
    qc.cx(4,5)
    qc.cx(3,5)
    qc.cx(2,3)
    qc.ccx(6,7,4)
    qc.ccx(4,5,7)
    qc.cx(7,5)
    qc.cx(6,4)                                                       #图12
    qc.cx(4,7)
    qc.ccx(7,6,8)
    qc.ccx(8,5,4)
    qc.ccx(7,6,8)
    qc.ccx(8,5,4)
    qc.ccx(4,7,6)
    qc.ccx(5,6,7)
    qc.cx(7,5)
    qc.cx(7,4)
    qc.swap(6,7)
    qc.swap(5,6)

    return qc
# In[6]:
def circuit_K2(): #xxxxxxxxxxxxxxxxxxxxxxxx
    #K2
    qc = QuantumCircuit(9)
    qc.cx(5,6)
    qc.cx(4,5)
    qc.ccx(6,7,4)
    qc.ccx(4,5,7)
    qc.cx(7,5)
    qc.cx(6,4)                                                       #图13
    qc.cx(4,7)
    qc.ccx(7,6,8)
    qc.ccx(8,5,4)
    qc.ccx(7,6,8)
    qc.ccx(8,5,4)
    qc.ccx(4,7,6)
    qc.ccx(5,6,7)
    qc.cx(2,3)
    qc.cx(3,7)
    qc.cx(7,5)
    qc.cx(0,5)
    qc.cx(3,6)
    qc.cx(1,6)
    qc.cx(2,3)
    qc.cx(7,4)
    qc.cx(3,4)
    qc.cx(1,4)
    qc.swap(6,7)
    qc.swap(5,6)

    return qc


def multi_inverse_2():
    multi_inverse_circuit = QuantumCircuit(20)
    qreg = multi_inverse_circuit.qregs[0]
    for i in range(4):
        multi_inverse_circuit.cx(4 + i, i)
    multi_inverse_circuit.append(circuit_m1(), qreg[7::-1] + qreg[8:12:1])
    for i in range(4):
        multi_inverse_circuit.cx(i, i + 4)
    # # # #
    multi_inverse_circuit.append(circuit_K1(), qreg[7:3:-1] + qreg[8:13:1])
    # # #
    multi_inverse_circuit.append(circuit_m1(), qreg[7:3:-1] + qreg[8:12:1] + qreg[15:11:-1])
    multi_inverse_circuit.append(circuit_m1(), qreg[3::-1] + qreg[8:12:1] + qreg[19:15:-1])
    multi_inverse_circuit.append(circuit_I(),qreg[8:13:1])
    multi_inverse_circuit.append(circuit_m2(), qreg[15:11:-1] + qreg[8:12:1] + qreg[7:3:-1])
    multi_inverse_circuit.append(circuit_m2(), qreg[19:15:-1] + qreg[8:12:1] + qreg[3::-1])


    multi_inverse_circuit.append(circuit_K2(), qreg[15:11:-1] + qreg[8:12:1] + qreg[7:8:1])
    for i in range(4):
        multi_inverse_circuit.cx(16 + i, 12+i)
    multi_inverse_circuit.append(circuit_m1().inverse(), qreg[15:11:-1] + qreg[19:15:-1] + qreg[8:12:1])
    for i in range(4):
        multi_inverse_circuit.cx(16 + i, 12+i)

    return multi_inverse_circuit

def SBox_input_circuit():
    sbox_input_circuit = QuantumCircuit(8) #input qubits
    ini_array = []
    for i in range(8):
        a = random.randint(0,1)
        ini_array.append(a)
        if a:
            sbox_input_circuit.x(i)

    return ini_array,sbox_input_circuit


def SBox_circuit_2():
    SBox_circuit = QuantumCircuit(20)
    qreg = SBox_circuit.qregs[0]

    SBox_circuit.append(circuit_M(), qreg[7::-1])
    SBox_circuit.append(multi_inverse_2(), qreg[0:8:1] + qreg[8:12:1] + qreg[12:20:1])
    SBox_circuit.append(circuit_M().inverse(), qreg[7::-1])
    SBox_circuit.append(circuit_A_Minverse(), qreg[19:11:-1])

    SBox_circuit.x(13)
    SBox_circuit.x(15)
    SBox_circuit.x(17)
    SBox_circuit.x(19)

    return SBox_circuit

def binary_int_list_to_int(int_b_list):
    str_tmp_list = list(map(str, int_b_list))
    bstr = ''.join(str_tmp_list)
    int_value = int(bstr,2)
    return int_value

#convert an Int number to Hexadecimal(expressed by string)
def toHex(num):
        """
        :type num: int
        :rtype: str
        """
        chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        hexStr = ""
        
        if num < 0:
            num = num + 2**32
        
        while num >= 16:
            digit = num % 16
            hexStr = chaDic.get(digit, str(digit)) + hexStr
            num //= 16
        hexStr = chaDic.get(num, str(num)) + hexStr

        return hexStr

def SBox(int_binary_list):
    #input: int binary list
    #output: decimal number(after SBox,then convert the result to decimal number)
    
    x = binary_int_list_to_int(int_binary_list)
    SBOX = [
        0x55, 0xc2, 0x63, 0x71, 0x3b, 0xc8, 0x47, 0x86, 0x9f, 0x3c, 0xda, 0x5b, 0x29, 0xaa, 0xfd, 0x77,
        0x8c, 0xc5, 0x94, 0x0c, 0xa6, 0x1a, 0x13, 0x00, 0xe3, 0xa8, 0x16, 0x72, 0x40, 0xf9, 0xf8, 0x42,
        0x44, 0x26, 0x68, 0x96, 0x81, 0xd9, 0x45, 0x3e, 0x10, 0x76, 0xc6, 0xa7, 0x8b, 0x39, 0x43, 0xe1,
        0x3a, 0xb5, 0x56, 0x2a, 0xc0, 0x6d, 0xb3, 0x05, 0x22, 0x66, 0xbf, 0xdc, 0x0b, 0xfa, 0x62, 0x48,
        0xdd, 0x20, 0x11, 0x06, 0x36, 0xc9, 0xc1, 0xcf, 0xf6, 0x27, 0x52, 0xbb, 0x69, 0xf5, 0xd4, 0x87,
        0x7f, 0x84, 0x4c, 0xd2, 0x9c, 0x57, 0xa4, 0xbc, 0x4f, 0x9a, 0xdf, 0xfe, 0xd6, 0x8d, 0x7a, 0xeb,
        0x2b, 0x53, 0xd8, 0x5c, 0xa1, 0x14, 0x17, 0xfb, 0x23, 0xd5, 0x7d, 0x30, 0x67, 0x73, 0x08, 0x09,
        0xee, 0xb7, 0x70, 0x3f, 0x61, 0xb2, 0x19, 0x8e, 0x4e, 0xe5, 0x4b, 0x93, 0x8f, 0x5d, 0xdb, 0xa9,
        0xad, 0xf1, 0xae, 0x2e, 0xcb, 0x0d, 0xfc, 0xf4, 0x2d, 0x46, 0x6e, 0x1d, 0x97, 0xe8, 0xd1, 0xe9,
        0x4d, 0x37, 0xa5, 0x75, 0x5e, 0x83, 0x9e, 0xab, 0x82, 0x9d, 0xb9, 0x1c, 0xe0, 0xcd, 0x49, 0x89,
        0x01, 0xb6, 0xbd, 0x58, 0x24, 0xa2, 0x5f, 0x38, 0x78, 0x99, 0x15, 0x90, 0x50, 0xb8, 0x95, 0xe4,
        0xd0, 0x91, 0xc7, 0xce, 0xed, 0x0f, 0xb4, 0x6f, 0xa0, 0xcc, 0xf0, 0x02, 0x4a, 0x79, 0xc3, 0xde,
        0xa3, 0xef, 0xea, 0x51, 0xe6, 0x6b, 0x18, 0xec, 0x1b, 0x2c, 0x80, 0xf7, 0x74, 0xe7, 0xff, 0x21,
        0x5a, 0x6a, 0x54, 0x1e, 0x41, 0x31, 0x92, 0x35, 0xc4, 0x33, 0x07, 0x0a, 0xba, 0x7e, 0x0e, 0x34,
        0x88, 0xb1, 0x98, 0x7c, 0xf3, 0x3d, 0x60, 0x6c, 0x7b, 0xca, 0xd3, 0x1f, 0x32, 0x65, 0x04, 0x28,
        0x64, 0xbe, 0x85, 0x9b, 0x2f, 0x59, 0x8a, 0xd7, 0xb0, 0x25, 0xac, 0xaf, 0x12, 0x03, 0xe2, 0xf2
     ]
    return SBOX[x]

def get_QSBox_result(QSB_circuit):
    backend_sim = Aer.get_backend('qasm_simulator')
    
    job_sim = execute(QSB_circuit,backend_sim, shots = 10)
    
    result_sim = job_sim.result()
    counts = result_sim.get_counts(QSB_circuit)
    
    return counts


# In[7]:
if __name__ == '__main__':

    sbox_circuit = QuantumCircuit(20, 20)  # S-box circuit
    qreg = sbox_circuit.qregs[0]
    creg = sbox_circuit.cregs[0]
    inputarray, input_circuit = SBox_input_circuit()
    sbox_circuit.append(input_circuit, qreg[0:8:1])
    sbox_circuit.append(SBox_circuit_2(), qreg[0:20:1])
    sbox_circuit.measure(qreg[0:20:1], creg[0:20:1])

    counts = get_QSBox_result(sbox_circuit)
    print(inputarray)
    print("Classical Result:" + str("{0:b}".format(SBox((inputarray))).zfill(8)))
    print("Quantum Result:" + str(counts))
