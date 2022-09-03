from pydoc import plain

# program pobiera od użytkownika tekst,
# analizując ilość słów i ich średnią długość określa złożoność

text = input("Podaj tekst: ")

flt = filter(str.isalnum,text) #filtruje tylko litery i cyfry
plain_text = "".join(flt) #do pustego stringa przepisuje tylko litery i cyfry

words = len(text.split())

division = len(plain_text) / words
print("Słowa w Twoim tekście mają średnio",division,"znaków.")
