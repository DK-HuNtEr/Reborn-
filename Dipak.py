
import os

try:
    import requests
except:
    os.system('python -m pip install requests')
try:
    import fake_email
except:
    os.system('python -m pip install fake_email')
    os.system('xdg-open https://chat.whatsapp.com/GjKY8C8AMhNJLwhKzCBQtr')
try:
    import faker
except:
    os.system('python -m pip install faker')
import requests
import random
import string
import hashlib
import json
from faker import Faker
from bs4 import BeautifulSoup
from fake_email import Email
import os
import re
import sys
import time
from datetime import datetime
green = '\x1b[1;92m'
yellow = '\x1b[1;93m'
normal = '\x1b[0m'


#------------[ WARNA-COLOR ]--------------#
status_color = '\033[1;32m'  # Green color
random_status = random.choice(['Online', 'Active', 'Busy', 'Away', 'Do Not Disturb'])

run_count = 0  # Initialize run count

logo = f"""
\033[1;37m
   _____      _                       
 |  __ \    | |                      
 | |__) |___| |__   ___  _ __ _ __   
 |  _  // _ \ '_ \ / _ \| '__| '_ \  
 | | \ \  __/ |_) | (_) | |  | | | | 
 |_|  \_\___|_.__/ \___/|_|  |_| |_|    \x1b[38;5;196mXD\x1b[37m
                                                                              
\033[1;37m=============================================
\033[1;37m [+]Owner   : \033[32mReborn\033[1;37m
\033[1;37m [+]Facebook: {status_color} Reborn Bëb{status_color}Uchida
\033[1;37m [+]STATUS  : {status_color}{random_status}\033[1;37m
\033[1;37m [+]Github  : \033[33mAuto Create\033[1;37m       
\033[1;37m [+]Version : 0.1
\033[1;37m [+]Run Count: {run_count}
\033[1;37m============================================="""

def linex():
    print('\033[1;37m=============================================')

def clear():
    os.system('clear')
    print(logo)
    
def ua():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/2.3.5;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = a+b
	return ua
def ua1():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua1 = a+b
	return ua1
def ua2():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua2 = a+b
	return ua2
def ua3():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua3 = a+b
	return ua3
def ua4():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua4 = a+b
	return ua4
def ua5():
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(11,80))+'.0.0.'+str(random.randrange(9,49))+'.'+str(random.randint(11,77)) +";FBBV/"+str(random.randint(11111111,99999999))+";"
	b = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N770F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
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
def lock_checker(id):
    try:
        req = requests.get(f'https://graph.facebook.com/{id}/picture?type=normal').text
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Locked'
    except Exception as e:
        print(f'[×] Error checking account status: {e}')
        return 'Error'

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def register_facebook_account(password, first_name, last_name, birthday):
    session = requests.Session()
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    email = f"{first_name.lower()}{random.randint(1000,9999)}@exdonuts.com"
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
    api_url = 'https://b-api.facebook.com/method/user.register'
    
    headers = {'User-Agent': ua()}
    response = requests.post(api_url, data=req, headers=headers)
    reg = response.json()
    id = reg.get('new_user_id')
    token = reg.get('session_info', {}).get('access_token')
    
    if id:
        check = lock_checker(id)
        if 'Locked' in check:
            print('id locked')
        else:
            print('sleeping mode active')
            time.sleep(5)
            try:
                cod = Email(em["session"]).inbox()
                code = re.search('(\d+)', str(cod['topic'])).group(1)
            except:
                code = 'code not found'
            if code:
                print(f'''
[♦] ACCOUNT IS LIVE
[♦] EMAIL    : \033[92;32m{email}
[♦] USER-ID : \033[92;32m{id}
[♦] PASSWORD :\033[92;32m {password}
[♦] NAME :\033[92;1m {first_name} {last_name}
[♦] BIRTHDAY :\033[92;1m {birthday}
''')
            
.,....hhyhyhuururuurur          
                # Saving cookies to a file
                cookies = session.cookies.get_dict()
                cookie_str = "; ".join([f"{key}={value}" for key, value in cookies.items()])
                with open("/sdcard/SUCCESS-OK-ID.txt", "a") as f:
                    f.write(f"{id}|{password}|{cookie_str}\n")
                
                print(f"Cookies saved for account {id}")
            else:
                pass
    else:
        print('account disabled try again')
        

if __name__ == '__main__':
    fake = Faker()
    os.system('clear')
    print(logo)
    num_accounts = int(input("Enter the number of accounts you want to create: "))
    for _ in range(num_accounts):
        password = 'SAMI-143'
        first_name = fake.first_name()
        last_name = fake.last_name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        print('creating account on process')
        register_facebook_account(password, first_name, last_name, birthday)
