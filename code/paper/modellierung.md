

Kapitel 4: Mathematische Modellierung des Minesweeper-Problems

4.1 Problembeschreibung

Das Ziel des Minesweeper-Puzzles besteht darin, die Position aller versteckten Minen auf einem rechteckigen Spielfeld zu bestimmen. Im Gegensatz zum klassischen Computerspiel ist das gesamte Zahlenmuster bereits bekannt. Jede Zahl gibt an, wie viele Minen sich in den benachbarten Feldern befinden.

Gesucht wird eine Belegung aller Felder mit „Mine“ oder „keine Mine“, die mit sämtlichen vorgegebenen Zahlen konsistent ist.

Da jede Zelle nur zwei Zustände annehmen kann und zahlreiche logische Bedingungen gleichzeitig erfüllt werden müssen, eignet sich das Problem sehr gut für die Modellierung als ganzzahliges Optimierungsproblem (Integer Programming).

⸻

4.2 Mengen und Indizes

Zur Beschreibung des Spielfelds werden folgende Mengen definiert:

Zeilenmenge

I=\{1,\ldots,n\}

mit

* n = Anzahl der Zeilen.

Spaltenmenge

J=\{1,\ldots,m\}

mit

* m = Anzahl der Spalten.

Menge aller Felder

N = I \times J

Jedes Feld wird durch seine Koordinaten

(i,j)

identifiziert.

⸻

4.3 Entscheidungsvariablen

Für jedes Feld (i,j) wird eine binäre Variable definiert:

x_{i,j}
=
\begin{cases}
1,& \text{falls das Feld eine Mine enthält}\\
0,& \text{sonst}
\end{cases}

Die Variablen beschreiben somit die unbekannte Position aller Minen.

⸻

4.4 Definitionsbereich

Da ein Feld entweder eine Mine enthält oder nicht, gilt:

x_{i,j}\in\{0,1\}
\qquad
\forall (i,j)\in N

Es handelt sich somit um binäre Entscheidungsvariablen.

⸻

4.5 Nachbarschaft eines Feldes

Für jedes Feld (i,j) werden alle unmittelbar angrenzenden Felder betrachtet.

Dazu gehören:

* oben
* unten
* links
* rechts
* oben links
* oben rechts
* unten links
* unten rechts

Ein Feld besitzt somit höchstens acht Nachbarn.

⸻

4.6 Parameter

Die bekannten Zahlen des Rätsels werden durch die Matrix

R=(r_{i,j})

beschrieben.

Dabei gibt

r_{i,j}

die Anzahl der Minen in der Nachbarschaft von Feld (i,j) an.

Diese Werte sind bekannt und bilden die Eingabedaten des Modells.

⸻

4.7 Nebenbedingungen

Für jedes aufgedeckte Zahlenfeld muss gelten, dass die Anzahl der benachbarten Minen exakt dem angegebenen Zahlenwert entspricht.

Daraus ergibt sich die zentrale Nebenbedingung des Modells:

\sum_{p=i-1}^{i+1}
\sum_{q=j-1}^{j+1}
x_{p,q}
=
r_{i,j}

für alle Felder mit bekanntem Zahlenwert.

Diese Gleichung stellt sicher, dass jede Zahl genau durch die umliegenden Minen erklärt wird.

⸻

4.8 Beispiel einer Nebenbedingung

Angenommen ein Feld enthält die Zahl

2

und besitzt die acht Nachbarn

x_{11},x_{12},x_{13},
x_{21},x_{23},
x_{31},x_{32},x_{33}

Dann entsteht die Nebenbedingung

x_{11}
+x_{12}
+x_{13}
+x_{21}
+x_{23}
+x_{31}
+x_{32}
+x_{33}
=
2

Dies bedeutet, dass sich unter den acht Nachbarfeldern genau zwei Minen befinden müssen.

⸻

4.9 Zielfunktion

Für die Lösbarkeit des Minesweeper-Puzzles ist keine eigentliche Zielfunktion erforderlich.

Es genügt, eine zulässige Lösung zu finden, welche sämtliche Nebenbedingungen erfüllt.

Daher kann beispielsweise die konstante Zielfunktion

\min 0

verwendet werden.

Das Problem wird somit als reines Feasibility Problem formuliert.

⸻

4.10 Ziel des Solvers

Der Solver erhält:

* die Mengen I und J,
* die Parameter r_{i,j},
* die binären Variablen x_{i,j},
* sämtliche Nebenbedingungen.

Anschließend bestimmt er automatisch eine Belegung aller Variablen x_{i,j}, sodass sämtliche Bedingungen erfüllt werden.

Die Ausgabe des Solvers liefert schließlich die Position aller Minen im Spielfeld.
