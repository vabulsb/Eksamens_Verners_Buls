# Ievade svara (kilogramos) un augstuma (metros)
svars = float(input("Ievadiet svaru (kg): "))
augstums = float(input("Ievadiet augstumu (m): "))

# KMA aprēķins
bmi = svars / (augstums**2)

# Izvade BMI
print("Tavs Ķermeņa Masas Indekss (KMA) ir:", bmi)