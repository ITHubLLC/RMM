import socket

domains = [
    "zinfandel-ips.centrastage.net",
    "tunnel-ips.centrastage.net"
]

output_file = "RMM.txt"

with open(output_file, "w") as f:
    for domain in domains:
        ip_addresses = socket.gethostbyname_ex(domain)[2]
        for ip in ip_addresses:
            f.write(f"{ip}\n")
