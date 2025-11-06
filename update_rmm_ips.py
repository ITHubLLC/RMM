import socket

# Domains to resolve
domains = [
    "zinfandel-ips.centrastage.net",
    "tunnel-ips.centrastage.net"
]

output_file = "RMM.txt"

with open(output_file, "w") as f:
    for domain in domains:
        try:
            ip_addresses = socket.gethostbyname_ex(domain)[2]
            f.write(f"# {domain}\n")
            for ip in ip_addresses:
                f.write(f"{ip}\n")
            f.write("\n")
        except Exception as e:
            f.write(f"# Error resolving {domain}: {e}\n\n")

print(f"Resolved IPs written to {output_file}")
