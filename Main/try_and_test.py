if (0 < 1):
    print("Hallo Sarah!")


if (0 > 1):
    print("Nein")
else:
    print("Hallo Katharina")

with open("personen.txt", "r", encoding="UTF-8") as file:
    print(file.read())

with open("personen.txt", "w", encoding="UTF-8") as file:
    file.write("01, Alex, Berger, Burggasse 3, 1070, Wien\n")
    file.write(input())
    file.write("\n03, Otto, Berger, Burggasse 3, 1070, Wien\n")
with open("personen.txt", "r", encoding="UTF-8") as file:
    print(file.read())
