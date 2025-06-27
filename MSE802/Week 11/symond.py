import numpy as np

# Define the f(x) mapping
f_table = {
    '00': '00',
    '01': '11',
    '10': '00',
    '11': '11'
}

def xor_bits(a, b):
    return ''.join(str(int(x)^int(y)) for x, y in zip(a, b))

def int_to_bin(n, bits=2):
    f = format(n, f'0{bits}b')
    print(f)
    return f 

# There are 4 qubits total: 2 for input x, 2 for output y
dim = 16  # 2^4 = 16 basis states
Uf = np.zeros((dim, dim), dtype=int)
print("Uf matrix (16x16):\n", Uf)
# Build the matrix
for i in range(dim):
    # Convert i to a 4-bit binary string (x0 x1 y0 y1)
    bits = int_to_bin(i, 4)
    x = bits[:2]
    print(x)
    y = bits[2:]
    print(y)
    print('...............')
    fx = f_table[x]
    print('fx' + fx)
    y_new = xor_bits(y, fx)
    out_bits = x + y_new
    j = int(out_bits, 2)

    Uf[j, i] = 1  # Uf maps |i⟩ to |j⟩

# Print the result
np.set_printoptions(linewidth=200)
print("Uf matrix (16x16):\n", Uf)













