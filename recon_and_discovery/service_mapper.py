service_lookup = {
    21: "FTP (Unencrypted File Transfer)",
    22: "SSH (Secure Shell)",
    80: "HTTP (Cleartext Web Traffic)",
    443: "HTTPS (Encrypted Web Traffic)",
    3389: "RDP (Remote Desktop Protocol)"
}

def inspect_port(port_list):
    for port in port_list:
      service_name = service_lookup.get(port,"unknown / Custom Service") 
      print(f"port {port} -> {service_name}")    

scanned_ports  = [80,22,8080,443,3389,9000]

print("SCANNING....")
inspect_port(scanned_ports)