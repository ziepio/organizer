from organizer import Organizer

moj_organizer = Organizer('Mój organizer')

while True:

    print('''Co chcesz zrobić:

    1 - dodaj notatkę
    2 - dodaj wizytówkę
    3 - dodaj kod rabatowy
    4 - wyświetl notatkę
    5 - wyświetl wizytówkę
    6 - wyświetl kod rabatowy
    0 - zamknij organizer1
    
    ''')

    x = input()
    if x == '1':
        moj_organizer.dodaj_notatke()
    if x == '2':
        moj_organizer.dodaj_wizytowke()
    if x == '3':
        moj_organizer.dodaj_kod_rabatowy()
    if x == '4':
        moj_organizer.wyswietl_notatke()
    if x == '5':
        moj_organizer.wyswietl_wizytowke()
    if x == '6':
        moj_organizer.wyswietl_kod_rabatowy()
    if x == '0':
        break
    else:
        print('Wybrana opcja nie istnieje.\n')
