import sys,os,time


if len(sys.argv) < 2 : 
    print(f"Usage:python3 target_checker.py <filename>")
    sys.exit()

filename = sys.argv[1]

if not  os.path.exists(filename):
    print(f"ERROR: Target file '{filename}' does not exist on the disk! ")
    sys.exit()

print(f"Target file '{filename}' found! Initializing verification.... ")
time.sleep(2)

with open(filename,"r") as file:
    for line in file:
        strip = line.strip()
        print(f"TARGET HOST: {strip}")

        

