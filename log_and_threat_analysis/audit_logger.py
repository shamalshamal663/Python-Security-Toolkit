import time 

print("VALIDATING!")
time.sleep(2)


def log_security_event(event_message,filename):
    with open(filename,"a") as file:
        file.write(f"{event_message}\n")
        print(f"event logged cleanly to {filename}\n")

log_security_event("ALERT:Failed root login attempt on port 22","audit.log")
log_security_event("CRITICAL:Unauthorized file modified in /etc/passwd","audit.log")

        
