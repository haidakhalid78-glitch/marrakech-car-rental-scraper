import os
from datetime import datetime

# 1. I dati dei noleggi auto a Marrakech
dati_auto = [
    {"Modello": "Peugeot 301", "Carburante": "Essence", "Prezzo_MAD": 300, "Zona": "Aeroporto"},
    {"Modello": "Citroën C-Elysée", "Carburante": "Gazole", "Prezzo_MAD": 350, "Zona": "Guéliz"},
    {"Modello": "Fiat Doblò", "Carburante": "Gazole", "Prezzo_MAD": 450, "Zona": "Aeroporto"}
]

# 2. Crea la cartella dei report se non esiste
os.makedirs("reports", exist_ok=True)
data_oggi = datetime.now().strftime("%Y-%m-%d")
file_path = f"reports/report_noleggi_{data_oggi}.txt"

# 3. Scrive il report in un file di testo semplice
with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"=== REPORT NOLEGGIO AUTO MARRAKECH ({data_oggi}) ===\n\n")
    for auto in dati_auto:
        f.write(f"- Modello: {auto['Modello']}\n")
        f.write(f"  Carburante: {auto['Carburante']}\n")
        f.write(f"  Prezzo: {auto['Prezzo_MAD']} MAD/giorno\n")
        f.write(f"  Zona: {auto['Zona']}\n")
        f.write("-" * 30 + "\n")

print(f"Report creato con successo! Controlla la cartella 'reports'.")
