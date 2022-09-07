password = input("Podaj hasło: ")
security_checklist = ""
            
chars = ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","ń","o","ó","p","q","r","s","ś","t","u","v","w","x","y","z","ź","ż"]

capital_chars = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'Ś', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ź', 'Ż']

special_chars = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

for char in chars:
    if char in password:                # sprawdza, czy mała litera
        security_checklist += "1"       # znajduje się w 'password'  
        
for capital_char in capital_chars:
    if capital_char in password:        # sprawdza, czy duża litera
        security_checklist += "2"       # znajduje się w 'password'
        
for special_char in special_chars:
    if special_char in password:        # sprawdza, czy znak specjalny
        security_checklist += "3"       # znajduje się w 'password'
        
for char in password:
    if char.isspace():                  # sprawdza, czy spacja NIE
        security_checklist += "4"       # znajduje się w 'password'        
        
if len(password) >= 8:                  # sprawdza, czy 'password'
    security_checklist += "5"           # jest większe lub równe 8
    
if "1" not in security_checklist:
    print("Hasło powinno mieć minimum jedną małą literę!")
if "2" not in security_checklist:
    print("Hasło powinno mieć minimum jedną dużą literę!")
if "3" not in security_checklist:
    print("Hasło powinno mieć minimum jeden znak specjalny!")
if "4" in security_checklist:
    print("Hasło NIE powinno mieć spacji!")
if "5" not in security_checklist:
    print("Hasło powinno składać się z minimum 8 znaków")
if "1" in security_checklist and "2" in security_checklist and "3" in security_checklist and "5" in security_checklist and "4" not in security_checklist:
    print("Hasło bezpieczne!")
