import random
import enum

class Optiuni(enum.Enum):
    Rock = 1
    Paper  = 2
    Scissors = 3
    Lizar = 4
    Spock = 5

    def __str__(self):
        return self.name


    @classmethod
    def values(cls):
        return [op.value for op in Optiuni]
    
    @classmethod
    def pairs(cls):
        return [(op.name, op.value) for op in Optiuni]


print(Optiuni.values())

# ales = Optiuni(3)
# print(ales)

# print(Optiuni.Rock)
# print(Optiuni.Rock.value)

while True:
    client = input("Introduceti o valoarea 1.Rock, 2.Paper, 3.Scissors\n")
    server = random.choice([1, 2, 3])
    print(server)
    server = Optiuni(server)

    try:
        client = int(client)
        client = Optiuni(client)
    except:
        print("Valoare incorecta")
        continue

    if client == server:
        print("Egalitate")
    elif client == Optiuni.Rock and server == Optiuni.Scissors:
        print("Ai castigat")
    elif client == Optiuni.Scissors and server == Optiuni.Paper:
        print("Ai castigat")
    elif client == Optiuni.Paper and server == Optiuni.Rock:
        print("Ai castigat")
    else:
        print("Ai pierdut")
    print("Client:", client, "Server:", server)