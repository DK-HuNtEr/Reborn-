# ====== CREATED BY DIP_AK======
import os
import random
import string
import hashlib
import re
import time
from datetime import datetime
from faker import Faker
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

try:
    import requests
except:
    os.system('python -m pip install requests')
    import requests

try:
    from bs4 import BeautifulSoup
except:
    os.system('python -m pip install beautifulsoup4')
    from bs4 import BeautifulSoup

try:
    from fake_email import Email
except:
    os.system('python -m pip install fake_email')
    from fake_email import Email

# ====== ASCII ART ======

# ------------[ COLORS ]-------------- #
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RESET = '\033[0m'
WHITE = '\033[1;37m'

# ------------[ BANNER ]-------------- #
run_count = 0
status_list = ['Online', 'Active', 'Busy', 'Away', 'Do Not Disturb']
random_status = random.choice(status_list)

logo = f"""
{WHITE}
   _____      _                       
  |  __ \\    | |                      
  | |__) |___| |__   ___  _ __ _ __   
  |  _  // _ \\ '_ \\ / _ \\| '__| '_ \\  
  | | \\ \\  __/ |_) | (_) | |  | | | | 
  |_|  \\_\\___|_.__/ \\___/|_|  |_| |_|   {YELLOW}XD{WHITE}

=============================================
[+] Owner    : {GREEN}Dipak{WHITE}
[+] Facebook : {GREEN}Reborn Bëb {WHITE}
[+] Status   : {GREEN}{random_status}{WHITE}
[+] Github   : {YELLOW}Auto Create{WHITE}
[+] Version  : 0.1
[+] Run Count: {run_count}
=============================================
"""

# ------------[ HELPERS ]-------------- #
def clear():
    os.system('clear')
    print(logo)

def linex():
    print(WHITE + '=' * 45)


def print_banner():
    print(Fore.CYAN + """
  _____           _        _                      
 |  ___|__   ___ | | _____| |_ ___  _ __ ___ ___ 
 | |_ / _ \ / _ \| |/ / _ \ __/ _ \| '__/ __/ _ \\
 |  _| (_) | (_) |   <  __/ || (_) | | | (_|  __/
 |_|  \___/ \___/|_|\_\___|\__\___/|_|  \___\___|
    """)
    print(Fore.YELLOW + "="*60)
    print(Fore.GREEN + "Facebook Account Creator".center(60))
    print(Fore.YELLOW + "="*60 + "\n")

# ====== USER AGENT GENERATOR ======
def ua1():
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
    b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua1 = a+b
    return ua1

def ua2():
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
    b = "[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = a+b
    return ua2

def ua3():
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
    b = "[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235247;FBDM/{density=3.0,width=1080,height=2132};FBLC/en_US;FBRV/235412020;FBCR/airtel;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = a+b
    return ua3

def ua4():
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
    b = "[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851411;FBDM/{density=3.0,width=1080,height=2118};FBLC/en_US;FBRV/199646485;FBCR/Jio 4G;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1951;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua4 = a+b
    return ua4

def ua5():
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
    b = "[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Vi India;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = a+b
    return ua5

def ua():
    p1 = ua1()
    p2 = ua2()
    p3 = ua3()
    p4 = ua4()
    p5 = ua5()
    ua = random.choice([p1,p2,p3,p4,p5])
    return ua

# ====== EMAIL GENERATOR ======
def generate_random_email():
    domains = ["yandex.com", "mail.com", "tutanota.com", "gmail.com", "outlook.com"]
    prefix = f"user{random.randint(1000, 9999)}{random.choice(string.ascii_lowercase)}"
    domain = random.choice(domains)
    return f"{prefix}@{domain}"

# ====== LOCK CHECK ======
def lock_checker(uid):
    try:
        r = requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal', timeout=10)
        return 'Active' if 'Photoshop' in r.text else 'Locked'
    except:
        return 'Error'

# ====== RANDOM STRING ======
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ====== REGISTER FUNCTION ======
def register_facebook_account(password, first_name, last_name, birthday, email):
    session = requests.Session()
    
    headers = {'User-Agent': ua()}
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'US',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    response = session.post('https://b-api.facebook.com/method/user.register', data=req, headers=headers)
    try:
        reg = response.json()
        uid = reg.get('new_user_id')
        if uid:
            status = lock_checker(uid)
            if status == 'Active':
                time.sleep(5)
                try:
                    inbox = Email(email).inbox()
                    code = re.search(r'(\d{5})', str(inbox['topic'])).group(1)

                    
                    confirm_url = 'https://b-api.facebook.com/method/auth.confirm_email'
                    payload = {
                        'email': email,
                        'code': code,
                        'format': 'json',
                        'access_token': reg.get('session_info', {}).get('access_token', '')
                    }
                    confirm = session.post(confirm_url, data=payload, headers=headers)
                    print(Fore.GREEN + f"[✓] Verified: {email} with code {code}")
                except:
                    code = 'Not Found'

                # Save to file
                cookie_dict = session.cookies.get_dict()
                cookie_str = '; '.join([f"{k}={v}" for k, v in cookie_dict.items()])
                with open("/sdcard/SUCCESS-OK-ID.txt", "a") as f:
                    f.write(f"{uid}|{password}|{cookie_str}\n")
                

                print(Fore.GREEN + """
╔══════════════════════════════════════════════╗
║            ACCOUNT CREATED SUCCESSFULLY      ║
╠══════════════════════════════════════════════╣""")
                print(Fore.CYAN + f"""║ {Fore.YELLOW}• EMAIL{Fore.RESET}    : {Fore.WHITE}{email.ljust(36)}║
║ {Fore.YELLOW}• UID{Fore.RESET}      : {Fore.WHITE}{str(uid).ljust(36)}║
║ {Fore.YELLOW}• PASSWORD{Fore.RESET} : {Fore.WHITE}{password.ljust(36)}║
║ {Fore.YELLOW}• NAME{Fore.RESET}     : {Fore.WHITE}{(first_name + ' ' + last_name).ljust(36)}║
║ {Fore.YELLOW}• BIRTHDAY{Fore.RESET} : {Fore.WHITE}{str(birthday).ljust(36)}║
║ {Fore.YELLOW}• CODE{Fore.RESET}     : {Fore.WHITE}{str(code).ljust(36)}║
╚══════════════════════════════════════════════╝
""")
                return True
            else:
                print(Fore.RED + '[✗] ID Locked')
                return False
        else:
            print(Fore.RED + '[✗] Account Disabled or Failed')
            return False
    except Exception as e:
        print(Fore.RED + f'[✗] Error: {e}')
        return False

# ====== GET EMAIL INPUT ======
def get_email_input(i, total):
    print(Fore.YELLOW + "\n" + "="*60)
    print(Fore.CYAN + f"ACCOUNT {i+1} OF {total}".center(60))
    print(Fore.YELLOW + "="*60)
    
    choice = input(Fore.GREEN + "\nUse random email (1) or input your own (2)? [1/2]: ").strip()
    
    if choice == "1":
        email = generate_random_email()
        print(Fore.MAGENTA + f"\nUsing random email: {email}")
        return email
    elif choice == "2":
        while True:
            email = input(Fore.BLUE + "\nEnter email address: ").strip()
            if "@" in email and "." in email.split("@")[1]:
                return email
            else:
                print(Fore.RED + "Invalid email format. Please enter a valid email address.")
    else:
        print(Fore.RED + "Invalid choice. Using random email by default.")
        return generate_random_email()

# ====== MAIN ======
if __name__ == '__main__':
    os.system('clear')
    print(logo)
    
    fake = Faker()
    manual_passwords = [
        "ram@krishna", "ram123$", "maya@123", "vimthapa@1234", "ganesh123@", "pokhara@123",
        "maya123", "asmita@123", "sagarmatha@122", "sanu@123", "nepal@123", "dharan@123@",
        "maya@123", "parbatimagar@123", "Nepal123", "sunitakc1234", "prabin@1234"
    ]
    
    try:
        num = int(input(Fore.BLUE + '\nEnter number of accounts to create: '))
    except:
        num = 1

    for i in range(num):
        # Get email for this account
        email = get_email_input(i, num)
        
        # Generate account details
        fname = fake.first_name()
        lname = fake.last_name()
        bday = fake.date_of_birth(minimum_age=18, maximum_age=28)
        
        if i < len(manual_passwords):
            password = manual_passwords[i]
        else:
            password = random.choice(manual_passwords)
        
        # Create account
        success = register_facebook_account(password, fname, lname, bday, email)
        
        
        if i < num - 1:
            cont = input(Fore.CYAN + "\nCreate another account? (y/n): ").strip().lower()
            if cont != 'y':
                break
