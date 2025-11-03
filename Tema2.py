#Date inițiale
from tkinter.font import names

elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

#Partea A – Afișare și prelucrare
print("A1. Elevii și notele lor:")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()

# A2. Nota maximă și minimă
nota_max = max(note)
#print("nota max: 10")
nota_min = min(note)
#print("nota min: 4")
#nota_min = note[note.index(nota_min)]
#nota_max = note[note.index(nota_max)]
#print("Nota maximă și minimă:")
print(f"Nota maximă este {nota_max}, obținută de:", end=" ")
for i in range(len(note)):
    if note[i] == nota_max:
        print(elevi[i], end=" ")
print()

print(f"Nota minima este {nota_min}, obținută de:", end=" ")
for i in range(len(note)):
    if note[i] == nota_min:
        print(elevi[i], end=" ")
print("\n")

# A3. Media clasei
media = sum(note) / len(note)
print(f"Media clasei este {media:.2f}")
print()

# A4. Promovați
print("Elevii promovați (nota ≥ 5):")
for i in range(len(note)):
    if note[i] >= 5:
        print(elevi[i])
print()

#Partea B – Actualizări

# B5. +1 punct fiecărei note (maxim 10)
for i in range(len(note)):
    note [i]= min(note[i] + 1 , 10)
print("Note dupa crestere cu un punct:" , note)
print()

# B6. Adăugare elev nou
elevi.append(elev_nou)
note.append(nota_elev_nou)
print("Liste după adăugarea elevului nou:")
print(elevi)
print(note)
print()

# B7. Ștergere elev predefinit
if elev_de_sters in elevi:
    index_sters = elevi.index(elev_de_sters)
    elevi.pop(index_sters)
    note.pop(index_sters)
    print(f"Elevul {elev_de_sters} a fost șters.")
else:
    print(f"Elevul {elev_de_sters} nu există în listă.")
print()

# Afisare liste actualizate.
print("Afisare liste actualizate:")
for i in range(len(elevi)):
       print(f"{elevi[i]}  nota {note[i]}")
       print()

#Partea C – Căutări și statistici fără input
print(" Căutări de nume:")
i = 0
while i < len(interogari_nume) and interogari_nume[i] != "stop":
    nume = interogari_nume[i]
    if nume in elevi:
        poz = elevi.index(nume)
        print(f"{nume} are nota {note[poz]}")
    else:
        print(f"{nume} nu există în listă.")
    i += 1
print()

# C10. Număr promovați / respinși
promovati = 0
respinși = 0
for n in note:
    if n >= 5:
        promovati += 1
    else:
        respinși += 1
print(f"Promovați: {promovati}, Respinși: {respinși}")
print()

# C11. Media promovaților
note_promovati = [n for n in note if n >= 5]
if len(note_promovati) > 0:
    media_promovati = sum(note_promovati) / len(note_promovati)
    print(f"Media promovaților este {media_promovati:.2f}")
else:
    print("Nu există elevi promovați.")




