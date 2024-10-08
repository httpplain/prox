import requests
import time
import logging
import os
from yaspin import yaspin
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def http_check(PROXY_LIST_FILE):
    TEST_URL = "http://httpbin.org/ip"
    TIMEOUT = 5
    logging.basicConfig(filename='error.log', level=logging.ERROR)

    def test_proxy(proxy):
        try:
            response = requests.get(TEST_URL, proxies={'http': proxy}, timeout=TIMEOUT)
            if 100 <= response.status_code < 400:
                return proxy
        except Exception:
            pass
        return None

    def main():
        start_time = time.time()
        http_proxies = []

        with open(PROXY_LIST_FILE, 'r') as f:
            http_proxies = [line.strip() for line in f.readlines()]
        
        cpu_count = os.cpu_count()
        max_threads = cpu_count * 450
        if not max_threads:
            max_threads = 1000

        print(f"[*] Utilizing {max_threads:,} threads, calculated from your device's {cpu_count} CPU cores.")

        with yaspin().bouncingBar as sp:
            sp.text = f"Initializing threads for {PROXY_LIST_FILE}..."
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                results = []
                progress_started = False
                for result in tqdm(executor.map(test_proxy, http_proxies), total=len(http_proxies), desc="[*] Checking HTTP Proxies", ascii=" #", unit= " prox"):
                    if not progress_started:
                        sp.text = "Threads initialized."
                        sp.ok("[_OK_]")
                        sp.stop()
                        progress_started = True
                    results.append(result)

        http_valid_proxies = [proxy for proxy in results if proxy is not None]
        
        end_time = time.time()
        total_time = end_time - start_time
        total_minutes = total_time // 60
        remaining_seconds = total_time % 60
        print("[*] Total time for Execution:", f"{int(total_minutes)} minute(s) and {round(remaining_seconds, 2)} seconds")
        
        print(f"[*] Valid HTTP Proxies: {len(http_valid_proxies):,}\n")

        with open(PROXY_LIST_FILE, 'w') as f:
            for proxy in http_valid_proxies:
                f.write(proxy + '\n')
    main()
    
def https_check(PROXY_LIST_FILE):
    TEST_URL = "https://httpbin.org/ip"
    TIMEOUT = 5
    logging.basicConfig(filename='error.log', level=logging.ERROR)

    def test_proxy(proxy):
        try:
            response = requests.get(TEST_URL, proxies={'https': proxy}, timeout=TIMEOUT)
            if 100 <= response.status_code < 400:
                return proxy
        except Exception:
            pass
        return None

    def main():
        start_time = time.time()
        https_proxies = []

        with open(PROXY_LIST_FILE, 'r') as f:
            https_proxies = [line.strip() for line in f.readlines()]
        
        cpu_count = os.cpu_count()
        max_threads = cpu_count * 250
        if not max_threads:
            max_threads = 1000

        print(f"[*] Utilizing {max_threads:,} threads, calculated from your device's {cpu_count} CPU cores.")

        with yaspin().bouncingBar as sp:
            sp.text = f"Initializing threads for {PROXY_LIST_FILE}..."
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                results = []
                progress_started = False
                for result in tqdm(executor.map(test_proxy, https_proxies), total=len(https_proxies), desc="[*] Checking HTTPS Proxies", ascii=" #", unit= " prox"):
                    if not progress_started:
                        sp.text = "Threads initialized."
                        sp.ok("[_OK_]")
                        sp.stop()
                        progress_started = True
                    results.append(result)

        https_valid_proxies = [proxy for proxy in results if proxy is not None]
        
        end_time = time.time()
        total_time = end_time - start_time
        total_minutes = total_time // 60
        remaining_seconds = total_time % 60
        print("[*] Total time for Execution:", f"{int(total_minutes)} minute(s) and {round(remaining_seconds, 2)} seconds")
        
        print(f"[*] Valid HTTPS Proxies: {len(https_valid_proxies):,}")

        with open(PROXY_LIST_FILE, 'w') as f:
            for proxy in https_valid_proxies:
                f.write(proxy + '\n')
    main()

def cproxy_sources():
    return {
        "HTTP": [
            "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://api.openproxylist.xyz/http.txt",
            "https://alexa.lr2b.com/proxylist.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "https://rootjazz.com/proxies/proxies.txt",
            "https://spys.me/proxy.txt",
            "https://proxyspace.pro/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
            "https://sunny9577.github.io/proxy-scraper/proxies.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
            "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
            "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
            "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt",
            "https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
            "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt",
            "https://proxyspace.pro/http.txt",
            "https://raw.githubusercontent.com/casals-ar/proxy-list/main/http",
            "https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/main/proxies/http.txt",
            "https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt",
            "https://raw.githubusercontent.com/AGDDoS/AGProxy/master/proxies/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/Mini0001/proxylist/main/http.txt",
            "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
            "https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
            "https://raw.githubusercontent.com/Sage520/Proxy-List/main/http.txt",
            "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            
        ],
        "SOCKS4": [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
        ],
        "SOCKS5": [            
            "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global/socks5_checked.txt",
        ],
        "HTTPS": [
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
            "https://proxyspace.pro/https.txt",
            "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
            "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt"
        ]
    }
