import qiskit as qk

'''
When you run the script once, you do not need to add
your API key again as your account has already been
saved in memory
'''
TOKEN = '4cb909509e365586e960d3b82179adee139035eae0c2c6f21b307e9b4bbb89e6339df2a481ae239a9eb3389530be03e2840e97edcde1de45f5da075bfdf553a4'
qk.IBMQ.save_account(TOKEN, overwrite=True)
qk.IBMQ.load_account()

'''
`n` is the number of Qubits needed to 
generate a a random number between
0 and 2^n - 1
'''
n = 3

'''
Creating a Quantum Register with `n` Qubits and 
`n` Classical Bits where n=3
'''
q = qk.QuantumRegister(n)
c = qk.ClassicalRegister(n)
qc = qk.QuantumCircuit(q, c)

'''
Applying a Hadamard Gate on the n Qubits
to get a final bitstring of size n
The bitstring will be converted to a
decimal number (integer) between 0 and 2^3 - 1 (7)
'''
for i in range(n):
    qc.h(i)

qc.measure(q, c)
# The backend simulator available to me
backend = qk.IBMQ.get_provider().get_backend('ibmqx2')
new_job = qk.execute(qc, backend, shots=1)

# The output bitstring consists of 3 collapsed Qubits (bits)
bitstring = new_job.result().get_counts()

# Converting binary to Decimal integers
random_integer = int(list(bitstring.keys())[0], 2)

print(random_integer)
