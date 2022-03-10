reg_A = [''] * 93
reg_B = [''] * 84
reg_C = [''] * 111


for i in [93, 84, 111]:
    for j in range(i):
        if i == 93:
            reg_A[j] = 0
        elif i == 84:
            reg_B[j] = 0
        elif i == 111:
            reg_C[j] = 0

reg_C[108] = reg_C[109] = reg_C[110] = 1
for i in range(80):  # initializing key
    reg_A[i] = 0
    reg_B[i] = 0


stream = []
for i in range(70):
    # first calculate output bits of every register
    Cz = reg_C[110] ^ reg_C[65] ^ (reg_C[108] & reg_C[109])
    Ax = reg_A[92] ^ reg_A[65] ^ (reg_A[90] & reg_A[91])
    By = reg_B[83] ^ reg_B[68] ^ (reg_B[81] & reg_B[82])
    # then calculate first bit of every register
    a1 = Cz ^ reg_A[68]
    b1 = Ax ^ reg_B[77]
    c1 = By ^ reg_C[86]
    for x in range(92, 0, -1):  # go to 1, because we already have first bit calculated
        reg_A[x] = reg_A[x-1]
    reg_A[0] = a1
    for x in range(83, 0, -1):
        reg_B[x] = reg_B[x-1]
    reg_B[0] = b1
    for x in range(110, 0, -1):
        reg_C[x] = reg_C[x-1]
    reg_C[0] = c1
    stream.append(Ax ^ By ^ Cz)

print (reg_A, "FINAL")
print (reg_B)
print (reg_C)

print (stream, "FINAL STREAM AFTER 70 CLOCKS")