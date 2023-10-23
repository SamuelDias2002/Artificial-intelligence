import random
import time
import matplotlib.pyplot as plt

'''Ex 1

Ex 2 -> Subsitituir 0.2 por um valor à escolha e verificar resultados
'''


def generate():
    s = [False, False, False]
    valid = False
    while not valid:
        for i in range(3):
            if random.random() <= 0.2:
                s[i] = True
            else:
                s[i] = False
        if ((s[0] or s[1]) and (s[1] or s[2])):
            valid = True
    return s[0], s[1], s[2]


c0 = 0
c1 = 0
c2 = 0
t = time.time()
for i in range(10000):
    s0, s1, s2 = generate()
    if s0:
        c0 += 1
    if s1:
        c1 += 1
    if s2:
        c2 += 1

print("Probabilidade de poço em (1,3):", c0 / 10000)
print("Probabilidade de poço em (2,2):", c1 / 10000)
print("Probabilidade de poço em (3,1):", c2 / 10000)
print("Tempo: " + str(time.time()-t))


'''Ex 3'''
pp = [0.01, 0.2, 0.5, 0.8, 0.99]
pc13 = [0.020, 0.307, 0.602, 0.827, 0.990]
pc22 = [0.991, 0.866, 0.795, 0.861, 0.991]

plt.plot(pp, pc13)
plt.plot(pp, pc22)
plt.show()

'''Ex 4'''

a = input("Digite o valor da proabilidade de poço:\n")

# Substituir 0.2 pelo a
