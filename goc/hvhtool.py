try :
  from time import strftime
  from datetime import datetime, timedelta
  import re,os,sys
  from curl_cffi import requests
  from datetime import date
  from time import sleep 
  from datetime import datetime 
except ImportError:
  os.system("pip install requests")
  os.system("pip install art")
  os.system("pip install colorama")
  os.system("pip install tabulate")
  os.system("pip install bs4")
  os.system("pip install pystyle")
  os.system("pip install curl_cffi")
  os.system("pip cài đặt random2")
  os.system("pip cài đặt selenium")
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= trang + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
import os,sys
os.system('cls')
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
blue = '\033[94m'
cyan = '\033[96m'
purple = '\033[95m'
bold = '\033[1m'
reset = '\033[0m'
def loading_bar():
    os.system("clear" if os.name != "nt" else "cls")
    title = f"{bold}{cyan}🚀 Đang Loading Vào BETAPCODE"
    spinner = ["◐", "◓", "◑", "◒"]
    for i in range(100):
        spin = spinner[i % len(spinner)]
        bar = '█' * (i // 2) + '-' * ((100 - i) // 2)
        sys.stdout.write(f"\r{title} {purple}[{spin}] {i+1}% [{bar}]{reset}")
        sys.stdout.flush()
        sleep(0.01)
    os.system("clear" if os.name != "nt" else "cls")
loading_bar()
banner1=f'''
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║ * Tool chạy trên cmd,codespace,teramux(ubuntu) (teramux thường không chạy đc)
\033[1;32m║ * Về Phía lỗi tool thì tool đẫ được test trước khi phát hành 
\033[1;32m║ * Nếu có lỗi thì liên hệ AD hoặc cài lại python đúng phiên bản
\033[1;32m║ * tool reg toktok có căn mới chạy đc
\033[1;39m└──────────────────────────────────────────────────────────────┘'''
banner = f""" 
\033[0;31m██╗░░██╗██╗░░░██╗██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;32m██║░░██║██║░░░██║██║░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;31m███████║╚██╗░██╔╝███████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;32m██╔══██║░╚████╔╝░██╔══██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;31m██║░░██║░░╚██╔╝░░██║░░██║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;32m╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────── Bé Tập Code TOOL ──────────────────────┐
\033[1;32m║   \033[1;39mTOOL BY\033[1;32m            :  Bé Tập Code                          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER\033[1;32m           :  HVHTOOL                         \033[1;32m     ║
\033[1;32m║   \033[1;39mYOTUBE_LINK\033[1;32m        :  https://www.youtube.com/@HVHTOOL\033[1;32m     ║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""


print(banner1)
#os.system("")

# màu


ngay=int(strftime('%d'))
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
os.system('cls')
print(banner)
print('Chạy tiến trình')



######################################################################################
os.system('cls')
print(banner)
os.system('cls')
print(banner)
### nhap key


os.system("cls")
time=datetime.now().strftime("%H:%M:%S")
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
os.system('cls')
print(banner)
print(banner1)
print('Chạy tiến trình')
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║ \033[1;33m GOLIKE PC|IOS|ANR\033[1;37m  ║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1.1 \033[1;31m] \033[1;32mTool GOLIKE AutoLinkedin\033[1;31m[\033[1;33m PC|CODESPACES\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1.2 \033[1;31m] \033[1;32mTool GOLIKE INSTAGRAM AUTO RANDOM User_Agent \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1.3 \033[1;31m] \033[1;32mTool GOLIKE X \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1.4 \033[1;31m] \033[1;32mTool GOLIKE Theads \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1.5 \033[1;31m] \033[1;32mTool GOLIKE TIKTOK \033[1;31m[\033[1;33m termux\033[1;31m] ")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 1.6 \033[1;31m] \033[1;32mTool GOLIKE LAZADA \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33m TOOL TTC  \033[1;37m          ║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 2.1 \033[1;31m] \033[1;32mTool TTC INSTAGRAM RANDOM User_Agent \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33m TOOL TDS  \033[1;37m          ║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m✨ 3.1 \033[1;31m] \033[1;32mTool TDS_TIKTOK \033[1;31m[\033[1;33m PC|CODESPACES|termux\033[1;31m]")
print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

chucnang = {
    1.1: 'AutoLinkedin_PC.py',
    1.2: 'AUTOGOLIKEIG_V1.py',
    1.3: 'AUTO-X_PC.py',
    1.4: 'AutoTheads.py',
    1.5: 'goliketiktok.py',
    1.6: 'lazada.py',
    2.1: 'TTCIG_user-agent.py',
    3.1: 'Tool TDS TikTok.py'
}
nhap = float(input('\033[1;31m[\033[1;37mBé Tập Code\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if nhap in [1.1,1.2,1.3,1.4,1.5,1.6]:
    base_url = "https://raw.githubusercontent.com/Hoanghuy200/Hoanghuy/refs/heads/main/tool-cung-cap/golike/"
    url = base_url + chucnang[nhap]
    response = requests.get(url, verify=False)
    #response.encoding = 'utf-8'
    exec(response.text)
elif nhap in [2.1]:
    base_url = "https://raw.githubusercontent.com/Hoanghuy200/Hoanghuy/refs/heads/main/tool-cung-cap/ttc/"
    url = base_url + chucnang[nhap]
    response = requests.get(url, verify=False)
    #response.encoding = 'utf-8'  # Set encoding to UTF-8
    exec(response.text)
elif nhap in [3.1]:
    base_url = "https://raw.githubusercontent.com/Hoanghuy200/Hoanghuy/refs/heads/main/tool-cung-cap/tds/"
    url = base_url + chucnang[nhap]
    response = requests.get(url, verify=False)
    #response.encoding = 'utf-8'  # Set encoding to UTF-8
    exec(response.text)
if nhap == 00 :
  exit()
else :
    exit()