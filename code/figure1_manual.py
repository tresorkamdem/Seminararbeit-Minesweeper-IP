# Figure 1 - Manuelle Modellierung mit FICO Xpress

import xpress as xp

# -----------------------------
# 1. Modell erstellen
# -----------------------------

prob = xp.problem()

# Zeilen und Spalten der 6x6-Instanz
I = range(1, 7)
J = range(1, 7)

print("Zeilen:", list(I))
print("Spalten:", list(J))

# -----------------------------
# 2. Entscheidungsvariablen
# -----------------------------

x = {}

for i in I:
    for j in J:
        x[(i, j)] = xp.var(vartype=xp.binary, name=f"x_{i}_{j}")

prob.addVariable(list(x.values()))

print("\nAnzahl Variablen:", len(x))

# -----------------------------
# 3. Manuelle Nebenbedingungen
# -----------------------------

constraints = []

constraints.append((["x_1_1", "x_1_2", "x_1_3", "x_2_1", "x_3_1"], 2))  # N1
constraints.append((["x_1_2", "x_1_3", "x_1_4"], 2))                    # N2
constraints.append((["x_1_3", "x_1_4", "x_1_5"], 2))                    # N3
constraints.append((["x_1_4", "x_1_5", "x_1_6", "x_2_6", "x_3_6"], 2))  # N4
constraints.append((["x_2_1", "x_3_1", "x_4_1"], 2))                    # N5
constraints.append((["x_2_6", "x_3_6", "x_4_6"], 2))                    # N6
constraints.append((["x_3_1", "x_4_1", "x_5_1"], 2))                    # N7
constraints.append((["x_3_6", "x_4_6", "x_5_6"], 2))                    # N8
constraints.append((["x_4_1", "x_5_1", "x_6_1", "x_6_2", "x_6_3"], 2))  # N9
constraints.append((["x_6_2", "x_6_3", "x_6_4"], 2))                    # N10
constraints.append((["x_6_3", "x_6_4", "x_6_5"], 2))                    # N11
constraints.append((["x_4_6", "x_5_6", "x_6_4", "x_6_5", "x_6_6"], 2))  # N12

print("\nManuell formulierte Nebenbedingungen:")

for number, (variables, rhs) in enumerate(constraints, start=1):
    left_side = " + ".join(variables)
    print(f"N{number}: {left_side} = {rhs}")

# Nebenbedingungen an Xpress übergeben
for variables, rhs in constraints:
    lhs = 0

    for var in variables:
        _, i, j = var.split("_")
        lhs += x[(int(i), int(j))]

    prob.addConstraint(lhs == rhs)

# -----------------------------
# 4. Datenmatrix für Kontrolle
# -----------------------------

R = [
    [-1, -1, -1, -1, -1, -1],
    [-1,  2,  2,  2,  2, -1],
    [-1,  2,  0,  0,  2, -1],
    [-1,  2,  0,  0,  2, -1],
    [-1,  2,  2,  2,  2, -1],
    [-1, -1, -1, -1, -1, -1],
]

print("\nMatrix R:")

for row in R:
    print(row)

# -----------------------------
# 5. Automatische Kontrolle
# -----------------------------

def get_neighbors(i, j):
    neighbors = []

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:

            if di == 0 and dj == 0:
                continue

            ni = i + di
            nj = j + dj

            if 0 <= ni < 6 and 0 <= nj < 6:
                if R[ni][nj] == -1:
                    neighbors.append((ni + 1, nj + 1))

    return neighbors


auto_constraints = []

for i in range(6):
    for j in range(6):

        if R[i][j] >= 0:
            neighbors = get_neighbors(i, j)

            if len(neighbors) > 0:
                variables = [f"x_{p}_{q}" for (p, q) in neighbors]
                auto_constraints.append((variables, R[i][j]))

print("\nAutomatisch erzeugte Nebenbedingungen zur Kontrolle:")

for number, (variables, rhs) in enumerate(auto_constraints, start=1):
    left_side = " + ".join(variables)
    print(f"N{number}: {left_side} = {rhs}")

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

for i in I:
    row = []

    for j in J:
        value = round(prob.getSolution(x[(i, j)]))
        row.append(str(value))

    print(" ".join(row))