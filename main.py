import secrets
import string
from colorama import Fore, Style

def genera_password(length=16, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    print(Fore.RED +"=== Generatore Password Sicure ==="+ Style.RESET_ALL)
    try:
        length = int(input(Fore.RED +"Lunghezza password (default 16): ") or 16 + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED +"Input non valido, uso 16 come default."+ Style.RESET_ALL)
        length = 16
    special = input(Fore.RED +"Usare caratteri speciali? (s/n, default s): "+ Style.RESET_ALL).lower() != 'n'
    pwd = genera_password(length, special)
    print(Fore.RED +"\nPassword generata:\n" + pwd + Style.RESET_ALL)

    input(Fore.RED +"\nPremi un tasto per uscire..."+ Style.RESET_ALL)

if __name__ == "__main__":
    main()
