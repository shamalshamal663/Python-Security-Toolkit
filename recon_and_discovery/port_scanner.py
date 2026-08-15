import time


print("PORT SCANNER X!")  # print a welcome command of tool name 
time.sleep(2) #wait 2s after printing the welcome 



# we need to create a list of port

s_port = [80,22,21,443,3389,800]
d_port = [21,22,3389] # high risk port


#create a function to iterate through the list 

def analyze_port(port_list):
    for port in port_list:
        if port in d_port:
            print(f"WARNING! :high risk service detected in  {port}")
        else:
         print(f"OK {port} operating normally ")


analyze_port(s_port)