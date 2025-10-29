# Declararea șirului cu un text copiat dintr-un articol de știri
articol = """Ministerul Sănătății a anunțat că, începând de luni, vor fi disponibile noi centre de vaccinare în mai multe orașe din țară. 
Autoritățile recomandă populației să se programeze din timp, pentru a evita aglomerația. 
Campania de vaccinare, are ca scop, protejarea populației și reducerea numărului de îmbolnăviri."""

 # 1. Împărțirea șirului în două părți egale
lungime = len(articol)
mijloc = lungime // 2
prima_parte = articol[:mijloc]
a_doua_parte = articol[mijloc:]
print(prima_parte)
print(a_doua_parte)
print(len(prima_parte))
print(len(a_doua_parte))

# 2. Operații pe prima parte
prima_parte = prima_parte.upper()        # Transformă toate literele în majuscule
print(prima_parte)
prima_parte = prima_parte.strip()        # Elimină spațiile goale de la început și sfârșit
print(prima_parte)

#3. Operații pe a doua parte
a_doua_parte = a_doua_parte.capitalize() # Transformă prima literă în majusculă
print(a_doua_parte)

a_doua_parte = a_doua_parte[::-1]        # Inversează ordinea caracterelor
print(a_doua_parte)



# Elimină toate caracterele de punctuație
import string
punctuatie = ".,,,!,?"+string.punctuation  
a_doua_parte = ''.join([c for c in a_doua_parte if c not in punctuatie])

# 4. Combinarea celor două părți
rezultat = prima_parte + "\n" + a_doua_parte

# 5. Afișarea rezultatului final
print("=== Text procesat ===")
print(rezultat)

