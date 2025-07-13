import base64
import os
import time
import json
from curl_cffi import requests
import sys
from time import sleep
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

def banner():
    # Clear console screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')
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
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'HVH{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://hohiepvn.x10.mx/key/van-thang-vip.php?key={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    try:
        token = "667294c6bf2cd922507983c4"
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():

    try: 
        keydis = requests.get('https://raw.githubusercontent.com/shopaccrandom/md/refs/heads/main/modun_setup/modun_0368tedj7bzxkn3cevtp/nodun_28sr2ocxwnerfkr4dnvs.txt').text.strip()
    except:
        print('lỗi khi tạo key trên discord')
        keydis = None
    
    try:
        with open("key.txt", "r", encoding="utf-8") as file:
            keydiscord = file.read()
    except:
        ip_address = get_ip_address()
        display_ip_address(ip_address)

    if ip_address or (keydis and keydis == keydiscord):
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mTool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")
                return

            # First prompt for choice
            print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 1 Để Lấy Key (Free) hoặc 2 Để Nhập Key ADMIN \033[1;33m")
            try:
                choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập lựa chọn: ")
                print("\033[97m════════════════════════════════════════════════")
                if choice not in ["1", "2"]:
                    print("Vui lòng nhập số hợp lệ (1 hoặc 2).")
                    return
            except KeyboardInterrupt:
                print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                sys.exit()

            if choice == "2":
                while True:
                    try:
                        keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mNhập Key ADMIN: \033[1;32m')
                        if keydis and keynhap == str(keydis):
                            with open("file.txt", "w", encoding="utf-8") as file:
                                file.write(keynhap)
                            print('Key ADMIN Đúng Mời Bạn Dùng Tool')
                            sleep(2)
                            luu_thong_tin_ip(ip_address, keynhap, datetime.now().replace(hour=23, minute=59, second=0, microsecond=0))
                            return
                        else:
                            print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mKey ADMIN Sai, Vui Lòng Nhập Lại!')
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

           
            while True:
                url, key, expiration_date = generate_key_and_url(ip_address)
                with ThreadPoolExecutor(max_workers=2) as executor:
                    yeumoney_future = executor.submit(get_shortened_link_phu, url)
                    yeumoney_data = yeumoney_future.result()
                    if yeumoney_data and yeumoney_data.get('status') == "error":
                        print(yeumoney_data.get('message'))
                        return
                    else:
                        link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                        print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mLink Để Vượt Key Là \033[1;36m:', link_key_yeumoney)

                    start_time = time.time()  # Record the start time
                    try:
                        keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mKey Đã Vượt Là: \033[1;32m')
                        elapsed_time = time.time() - start_time
                        if elapsed_time < 60:
                            print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCó hành vi bypass! Vui lòng dùng link mới.')
                            continue  # Automatically generate new link
                        if keynhap == key or (keydis and keynhap == str(keydis)):
                            with open("file.txt", "w", encoding="utf-8") as file:
                                file.write(keydis if keydis else keynhap)
                            print('Key Đúng Mời Bạn Dùng Tool')
                            sleep(2)
                            luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                            return
                        else:
                            print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:', link_key_yeumoney)
                            start_time = time.time()  # Reset start time for next attempt
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

if __name__ == '__main__':
    if os.path.exists("ch.txt"):
        os.remove("ch.txt")
        main()
    else:
        print('MÀY LÀM ĐC GÌ PHA ĐẤY ??? =))')
        exit()
    
while True:
    try:
        url = 'https://quanlytoolhvh.elementfx.com/tool/hvhtool.py'
        response = requests.get(url, verify=False)
        #response.encoding = 'utf-8'
        exec(response.text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
        sys.exit()
