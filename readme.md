# Python Übungen

## Übung 1 - Python Basics

### 1 
Erstellen Sie einen Kommentar der kurz das Programm benennt.

### 2
Erstellen Sie eine Ausgabe (print) mit dem Text `Hallo Welt!`.

### 3
Erweitern Sie diese Ausgabe, indem sie eine Variable `name` erstellen und dieser
Ihren Namen zuweisen.
Geben Sie nun die Variable `name` aus.

### 4
Erweitern Sie die Ausgabe, indem Sie einen vollständigen Satz ausgeben. `Hallo,
mein Name ist: {name}`

### 5
Erweitern Sie das Programm, indem Sie nach einem Namen fragen und diesen danach mit der Ausgabe 
aus Punkt 3 ausgeben.

Der Befehl dafür ist: `input()`

## Übung 2 - Python

### 1
Definieren Sie eine Variable `secret_number` mit einem Wert zwischen 1 und 10.

### 2
Erstellen Sie eine Eingabeaufforderung `input()` mit der Sie eine Zahl erfragen und
in der Variable `guess_number` speichern.

### 3
Erstellen Sie eine if-Abfrage die beiden Variablen vergleicht und bei Gleichheit einen
Text mit `print(“Treffer!“)` ausgibt.

### 4
Erweitern Sie die if/elif Abfragen so, dass das Programm erkennt, ob die geratene
Zahl größer oder kleiner ist als die `secret_number` und einen Text ausgibt. `Zahl zu
groß` oder `Zahl zu klein`.

## Übung 3 - Python

### 1
Erstellen Sie ein kleines Programm das erst eine (kleine) Zahl mit `input()` abfragt
und in einer Variable speichert.

### 2
Erstellen Sie eine while Schleife, die x-mal durchlaufen wird, abhängig von der Zahl
die eingegeben wurde.

### 3
Geben Sie den Text: `Python rockt!` x-mal in der while-Schleife aus.

### 4
Fügen Sie eine Abbruchbedingung ein, wenn der Nutzer eine 0 eingibt.

### 5
Geben Sie am Ende des Schleifendurchlaufs eine extra Meldung aus: `while Schleife durchlaufen.`

### 6
Geben Sie eine Fehlermeldung aus, wenn der Nutzer keine Zahl eingibt.

## Übung 4b - `while`-loop

### 1
Schreibe eine Python-Funktion, die die Summe aller natürlichen Zahlen von 1 bis zu einer gegebenen Zahl berechnet. 
Verwende dafür eine while-Schleife.

Beispiel:
```python
# Funktion aufrufen
result = summe_natuerliche_zahlen(5)
# Erwartete Ausgabe:
# Die Summe der natürlichen Zahlen von 1 bis 5 ist 15.
```

### 2
Schreibe eine Python-Funktion, die die Anzahl der Stellen einer gegebenen Zahl zählt. Verwende dafür eine
while-Schleife.

Beispiel:
```python
# Funktion aufrufen
result = anzahl_stellen(12345)
# Erwartete Ausgabe:
# Die Zahl 12345 hat 5 Stellen.
```

### 3
Schreibe eine Python-Funktion, die die Fakultät einer gegebenen Zahl berechnet. Verwende dafür eine while-
Schleife.

Beispiel:
```python
# Funktion aufrufen
result = fakultaet(5)
# Erwartete Ausgabe:
# Die Fakultät von 5 ist 120.
```

## Übung 4d - Python `for`-loop

### 1
Schreiben Sie ein Python-Programm, das die ersten 10 natürlichen Zahlen ausgibt, die durch 4 teilbar sind. Verwenden
Sie eine Schleife.

### 2
Schreiben Sie ein Python-Programm, das die Summe der geraden Zahlen von 1 bis 50 berechnet und ausgibt. Verwen-
den Sie eine Schleife.

### 3
Schreiben Sie ein Python-Programm, das die Quadratzahlen der Zahlen von 1 bis 5 ausgibt. Verwenden Sie eine for-
Schleife.

### 4
Schreiben Sie ein Python-Programm, das die Summe der Zahlen von 1 bis 10 ausgibt. Verwenden Sie eine for-Schleife.

## Übung 4e - Python Strings

### 1 String-Längenvergleich
Schreibe eine Funktion, die zwei Strings als Parameter akzeptiert und zurückgibt, ob die Länge des ersten Strings 
größer, kleiner oder gleich der Länge des zweiten Strings ist. Verwende dafür die entsprechenden String-Methoden.

```python
def vergleiche_string_laengen(str1, str2): 
  if len(str1) > len(str2): 
    return "Der erste String ist länger als der zweite." 
  elif len(str1) < len(str2): 
    return "Der erste String ist kürzer als der zweite." 
  else: return "Die Längen der beiden Strings sind gleich." 
# Beispielaufruf: 
string1 = "Python" 
string2 = "Programmierung" 
ergebnis = vergleiche_string_laengen(string1, string2) 
print(ergebnis)
```

### 2 Wortzählung in einem Satz
Schreibe eine Funktion, die einen Satz als Parameter akzeptiert und die Anzahl der Wörter im Satz zurückgibt. 
Verwende dafür eine geeignete String-Methode.

```python
def zaehle_woerter(satz): 
  woerter = satz.split() 
  anzahl_woerter = len(woerter) 
  return anzahl_woerter 
# Beispielaufruf: 
satz_beispiel = "Python ist eine mächtige Programmiersprache." 
anzahl = zaehle_woerter(satz_beispiel) 
print(f"Anzahl der Wörter im Satz: {anzahl}")
```

## Übung 4f1 - Python Functions I

### 1 
Schreibe eine Funktion, die den prozentualen Anteil einer Zahl in Bezug auf eine andere berechnet. 
(Es werden zwei Parameter übergeben)

### 2
Schreibe eine Funktion, die einen übergebenen String umkehrt. Tipp: Eine Möglichkeit ist slicing.

### 3
Schreibe eine Funktion `quadriere()`, die eine Zahl quadriert, und eine Funktion `verdopple()`, die eine Zahl 
verdoppelt. Erstelle dann eine Funktion `quadriere_und_verdopple()`, die beide Funktionen mit
einer Zahl als Parameter aufruft und die Ergebnisse zurückgibt.

### 4
Erstelle eine Funktion `berechne_mehrwertsteuer()`, die den Mehrwertsteuerbetrag für einen gegebenen Nettobetrag 
und Mehrwertsteuersatz berechnet. Dann schreibe eine Funktion `gesamt_bruttobetrag()`, die den Bruttobetrag unter 
Verwendung der Funktion `berechne_mehrwertsteuer()` berechnet.

## Übung 4f2 - Python Functions II

### 1 
Schreibe eine Funktion, die die Summe aller übergebenen Argumente berechnet (beliebig viele *Argumente).

### 2
Erstelle eine Funktion, die eine variable Anzahl an Wörtern akzeptiert und sie zu einem Satz zusammensetzt.

## Übung 4f3 - Python Functions II

### 1 
Schreibe eine Funktion, die den Umfang `2 * (Breite + Höhe)` eines Rechtecks berechnet,
wobei die Breite und Höhe als Keyword Arguments übergeben werden.

### 2
Erstelle eine Funktion, die den BMI (Body Mass Index) berechnet (`gewicht / groesse²`), wobei Gewicht und Größe als
Keyword Arguments übergeben werden.

## Übung 4 - Taschenrechner

### 1 
Erstellen Sie ein kleines Programm das zwei Zahlen mit input() abfragt und je in einer Variable speichert.

`erste Zahl: `

`zweite Zahl: `

### 2
Erstellen Sie eine Funktion, die nach der Eingabe beider Zahlen die zwei Variablen übergeben bekommt.

### 3
In der Funktion sollen beide Variablen addiert werden.

### 4
Geben Sie das Ergebnis mit return zurück.

### 5
Geben Sie die Rückgabe der Funktion mit `print()` aus. Erstellen Sie zusätzlich eine Abfrage nach der Rechenart. 
`+ - * /`
Diese Abfrage sollte von den Zahlen erscheinen.

### 6
Erstellen Sie für jede Rechenart (`addieren`, `subtrahieren`, `multiplizieren` und `dividieren`) eine eigene Funktion.

## Übung 5 - Listen

### 1 - Listen erstellen und Elemente hinzufügen
#### 1.1
Erstellen Sie eine leere Liste mit dem Namen `meine_liste`.

#### 1.2
Fügen Sie die Zeichenfolgen "Apfel", "Banane" und "Orange" der Liste hinzu.

### 2 - Elementzugriff und Ausgabe
#### 2.1
Geben Sie das zweite Element der Liste meine_liste aus.
#### 2.2
Geben Sie die Liste in umgekehrter Reihenfolge aus.

### 3 - Listenoperationen
#### 3.1
Erstellen Sie eine neue Liste namens zusatz_liste mit den Elementen "Erdbeere"
und "Traube".
#### 3.2
Verketten Sie meine_liste und zusatz_liste in einer neuen Liste namens kombinierte_liste.

### 4 Elemententfernung
#### 4.1. 
Entfernen Sie das Element "Banane" aus kombinierte_liste.
#### 4.2. 
Entfernen Sie das erste Element von meine_liste.

### 5 - Elementsuche und Index
#### 5.1. 
Überprüfen Sie, ob "Apfel" in meine_liste vorhanden ist.
#### 5.2. 
Finden Sie den Index des Elements "Orange" in meine_liste.

### 6 - Sortieren von Listen
#### 6.1. 
Sortieren Sie kombinierte_liste in aufsteigender Reihenfolge.
#### 6.2. 
Sortieren Sie meine_liste in absteigender Reihenfolge.

## Übung - RockPaperScissor

### 1
Erstellen Sie eine Abfrage für den Spieler, welche der drei Varianten er wählt. (Rock, Paper, Scissor)
### 2
Erstellen Sie für den Computer eine zufällige Wahl von Rock, Paper oder Scissor.

```python
# ggf. hilfreich
import random
random.choice()
```

### 3
Erstellen Sie einen Loop, der nach der Spielereingabe auswertet wer gewon-nen hat und eine entsprechende Meldung 
ausgibt.

`Stein schlägt Schere`

`Schere schlägt Papier`

`Papier schlägt Stein`

### 4
Fragen Sie den Nutzer, ob er nach Beendigung noch einmal spielen möchte. Wenn ja, starten Sie das Spiel erneut.

## Übung 9 - Python Dictionary

### 1
Erstellen Sie ein leeres Dictionary mit dem Namen "mein_dict".

### 2
Fügen Sie dem Dictionary aus Übung 1 den Schlüssel "Name" mit dem Wert "Max" hinzu.

### 3
Überprüfen Sie, ob der Schlüssel "Alter" im Dictionary aus Übung 2 vorhanden ist.

### 4
Aktualisieren Sie den Wert des Schlüssels "Name" im Dictionary aus Übung 2 auf "Anna".

### 5
Entfernen Sie den Schlüssel "Name" aus dem Dictionary aus Übung 4.

### 6
Erstellen Sie ein Dictionary mit den Schlüsseln "Fach" und "Note" und den Werten "Mathematik" und 9.

### 7
Fügen Sie dem Dictionary aus Übung 6 einen weiteren Schlüssel "Gewichtung" mit dem Wert 2 hinzu.

### 8
Erstellen Sie eine Funktion mit dem Namen "durchschnittsnote", die das gewichtete Durchschnittsnote basierend 
auf dem Dictionary aus Übung 7 berechnet.

### 9
Rufen Sie die Funktion aus Übung 8 mit dem Dictionary aus Übung 7 auf und geben Sie das Ergebnis aus.

### 10
Erstellen Sie eine Liste von Dictionaries, wobei jedes Dictionary Informationen über einen Studenten enthält 
(Name, Alter, Note).

## 10b - Dictionary

### Wörterbuch aktualisieren
Erstelle ein Programm, das ein Wörterbuch mit deutschen Wörtern und ihren englischen Übersetzungen verwaltet. 
Das Programm sollte die folgenden Funktionen haben:

#### Wörterbuch anzeigen:
Zeige das gesamte Wörterbuch mit den deutschen Wörtern und ihren Über-
setzungen an.

#### Wort hinzufügen:
Füge dem Wörterbuch ein neues deutsches Wort und seine englische Übersetzung hinzu.

#### Wort löschen:
Lösche ein deutsches Wort und seine Übersetzung aus dem Wörterbuch.

#### Wort übersetzen:
Gib die englische Übersetzung für ein gegebenes deutsches Wort aus.

Schreibe das Programm so, dass es eine interaktive Benutzeroberfläche bietet und den Benutzer
nach Aktionen fragt.

## Übung 10 - Dictionary

### 11 
Erstellen Sie eine Funktion namens "dict_mit_max_value", die ein Dictionary als Parameter nimmt und den Schlüssel 
mit dem höchsten Wert zurückgibt.

### 12
Erstellen Sie eine Funktion namens "merge_dicts", die zwei Dictionaries zusammenführt, wobei im Falle von 
Schlüsselüberschneidungen die Werte addiert werden.

### 13
Erstellen Sie eine Funktion namens "filter_dict", die ein Dictionary und einen Schwellenwert als Parameter nimmt 
und ein neues Dictionary zurückgibt, das nur Schlüssel-Wert-Paare enthält, deren Wert über dem Schwellenwert liegt.

### 14 
Erstellen Sie eine Funktion namens "reverse_dict", die die Schlüssel und Werte in einem Dictionary vertauscht.

### 15
Erstellen Sie eine Funktion namens "common_keys", die zwei Dictionaries als Parameter nimmt und eine Liste der 
gemeinsamen Schlüssel zurückgibt.

### 16 
Erstellen Sie eine Funktion namens "nested_dict_value", die einen verschachtelten Schlüssel als Liste von Schlüsseln 
nimmt und den entsprechenden Wert aus einem verschachtelten Dictionary zurückgibt.

### 17
Erstellen Sie eine Funktion namens "count_elements", die eine Liste von Elementen als Parameter nimmt und ein 
Dictionary zurückgibt, das die Häufigkeit jedes Elements enthält.

### 18
Erstellen Sie eine Funktion namens "remove_duplicates", die eine Liste von Dictionaries als Parameter nimmt und eine 
neue Liste zurückgibt, in der die Duplikate entfernt wurden (basierend auf den Werten der Schlüssel-Wert-Paare).

### 19
Erstellen Sie eine Funktion namens "dictionary_diff", die zwei Dictionaries als Parameter nimmt und ein neues 
Dictionary zurückgibt, das die Unterschiede zwischen den beiden enthält (Schlüssel und Werte).

### 20
Erstellen Sie eine Funktion namens "flatten_dict", die ein verschachteltes Dictionary als Parameter nimmt und ein 
flaches Dictionary zurückgibt, in dem die Schlüssel durch Punktnotation kombiniert werden.

## Übung 6 - Recap

Aufgabe:
- Schreibe eine Funktion mit dem Namen `doppel()`, die eine Zahl entgegennimmt und das doppelte dieser Zahl
zurückgibt.

- Erstelle eine Funktion namens `ist_gerade()`, die überprüft, ob eine gegebene Zahl gerade ist. Die Funktion sollte
True zurückgeben, wenn die Zahl gerade ist, und False sonst.

- Schreibe eine Funktion namens `summe_bis()`, die die Summe aller Zahlen von 1 bis zu einer gegebenen Zahl
berechnet und zurückgibt.

- Schreibe eine Funktion namens `quadrat()`, die die Quadratzahl einer gegebenen Zahl berechnet und zurückgibt.

- Schreibe eine Funktion namens `mittlere_zahl`, die die mittlere Zahl aus drei gegebenen Zahlen zurückgibt.

## Übung 8 - tupel

Gegeben ist eine Liste von Tupeln, die die Namen und Punktzahlen von Schülern darstellen. Implementieren Sie eine
Funktion, die die Durchschnittspunktzahl für jeden Schüler berechnet und ausgibt.
```python
# Gegebene Daten
schueler_noten = [
("Max", [85, 90, 92]),
("Anna", [88, 89, 90]),
("Tom", [78, 80, 82]),
]

# Funktion zur Berechnung des Durchschnitts
def durchschnitt_berechnen(name, noten):
  # TODO: Implementieren Sie die Berechnung des Durchschnitts
  pass

# Funktion zur Ausgabe der Durchschnittspunktzahl für jeden Schüler
def durchschnitt_ausgeben(notenliste):
  # TODO: Implementieren Sie die Ausgabe der Durchschnittspunktzahl für jeden Schüler
  pass

durchschnitt_ausgeben(schueler_noten)
```

## Übung 4 - Lottogenerator
Wir bauen einen kleinen Lotto-Zufallszahlengenerator.
Lotto 6 aus 49. Im Lotto gibt es ein Kästchen mit den Zahlen von 1 bis 49 die man ankreuzen kann. Insgesamt 6 Zahlen. 
Erstellen Sie ein Programm, das sechs Zahlen aus der Menge 1 bis 49 auswählt und sortiert ausgibt. 
Wichtig ist, dass keine Zahl doppelt vorkommen kann.

## Übung 11a - sets

### 1
Erstelle zwei Sets set1 und set2 mit jeweils mindestens 5 Elementen.

### 2
Füge ein neues Element zu set1 hinzu.

### 3
Überprüfe, ob ein bestimmtes Element in set2 vorhanden ist.

### 4
Entferne ein Element aus set1.

## Übung 11b - sets

### 1
Erstelle ein neues Set union_set, das die Vereinigung von set1 und set2 ist.

### 2
Erstelle ein neues Set intersection_set, das die Schnittmenge von set1 und set2 ist.

### 3
Erstelle ein neues Set difference_set, das die Differenz von set1 und set2 ist.

## Übung 11c - sets


### 1
Überprüfe, ob set1 eine Teilmenge von set2 ist.

### 2
Entferne alle Elemente aus set1.

### 3
Lösche das Set set2.

## Übung 11d - sets


### Mengenveränderungen und Aktualisierungen
#### 1
Füge alle Elemente von set2 zu set1 hinzu.
#### 2
Entferne die gemeinsamen Elemente von set1 und set2.
#### 3
Aktualisiere set1 mit den Elementen aus set2.

### Mengenvergleich
#### 1
Überprüfe, ob set1 und set2 gleich sind.
#### 2
Überprüfe, ob set1 und set2 unterschiedliche Elemente enthalten.

### Mengenlänge und maximales/minimales Element
#### 1
Finde die Länge von set1.
#### 2
Finde das maximale Element in set1.
#### 3
Finde das minimale Element in set1.

### Mengen-Komprehension
#### 1
Erstelle ein Set squares_set, das die Quadrate der Zahlen von 1 bis 5 enthält.
#### 2
Erstelle ein Set even_set, das die geraden Zahlen von 1 bis 10 enthält.

### Mengenmethoden-Kombination
#### 1
Erstelle ein Set set3 mit einigen Elementen.
#### 2
Füge die Elemente von set2 zu set3 hinzu und entferne dann die Elemente von set1.

### Mengenprüfung und Entfernung
#### 1
Überprüfe, ob set1 leer ist.
#### 2
Entferne alle Elemente von set2, die größer als 5 sind.

### Mengenarithmetik
#### 1
Erstelle ein Set prime_set mit den Primzahlen bis 10.
#### 2
Erstelle ein Set composite_set mit den zusammengesetzten Zahlen bis 10.
#### 3
Berechne die Vereinigung, Schnittmenge und Differenz von prime_set und composite_set.

### Mengenfilterung
#### 1
Erstelle ein Set mixed_set mit verschiedenen Datentypen (Zahlen, Strings, Bool).
#### 2
Filtere nur die Zahlen aus mixed_set und erstelle ein neues Set numbers_set.

## Klausurvorbereitung I

### Übung 1: Listen erstellen und bearbeiten

#### a)

Erstelle eine leere Liste namens meine_liste.

#### b) 

Füge die Zahlen 1, 2, 3 und 4 der Liste hinzu.

#### c) 

Drucke die Liste aus.

#### d) 

Ändere das zweite Element der Liste auf 99.

#### e) 

Entferne die Zahl 3 aus der Liste.

### Übung 2: Tuple erstellen und verwenden

#### a) 

Erstelle ein Tupel namens mein_tupel mit den Werten "Apfel", "Banane", "Orange".

#### b) 

Drucke das zweite Element des Tupels aus.

#### c) 

Versuche, das erste Element des Tupels zu ändern (dies sollte fehlschlagen).

### Übung 3: Listenslicing

#### a) 

Erstelle eine Liste von Zahlen von 1 bis 10.

#### b) 

Gib nur die geraden Zahlen aus der Liste aus.

## Klausurvorbereitung II

### Listen erstellen

- Erstelle eine leere Liste namens meine_liste.
- Füge die Zahlen 1, 2, 3 hinzu.
- Füge den String "Hallo" hinzu.

### Listenelemente zugreifen

- Greife auf das erste Element der Liste meine_liste zu.
- Greife auf das letzte Element der Liste zu.

### Liste verlängern

- Erstelle eine zweite Liste mit den Zahlen 4, 5, 6.
- Verlängere meine_liste um die Elemente der zweiten Liste.

### Listenelemente entfernen

- Entferne die Zahl 3 aus meine_liste.
- Entferne das Element "Hallo" aus der Liste.

### Listenumkehr
- Gegeben ist die Liste zahlen = [1, 2, 3, 4, 5].
- Kehre die Reihenfolge der Elemente in der Liste um, ohne die Methode reverse() zu verwenden.

## Klausurvorbereitung for-loops

### 1 For-Schleife und Bedingungen

Nutzen Sie eine For-Schleife, um alle Zahlen von 1 bis 10 auszugeben, außer der Zahl 5.

### 2 For-Schleife und Listenmanipulation
Gegeben ist die Liste zahlen = [1, 2, 3, 4, 5]. 
Multiplizieren Sie jede Zahl in der Liste mit 2 und geben Sie das Ergebnis
aus.

### 3 Verknüpfung von Schleifen und Bedingungen
Gegeben ist die Liste namen = ['Anna', 'Bob', 'Charlie', 'David']. Nutzen Sie eine For-Schleife, um nur die Namen auszu-
geben, die mehr als 3 Buchstaben haben.

### 4 For-Schleifen und Listenverarbeitung
Gegeben ist die Liste temperaturen = [18, 22, 17, 25, 20], die die Temperaturen in Grad Celsius darstellt. 
Nutzen Sie eine For-Schleife, um diese Temperaturen in Fahrenheit umzuwandeln und auszugeben. Die Umrechnungsformel lautet:
Fahrenheit = Celsius * 9/5 + 32.

## Klausurvorbereitung while-loops

### 1

Schreibe ein Python-Programm, das eine Zahl vom Benutzer entgegennimmt und dann die Summe aller Zah-
len von 1 bis zu dieser eingegebenen Zahl berechnet. Verwende dabei eine while-Schleife.

### 2

Schreibe ein Python-Programm, das die Anzahl der Ziffern in einer vom Benutzer eingegebenen Zahl zählt.
Verwende eine while-Schleife.

### 3

Schreibe ein Python-Programm, das die Anzahl der Zeichen (Buchstaben und Ziffern) in einer vom Benutzer
eingegebenen Zeichenkette zählt. Verwende eine while-Schleife.

### 4
Schreibe ein Python-Programm, das das Spiel "Zahlenraten" implementiert. Der Computer wählt eine Zufalls-
zahl zwischen 1 und 100, und der Benutzer muss die Zahl erraten. Das Programm gibt Hinweise, ob die gesuchte Zahl
größer oder kleiner als der geratene Wert ist. Verwende dabei eine while-Schleife.

## Klausurvorbereitung 2

### Listen erstellen

- Erstelle eine leere Liste namens meine_liste.
- Füge die Zahlen 1, 2, 3 hinzu.
- Füge den String "Hallo" hinzu.

### Listenelemente zugreifen

- Greife auf das erste Element der Liste meine_liste zu.
- Greife auf das letzte Element der Liste zu.

### Liste verlängern

- Erstelle eine zweite Liste mit den Zahlen 4, 5, 6.
- Verlängere meine_liste um die Elemente der zweiten Liste.

### Listenelemente entfernen

- Entferne die Zahl 3 aus meine_liste.
- Entferne das Element "Hallo" aus der Liste.

### Listenumkehr

- Gegeben ist die Liste zahlen = [1, 2, 3, 4, 5].
- Kehre die Reihenfolge der Elemente in der Liste um, ohne die Methode reverse() zu verwenden.

## Klausurvorbereitung Zusatzaufgaben

- Schreibe eine Funktion, die die Summe aller Zahlen von 1 bis zu einer gegebenen Zahl berechnet.

- Gegeben ist eine Liste von Zahlen. Schreibe eine Funktion, die die Summe aller ungeraden Zahlen in der Lis-
te berechnet.
zahlen_beispiel = [1, 2, 3, 4, 5, 6, 7, 8, 9]

- Schreibe eine Funktion wortlaengen_dict(satz), die ein Dictionary erstellt, dessen Schlüssel Wörter im Satz
sind und die Werte deren Längen.
satz = "Python ist eine großartige Programmiersprache"

- Schreibe eine Funktion woerter_zaehlen(satz), die die Anzahl der Wörter in einem Satz zählt.
satz = "Python ist eine großartige Programmiersprache"

- Schreibe eine Funktion schachbrett_muster(n), die ein Schachbrettmuster mit der Größe n x n als String zu-
rückgibt.

```bash
# # #
 # #
# # #
```
