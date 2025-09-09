import dns.resolver

def dns_lookup():
    try:
        domain = input("Enter a domain name (e.g., example.com): ").strip()
        if not domain:
            print("No domain entered.")
            return

        with open("dns.txt", "w") as f:
            f.write(f"DNS records for {domain}:\n\n")

            try:
                f.write("A Records:\n")
                for r in dns.resolver.resolve(domain, "A"):
                    f.write(f"  {r}\n")
            except:
                f.write("  No A records found.\n")

            try:
                f.write("MX Records:\n")
                for r in dns.resolver.resolve(domain, "MX"):
                    f.write(f"  {r.exchange} (priority {r.preference})\n")
            except:
                f.write("  No MX records found.\n")

            try:
                f.write("CNAME Records:\n")
                for r in dns.resolver.resolve(domain, "CNAME"):
                    f.write(f"  {r}\n")
            except:
                f.write("  No CNAME records found.\n")

        print("DNS records saved to dns.txt")

    except Exception as e:
        print("Error:", e)

dns_lookup()
