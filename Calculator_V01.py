"""
Czas na duże, poważne zadanie! Dojrzewasz jako programista, więc mamy coś odpowiedniego – stworzymy własny kalkulator,
oczywiście nieco uproszczony. Załóżmy, że będzie przyjmował zawsze dwie liczby do obliczeń.

Docelowo chcielibyśmy uzyskać taki efekt:

Po uruchomieniu programu jesteśmy pytani o typ obliczenia

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:
Następnie pobieramy dwie wartości liczbowe.

Korzystając z biblioteki logging, informujemy użytkownika,
jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).

Następnie wykonujemy obliczenie i drukujemy rezultat z print.

Do pobierania wartości użyj input. Nie ma potrzeby sprawdzania, czy podane argumenty są liczbami,
przewidujemy poprawne uzupełnienie.

Przykładowe wywołanie razem z wartościami wybranymi przez użytkownika może wyglądać tak:

>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70
Dla chętnych
Jeśli chcesz usprawnić swoje zadanie, możesz dodać dwa rozszerzenia:

Sprawdzaj, czy podana wartość na pewno jest liczbą.
W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa,
np. możesz dodać do siebie trzy i więcej liczb.
"""
#import packages
import sys
import logging

#configure logging
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

#define aritmethical operators
math_operations = {1: "sum", 2: "subtract", 3: "multiply", 4: "divide"}

def calc():
    #prompt to determine operation user wants to run
    action = int(input("\nWhat would you like to do? 1-Sum, 2-Subtract, 3-Multiply or 4-Divide?\n*Please enter a number corresponding to action: "))
    #prompt to get operators from user
    num_1 = float(input("Enter the first value to %s: " % math_operations.get(action)))
    num_2 = float(input("Enter the second value: "))

    #Performing calculation
    result = 0
    if action == 1:
        result = num_1 + num_2
    elif action == 2:
        result = num_1 - num_2
    elif action == 3:
        result = num_1 * num_2
    elif action == 4:
        result = num_1 / num_2

    #operation log
    logging.debug(f"Now I will {math_operations.get(action)} numbers: {num_1} and {num_2} ")

    #printing the operation result
    print(f"The result is - {result}")


calc()
