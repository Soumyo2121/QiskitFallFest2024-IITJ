import streamlit as st
from qiskit import *
from qiskit_aer import Aer
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import *
from qiskit_aer import QasmSimulator


st.title("Quantum Random Number Generator Using Entanglement")


n = st.number_input("Enter the number of entangled qubit pairs:", min_value=1, value=1)
nq = 2*n
nc = 2*n
# Create a Quantum Circuit with 2n qubits (for n entangled pairs)
qc = QuantumCircuit(nq, nc)

# Create entanglement for each qubit pair
for i in range(n):
    qc.h(2*i)           # Apply Hadamard gate to the first qubit of the pair
    qc.cx(2*i, 2*i+1)   # Apply CNOT gate to entangle the first and second qubit
    qc.measure(2*i, 2*i)    # Measure first qubit
    qc.measure(2*i+1, 2*i+1) # Measure second qubit



# Run the circuit on a simulator when button is clicked
if st.button("Generate Random Number"):
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=1)
    result = job.result().get_counts()

    # Extract the random bitstring (correlated results due to entanglement)
    random_bitstring = list(result.keys())[0]
    random_number = int(random_bitstring, 2)
    
    # Display the random number
    st.write(f"### The generated random number is: {random_number}")
    
    # Display the measurement outcome (bitstring)
    st.write(f"### The generated random Bitstring is: {random_bitstring}")