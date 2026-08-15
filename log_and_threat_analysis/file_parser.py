import time


print("Scanning file ! ")
time.sleep(2)


def parse_log_file(file_log):
    threat = []
    with open(file_log,"r") as file:
        for line in file:
            if "CRITICAL" in line or "WARNING" :
              threat.append(line.strip())
    return threat


result = parse_log_file("server.log") 



print("------flagged threats -------")
print(result)

