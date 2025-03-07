

culori = [ "alb", "rosu", "negru", "verde"]
## rezultat = []

def lungimea_5(cuvant):
    return len(cuvant) == 5

print(list(filter(lungimea_5, culori)))

print(list(filter(lambda cuvant: len(cuvant) == 5  ,culori)))
print(list(filter(lambda cuvant: len(cuvant) == 4  ,culori)))
print(list(filter(lambda x: len(x) == 4  ,culori)))


