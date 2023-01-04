import numpy as np

def oppgave33(punktA, punktB):
    xA = punktA[0]
    yA = punktA[1]
    xB = punktB[0]
    yB = punktB[1]

    ans = ((xB-xA)**2 + (yB-yA)**2)**0.5
    print(ans)

def oppgave34():
    oppgave33((2.3, 8.1), (7.4, -13.5))

def oppgave318():
    L = [-2.2, -1, 0, 1.1, 2]
    A = np.array(L)

    print(type(L))
    print(type(A))
    print('L = ', L)
    print('A = ', A)

def oppgave320():
    A1 = np.zeros([5])
    A2 = np.ones([5])
    A3 = np.zeros([5]) + 8.3
    A4 = np.zeros(len(A3)) + 9.4
    A5 = np.linspace(0, 0+(0.2*4), 5)
    A6 = np.arange(0, 1, 0.2)

    print('A1 =', A1)
    print('A2 =', A2)
    print('A3 =', A3)
    print('A4 =', A4)
    print('A5 =', A5)
    print('A6 =', A6)


def oppgave321():
    A = np.zeros([5])
    print(np.size(A))
    print(len(A))
    print(A.shape[0])

def oppgave322():
    C = np.array([0, 10, 20, 30])
    x = C[0]
    y = C[-1]
    z = C[1:]
    print(x)
    print(y)
    print(z)

    C[-1] = 50
    print(C)
    assert C[-1] == 50
    C[0:2] = 1
    print(C)

def oppgave324():
    E = np.array([0, 2, 4, 5, 3, 1])
    large = 0
    element = 0
    for nr, i in enumerate(E):
        if i > large:
            large = i
            element = nr

    print('element nr: ',element,'Value: ', large)

def oppgave327():
    for r in range(4):
        if r > 0:
            volum = (4*np.pi*r**3)/3
            print('radius = ', r, 'volum = ', volum)

if __name__ == '__main__':
    oppgave33((2.3, 8.1), (7.4, -13.5))
    oppgave34()
    oppgave318()
    oppgave320()
    oppgave321()
    oppgave322()
    oppgave324()
    oppgave327()

