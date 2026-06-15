import matplotlib.pyplot as plt
import os

os.makedirs("figures", exist_ok=True)

def draw_grid(R, filename, title):
    n = len(R)
    m = len(R[0])

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, m)
    ax.set_ylim(0, n)
    ax.set_aspect("equal")
    ax.invert_yaxis()

    for i in range(n):
        for j in range(m):
            value = R[i][j]

            rect = plt.Rectangle((j, i), 1, 1, fill=False)
            ax.add_patch(rect)

            if value == -1:
                text = "?"
            else:
                text = str(value)

            ax.text(
                j + 0.5,
                i + 0.5,
                text,
                ha="center",
                va="center",
                fontsize=14
            )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


# Figure 1: manuelle 6x6-Instanz
R1 = [
    [-1, -1, -1, -1, -1, -1],
    [-1,  2,  2,  2,  2, -1],
    [-1,  2,  0,  0,  2, -1],
    [-1,  2,  0,  0,  2, -1],
    [-1,  2,  2,  2,  2, -1],
    [-1, -1, -1, -1, -1, -1],
]

# Figure 2: eigene automatische 8x8-Instanz
R2 = [
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1,  2,  2,  2,  2,  2,  2, -1],
    [-1,  2,  0,  0,  0,  0,  2, -1],
    [-1,  2,  0, -1, -1,  0,  2, -1],
    [-1,  2,  0, -1, -1,  0,  2, -1],
    [-1,  2,  0,  0,  0,  0,  2, -1],
    [-1,  2,  2,  2,  2,  2,  2, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
]

draw_grid(
    R1,
    "figures/figure1_manual_instance.png",
    "Figure 1: Manuelle 6x6-Instanz"
)

draw_grid(
    R2,
    "figures/figure2_automatic_instance.png",
    "Figure 2: Automatische 8x8-Instanz"
)
print("Figures successfully created.")

# ============================
# Solutions
# ============================

S1 = [
    [0,0,1,1,0,0],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,0,1,1,0,0]
]

S2 = [
    [0,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,1],
    [0,1,0,1,1,0,1,0]
]

def draw_solution(solution, filename, title):
    n = len(solution)
    m = len(solution[0])

    fig, ax = plt.subplots(figsize=(5,5))

    ax.set_xlim(0,m)
    ax.set_ylim(0,n)

    ax.set_aspect("equal")
    ax.invert_yaxis()

    for i in range(n):
        for j in range(m):

            rect = plt.Rectangle(
                (j,i),
                1,
                1,
                fill=False
            )

            ax.add_patch(rect)

            if solution[i][j] == 1:
                ax.text(
                    j+0.5,
                    i+0.5,
                    "●",
                    fontsize=18,
                    ha="center",
                    va="center"
                )

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(title)

    plt.tight_layout()
    plt.savefig(filename,dpi=300)
    plt.close()

draw_solution(
    S1,
    "figures/figure1_manual_solution.png",
    "Figure 1: Lösung der 6x6-Instanz"
)

draw_solution(
    S2,
    "figures/figure2_automatic_solution.png",
    "Figure 2: Lösung der 8x8-Instanz"
)

print("Solution figures created.")
