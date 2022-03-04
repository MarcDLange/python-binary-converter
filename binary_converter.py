# Konvertiere den input() in int() und speichere ihn in decimal.
decimal = int(input())
# Erstelle eine leere liste und speichere sie in binary_number.
binary_number = []

# Definiere die funktion calculate() mit dem parameter number.
def calculate(number):
    # (% = Modulo, teilen mit Rest) | Wenn "number" / 2 einen Rest hat, also der Rest nicht null ist.
    if(number % 2 != 0):
        # Dann hänge an das Ende der Liste eine eins.
        binary_number.append(1)
    else:
        # Sonst eine null.
        binary_number.append(0)
    # divmod teilt und speichert die ganze Zahl sowie den Rest.
    whole_number = divmod(number, 2)
    # Ich weise number die ganze zahl von divmod zu.
    number = whole_number[0]
    # Ich gebe numer zurück wenn die funktion ausgeführt wird.
    return number

#Solange wie decimal größer oder gleich 1 ist:
while(decimal >= 1):
    #Soll der Rückgabewert von calculate(decimal) in decimal gespeichert werden.
    decimal = calculate(decimal)

# Drehe die reihenfolge der liste um.
binary_number.reverse()
# Erstelle einen leeren string und 
binary_number = " ".join(str(x) for x in binary_number)
# Gebe den Inhalt von binary_number auf dem Bildschirm aus.
print(binary_number)