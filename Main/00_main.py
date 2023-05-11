"""Das ist die Hauptdatei"""

import module_display_persons

t_daten = module_display_persons.t_daten
module_display_persons.display()

import module_add
import module_change
import module_remove

## für Rolle gibt es nur zwei Werte, kann man das irgendiwe darstellen? Liste macht hier keinen Sinn, da sonst zwei Werte bei mir wären

def hauptmenü():
    start = input("Hallo, heute ist ein guter Tag um eine Liste zu bearbeiten. Gib 'a' für Hinzufügen ein, 'c' fürs Ändern und 'r' fürs Entfernen. ")
    if start == ["a"]:
        print("a")
        # #start mit module_add
        # elif start == ["c"]:
        # #start mit module_change
        # elif start == ["r"]:
        # #start mit module_remove
        # else:
        #     try:

#Module so verknüfen, dass man sie mit jeweiligen Buchstaben aufrufen kann (wenn das aufgerufen ist, wird diese Funktion ausgeführt. if a, kommt Modul_add ins Spiel, try and error kommt hier hinzu (ist es wirklich gültiger Buchstabe - noch warten
# Gib "Main" ein, wenn Du zum Hauptmenü willst

hauptmenü()

module_display_persons.display()
module_add.display()

