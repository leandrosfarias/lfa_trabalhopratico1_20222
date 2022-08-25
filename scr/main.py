base = open('base.txt', 'r')
for linha in base:
    if "states" in linha:
        print("States entrou")
    if "initial" in linha:
        print("Initial entrou")
    if "accepting" in linha:
        print("Accepting entrou")
    if "alphabet" in linha:
        print("Alphabet entrou")
    if "transitions" in linha:
        print("Transitions entrou")
print(base.readlines())
base.close()