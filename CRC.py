import random


# Συνάρτηση για τη δημιουργία ενός τυχαίου δυαδικού
# μηνύματος των k bits
def randomBinaryNum(k):
    D = ""
    for i in range(k):
        t = str(random.randint(0, 1))
        D += t
    return D


# Συνάρτηση που υλοποιεί την πράξη XOR δηλαδή τη δυαδική
# πρόσθεση/αφαίρεση χωρίς κρατούμενο
def xor(a, b):
    xor = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            xor.append('0')
        else:
            xor.append('1')
    return ''.join(xor)


# Συνάρτηση που υλοποιεί την αριθμητική modulo 2 για τη διαδοχική
# διαίρεση δυο δυαδικών αριθμών
def mod2(D, P):
    l = len(P)
    t = D[0: l]

    while l < len(D):
        if t[0] == '1':
            t = xor(P, t) + D[l]

        else:
            t = xor('0' * l, t) + D[l]
        l += 1

    if t[0] == '1':
        t = xor(P, t)
    else:
        t = xor('0' * l, t)

    return t


# Συνάρτηση για τον υπολογισμό του FCS
def FCS(D, P):
    l = len(P)

    # ολίσθηση προς τα αριστερά του μηνύματος κατά n-k
    slide = D + '0' * (l - 1)

    FCS = mod2(slide, P)
    return FCS


# Συνάρτηση για την αλλοίωση του μηνύματος
# Ανάλογα με την πιθανότητα BER αλλάζουν κάποια bits του μηνύματος
def changeD(Data, BER):
    n = len(Data)
    b = ""
    for i in range(n):
        if random.uniform(0, 1) < BER:
            if Data[i] == "1":
                b += "0"
            else:
                b += "1"
        else:
            b += Data[i]
    return b


NotDetected = 0
FalseData = 0
Changed = 0
for i in range(1000):
    k = 20
    BER = 0.001
    P = "110101"

    D = randomBinaryNum(k)

    F = FCS(D, P)

    T = D + F

    CD = changeD(T, BER)

    # Αλλοιωμένα μηνύματα
    flag = False
    if T != CD:
        Changed += 1
        flag = True

    CRC = mod2(CD, P)

    if flag == True and int(CRC) != 0:
        # μηνύματα που ανιχνεύονται ως εσφαλμένα από το CRC
        FalseData += 1

    if flag == True and int(CRC) == 0:
        # μηνύματα που φθάνουν με σφάλμα στον
        # αποδέκτη και δεν ανιχνεύονται από το CRC
        NotDetected += 1

print((Changed * 100) / 1000000)
print((FalseData*100)/1000000)
print((NotDetected*100)/1000000)

'''D = "101011100"
P = "11100"
BER = 0.01

F = FCS(D, P)
T = D + F
CD = changeD(T, BER)
CRC = mod2(CD, P)

print("FCS " + F)
print("T " + T)
print("CD " + CD)
print("CRC " + CRC)

if T != CD and int(CRC) == 0:
    print("Not Found")
elif T != CD and input(CRC) != 0:
    print("Found")
else:
    print("Approved")'''
