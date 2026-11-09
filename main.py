LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cipherRow(text):
    ciphered = ""

    for ch in text:
        if ch in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.index(ch)
            ciphered += LOWER_ALPHABETS[(index + 13) % 26]

        elif ch in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.index(ch)
            ciphered += UPPER_ALPHABETS[(index + 13) % 26]

        else:
            ciphered += ch

    return ciphered


def collectRows():
    rows = []

    print("Collecting plain text rows for ciphering.")

    while True:
        row = input("Insert row(empty stops): ")

        if row == "":
            break

        rows.append(row)

    return rows


def showCipheredText(rows):
    print("\n#### Ciphered text ####")

    for row in rows:
        print(cipherRow(row))


def saveCipheredText(rows):
    print("\n#### Ciphered text ####")

    filename = input("Insert filename to save: ")

    file = open(filename, "w")

    for row in rows:
        file.write(cipherRow(row) + "\n")

    file.close()

    print("Ciphered text saved!")


def main():
    print("Program starting.\n")

    rows = collectRows()

    print("\n1 - Show ciphered text")
    print("2 - Save ciphered text")

    choice = input("Your choice: ")

    if choice == "1":
        showCipheredText(rows)

    elif choice == "2":
        saveCipheredText(rows)

    else:
        print("Unknown option!")

    print("Program ending.")


main()
