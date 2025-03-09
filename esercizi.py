#es 1
nome = "alberto"
eta = 25
hobby = "carte","giochi","figa"
print(f"mi chiamo {nome}, ho {eta} anni e i miei hobby sono: {hobby}")
#es 2
def controlla_pari(n):
    if n % 2 == 0:
      return "è pari"
    else:
      return "è dispari"
print(controlla_pari(4))
#es 3
numeri = [1,2,3,4,5,6,7,8,9,10]
for i in numeri:
   print(controlla_pari(i))
#es 4
studente = {"nome" : "alberto", "eta": 25, "voti": [8,7,8] }
def media_voti(s):
    somma = 0  
    for voto in s["voti"]:  
        somma = somma + voto  
    return somma / len(s["voti"])  
print(media_voti(studente))
print(round(media_voti(studente)))
print(f"{studente['nome']} media voti {media_voti(studente)}")
#es 5
def somma_numeri(*args):
    somma = 0
    for x in args:
        if isinstance(x, (int, float)):  # Controlla se x è un numero (int o float)
            somma = somma + x
    return somma
print(somma_numeri(1,"s,",4,5) )     
#es 6
tempertatura_c = [0,10,20,30,15,25]
tempertatura_fare = list(map(lambda c : c * 9/5 +32, tempertatura_c))
tempertatura_fare_filtred = list(filter(lambda f: f> 68, tempertatura_fare))
print(tempertatura_fare_filtred)
#es 7
def crea_potenza(esponente):
   def potenza(x):
      risultato = x ** esponente
      return risultato
   return potenza
quadrato = crea_potenza(2)
cubo = crea_potenza(3)
print(quadrato(2))
print(quadrato(3))
print(quadrato(4))
print(cubo(2))
print(cubo(3))
print(cubo(4))
#es 8
def fattoriale(n):
   if n == 1:
    return 0
   else:
      return n * fattoriale(n-1)
print(fattoriale(5))
def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
#es 9
def traccia(func):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {func.__name__} con argomenti {args} {kwargs}")
        risultato = func(*args, **kwargs)
        print(f"{func.__name__} ha restituito {risultato}")
        return risultato
    return wrapper

@traccia
def moltiplica(a, b):
    return a * b

print(moltiplica(3, 4))

#es 10
studenti = [
    {"nome": "Alice", "età": 20, "voti": [85, 90, 78]},
    {"nome": "Bob", "età": 22, "voti": [60, 65, 58]},
    {"nome": "Charlie", "età": 21, "voti": [95, 92, 88]},
    {"nome": "David", "età": 23, "voti": [70, 72, 68]}
]

def media_voti(studente):
    return sum(studente["voti"]) / len(studente["voti"])

def stampa_studenti(studenti):
    for studente in studenti:
        media = media_voti(studente)
        print(f"{studente['nome']} (età: {studente['età']}) ha una media di {media:.2f}")

print("Tutti gli studenti:")
stampa_studenti(studenti)

soglia = 70
studenti_filtrati = [s for s in studenti if media_voti(s) > soglia]

print("\nStudenti con media superiore a 70:")
stampa_studenti(studenti_filtrati)
    
