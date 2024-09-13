import argparse
import subprocess
import threading
import sys
import signal
from colorama import Fore, init, Style

# Initialize colorama
init()

# Define banner
banner = """
░██████╗██╗░░██╗░█████╗░░█████╗░████████╗  ░█████╗░██╗░░░██╗████████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██║░░░██║╚══██╔══╝
╚█████╗░███████║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░
░╚═══██╗██╔══██║██║░░██║██║░░██║░░░██║░░░  ██║░░██║██║░░░██║░░░██║░░░
██████╔╝██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░  ╚█████╔╝╚██████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░░░░╚═╝░░░
"""

def display_banner():
    print(Fore.CYAN + banner + Style.RESET_ALL)

def run_command(command, output_lines, interrupted):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            output_lines.append(line.strip())
            print(line.strip())
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
    except KeyboardInterrupt:
        interrupted[0] = True

def find_subdomains(url, output_file=None):
    tools = {
        "subfinder": ["subfinder", "-d", url],
        "assetfinder": ["assetfinder", "--subs-only", url]
    }
    
    all_subdomains = set()
    interrupted = [False]  # To handle interruption
    
    def run_tool(tool_name, command):
        nonlocal all_subdomains
        output_lines = []
        run_command(command, output_lines, interrupted)
        if not interrupted[0]:
            for line in output_lines:
                subdomain = line.strip()
                if subdomain and subdomain not in all_subdomains:
                    all_subdomains.add(subdomain)
                    print(subdomain)

    threads = []
    for tool, command in tools.items():
        thread = threading.Thread(target=run_tool, args=(tool, command))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    if output_file:
        with open(output_file, 'w') as f:
            for subdomain in sorted(all_subdomains):
                f.write(subdomain + '\n')
        print(f"Subdomains saved to {output_file}")
    
    if interrupted[0]:
        print("Execution was interrupted!")

def crawl(url, output_file=None):
    tools = {
        "katana": ["katana", "-u", url],
        "gau": ["gau", url]
    }

    outputs = {}
    interrupted = [False]  # To handle interruption

    def run_tool(tool_name, command):
        output_lines = []
        run_command(command, output_lines, interrupted)
        outputs[tool_name] = output_lines

    threads = []
    for tool, command in tools.items():
        thread = threading.Thread(target=run_tool, args=(tool, command))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    if output_file:
        with open(output_file, 'w') as f:
            for tool, output_lines in outputs.items():
                f.write(f"Output from {tool}:\n")
                for line in output_lines:
                    f.write(line + '\n')
                f.write("\n")
        print(f"Crawling results for {tool} saved to {output_file}")
    
    if interrupted[0]:
        print("Execution was interrupted!")

def run_directory_bruteforcing(url, wordlist, threads):
    command = [
        'python3', 'directory_tools/directory.py',
        '-u', url,
        '-w', wordlist,
        '-t', str(threads)
    ]
    subprocess.run(command)

def handle_interrupt(signum, frame):
    print("\nInterrupted! Saving current results...")
    sys.exit(0)

# Set up signal handler for interrupts
signal.signal(signal.SIGINT, handle_interrupt)

if __name__ == "__main__":
    # Display banner
    display_banner()
    
    # Parse arguments
    parser = argparse.ArgumentParser(description="Main script for handling different tasks.")
    parser.add_argument("-u", "--url", help="The base URL to process.")
    parser.add_argument("-o", "--output", help="File to save the results.")
    parser.add_argument("-s", "--scan", action='store_true', help="Trigger subdomain scan.")
    parser.add_argument("--crawl", action='store_true', help="Trigger URL crawling with both tools.")
    parser.add_argument("-db", "--directory-bruteforce", action='store_true', help="Run directory brute-forcing.")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file for directory brute-forcing.")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads for directory brute-forcing (default: 10).")
    
    args = parser.parse_args()

    if args.scan:
        if not args.url:
            print("Error: URL is required for subdomain scanning.")
            sys.exit(1)
        print("Finding subdomains...")
        find_subdomains(args.url, args.output)
        print("Subdomain discovery completed.")
    elif args.crawl:
        if not args.url:
            print("Error: URL is required for crawling.")
            sys.exit(1)
        print("Crawling URL with katana and gau...")
        crawl(args.url, args.output)
    elif args.directory_bruteforce:
        if not args.url or not args.wordlist:
            print("Error: URL and wordlist are required for directory brute-forcing.")
            sys.exit(1)
        run_directory_bruteforcing(args.url, args.wordlist, args.threads)
    else:
        print("Error: No valid option provided. Use -s for scanning, --crawl for crawling, or -db for directory brute-forcing. Output file is optional.")
