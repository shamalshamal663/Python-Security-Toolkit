import os , sys , os ,requests


if len(sys.argv) < 3 :
    print(f"Usage : python3 dir_fuzzer.py <target_base_url> <wordlist.txt>")
    sys.exit()

base_url = sys.argv[1].rstrip("/")
wordlist_file =sys.argv[2]

if not os.path.exists(wordlist_file):
    print(f"ERROR: file {wordlist_file} not on the disc")
    sys.exit()

def fuzz_endpoints(base_url,wordlist_file,output_file="discover_route.txt"):
    with open(wordlist_file,"r") as wfile:
        with open(output_file,"w") as ofile:
            print(f"[SCANNING START] Fuzzing target:{base_url} using '{wordlist_file}....")
            for line in wfile:
                endpoint = line.strip()
                url = f"{base_url}/{endpoint}"
                try:
                    response = requests.get(url,timeout=5)
                    if response.status_code == 200:
                        print(f"[200 ok] Found Active Route:/{endpoint}")
                        ofile.write(f"[200 ok]{url}\n")
                    elif response.status_code == 404:
                        print(f"[404]/{endpoint}")
                    else:
                        print(f"{response.status_code}]/{endpoint}")
                except requests.exceptions.RequestException as e :
                    print(f"[ERROR] Failed to reach / {endpoint}:{e}")
            print(f"[SCAN COMPLETE] Discovered routes saved to '{output_file}'")



fuzz_endpoints(base_url,wordlist_file)
                                    
    
