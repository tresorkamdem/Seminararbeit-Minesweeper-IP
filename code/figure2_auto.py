# Figure 2 - Eigene 8x8-Instanz mit automatischer Modellierung und FICO Xpress

import xpress as xp

# -----------------------------
# 1. Modell erstellen
# -----------------------------

prob = xp.problem()

I = range(1, 9)
J = range(1, 9)

# -----------------------------
# 2. Datenmatrix
# -1 = unbekanntes Feld
# 0,1,2,... = Zahlenfeld
# -----------------------------

R = [
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1,  2,  2,  2,  2,  2,  2, -1],
    [-1,  2,  0,  0,  0,  0,  2, -1],
    [-1,  2,  0, -1, -1,  0,  2, -1],
    [-1,  2,  0, -1, -1,  0,  2, -1],
    [-1,  2,  0,  0,  0,  0,  2, -1],
    [-1,  2,  2,  2,  2,  2,  2, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
]

print("Eigene 8x8-Instanz:")

for row in R:
    print(" ".join("?" if value == -1 else str(value) for value in row))

# -----------------------------
# 3. Entscheidungsvariablen
# -----------------------------

x = {}

for i in I:
    for j in J:
        x[(i, j)] = xp.var(vartype=xp.binary, name=f"x_{i}_{j}")

prob.addVariable(list(x.values()))

print("\nAnzahl Variablen:", len(x))

# -----------------------------
# 4. Nachbarschaftsfunktion
# -----------------------------

def get_neighbors(i, j):
    neighbors = []

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:

            if di == 0 and dj == 0:
                continue

            ni = i + di
            nj = j + dj

            if 0 <= ni < 8 and 0 <= nj < 8:
                if R[ni][nj] == -1:
                    neighbors.append((ni + 1, nj + 1))

    return neighbors

# -----------------------------
# 5. Automatische Nebenbedingungen
# -----------------------------

auto_constraints = []

for i in range(8):
    for j in range(8):

        if R[i][j] >= 0:
            number = R[i][j]
            neighbors = get_neighbors(i, j)

            if len(neighbors) > 0:
                variables = [f"x_{p}_{q}" for (p, q) in neighbors]
                auto_constraints.append((variables, number))

print("\nAutomatisch erzeugte Nebenbedingungen:")

for k, (variables, rhs) in enumerate(auto_constraints, start=1):
    left_side = " + ".join(variables)
    print(f"N{k}: {left_side} = {rhs}")

print("\nAnzahl Nebenbedingungen:", len(auto_constraints))

# Nebenbedingungen an Xpress übergeben

for variables, rhs in auto_constraints:
    lhs = 0

    for var in variables:
        _, i, j = var.split("_")
        lhs += x[(int(i), int(j))]

    prob.addConstraint(lhs == rhs)

# -----------------------------
# 6. Solver starten
# -----------------------------

print("\nSolver startet...")

prob.setObjective(0)
prob.solve()

print("Solver beendet.")

# -----------------------------
# 7. Lösung ausgeben
# -----------------------------

print("\nLösung:")
print("1 = Mine, 0 = keine Mine")

for i in I:
    row = []

    for j in J:
        value = round(prob.getSolution(x[(i, j)]))
        row.append(str(value))

    print(" ".join(row))