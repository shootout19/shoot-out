This tool is under process so it gives a false result.
# URL Scanner and Crawler

This Python script provides tools for scanning subdomains and crawling URLs using popular tools like `subfinder`, `assetfinder`, `katana`, and `gau`. The results can be displayed in the terminal or saved to a file.

## Features

- **Subdomain Scanning**: Find subdomains using `subfinder` and `assetfinder`.
- **URL Crawling**: Crawl URLs using `katana` and `gau`.
- **brute forcing** : directory brute forcing
- **Optional Output File**: Save results to a file or display them in the terminal.
- **Interrupt Handling**: Handle interruptions gracefully and save the results collected up to that point.

## Prerequisites

Make sure you have Python 3.x installed. You also need to install the required tools and Python packages.

### Required Tools

- `subfinder`
- `assetfinder`
- `katana`
- `gau`
You can usually install these tools via package managers or from their respective repositories.
# Installation
```
git clone <url>
cd shoot-out
pip3 install -r requirements.txt
```
# using Tools Installation
Installation go lang in kali `sudo apt install golang`
1. Subfinder --> `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest`
2. assetfinder --> `go install github.com/tomnomnom/assetfinder@latest`
3. katana --> `go install github.com/projectdiscovery/katana@latest`
4. gau --> `go install github.com/lc/gau@latest`

# Arguments
```

░██████╗██╗░░██╗░█████╗░░█████╗░████████╗  ░█████╗░██╗░░░██╗████████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░██║╚══██╔══╝
╚█████╗░███████║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░
░╚═══██╗██╔══██║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░
██████╔╝██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ╚█████╔╝╚██████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░░░░╚═╝░░░

usage: main.py [-h] [-u URL] [-o OUTPUT] [-s] [--crawl] [-db] [-w WORDLIST] [-t THREADS]

Main script for handling different tasks.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The base URL to process.
  -o OUTPUT, --output OUTPUT
                        File to save the results.
  -s, --scan            Trigger subdomain scan.
  --crawl               Trigger URL crawling with both tools.
  -db, --directory-bruteforce
                        Run directory brute-forcing.
  -w WORDLIST, --wordlist WORDLIST
                        Path to the wordlist file for directory brute-forcing.
  -t THREADS, --threads THREADS
                        Number of concurrent threads for directory brute-forcing (default: 10).

```

# How to use 
for finding subdomain
```
python3 main.py -u google.com -s -o output.txt

░██████╗██╗░░██╗░█████╗░░█████╗░████████╗  ░█████╗░██╗░░░██╗████████╗                                                                                        
██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░██║╚══██╔══╝                                                                                        
╚█████╗░███████║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░                                                                                        
░╚═══██╗██╔══██║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░                                                                                        
██████╔╝██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ╚█████╔╝╚██████╔╝░░░██║░░░                                                                                        
╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░░░░╚═╝░░░                                                                                        
                                                                                                                                                             
Finding subdomains...
docs.google.com
google.com
216-239-45-10.google.com
216-239-45-32.google.com
216-239-45-33.google.com
press CTRL + c
```
for crawling a web page 
```
python3 main.py -u youtube.com --crawl -o output.txt

░██████╗██╗░░██╗░█████╗░░█████╗░████████╗  ░█████╗░██╗░░░██╗████████╗                                                                                        
██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░██║╚══██╔══╝                                                                                        
╚█████╗░███████║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░                                                                                        
░╚═══██╗██╔══██║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░                                                                                        
██████╔╝██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ╚█████╔╝╚██████╔╝░░░██║░░░                                                                                        
╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░░░░╚═╝░░░                                                                                        
                                                                                                                                                             
Crawling URL with katana and gau...
https://youtube.com
https://www.youtube.com/
https://www.youtube.com/s/desktop/59ec15cc/jsbin/intersection-observer.min.vflset/intersection-observer.min.js
https://www.youtube.com/s/desktop/59ec15cc/jsbin/web-animations-next-lite.min.vflset/web-animations-next-lite.min.js
https://www.youtube.com/s/desktop/59ec15cc/jsbin/spf.vflset/spf.js
https://www.youtube.com/s/desktop/59ec15cc/jsbin/network.vflset/network.js
https://www.youtube.com/s/desktop/59ec15cc/jsbin/www-i18n-constants-en_GB.vflset/www-i18n-constants.js
https://www.youtube.com/s/desktop/59ec15cc/cssbin/www-main-desktop-watch-page-skeleton.css
https://www.youtube.com/s/desktop/59ec15cc/jsbin/custom-elements-es5-adapter.vflset/custom-elements-es5-adapter.js
https://www.youtube.com/s/desktop/59ec15cc/jsbin/www-tampering.vflset/www-tampering.js
https://www.youtube.com/s/desktop/59ec15cc/jsbin/scheduler.vflset/scheduler.js
press CTRL + c
```
for directory bruteforcing
```
python3 main.py -db -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://google.com -t 20

░██████╗██╗░░██╗░█████╗░░█████╗░████████╗  ░█████╗░██╗░░░██╗████████╗                                                                                        
██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░██║╚══██╔══╝                                                                                        
╚█████╗░███████║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░                                                                                        
░╚═══██╗██╔══██║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░                                                                                        
██████╔╝██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ╚█████╔╝╚██████╔╝░░░██║░░░                                                                                        
╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░░░░╚═╝░░░                                                                                        
                                                                                                                                                             
Found: https://google.com/# 
Found: https://google.com/images
Found: https://google.com/2006
Found: https://google.com/news
press CTRL + c
```







