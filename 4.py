
import socket
import dns.resolver
import logging
from datetime import datetime

LOGFILE = "dns_queries.log"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("dns_test")

def log_to_file(s: str):
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(s + "\n")

def query_records(domain: str):
    records = {}
    resolver = dns.resolver.Resolver()

    try:
        answers = resolver.resolve(domain, "A")
        records["A"] = [r.to_text() for r in answers]
    except Exception as e:
        logger.warning("A record lookup failed: %s", e)
        records["A"] = []

    try:
        answers = resolver.resolve(domain, "MX")
        records["MX"] = [r.to_text() for r in answers]
    except Exception as e:
        logger.warning("MX lookup failed: %s", e)
        records["MX"] = []
    try:
        answers = resolver.resolve(domain, "CNAME")
        records["CNAME"] = [r.to_text() for r in answers]
    except Exception as e:

        logger.info("CNAME lookup: %s", e)
        records["CNAME"] = []

    return records

def main():
    domain = input("Enter domain to query (e.g. example.com): ").strip()
    ts = datetime.utcnow().isoformat() + "Z"
    log_to_file(f"=== DNS Query at {ts} for {domain} ===")

    try:
        ip = socket.gethostbyname(domain)
        logger.info("Resolved %s -> %s", domain, ip)
        log_to_file(f"A (system): {ip}")
    except Exception as e:
        logger.warning("System resolve failed: %s", e)
        log_to_file(f"A (system): FAILED - {e}")

    recs = query_records(domain)
    logger.info("Records: %s", recs)
    log_to_file(f"A records: {recs.get('A')}")
    log_to_file(f"MX records: {recs.get('MX')}")
    log_to_file(f"CNAME records: {recs.get('CNAME')}")

    logger.info("All DNS query results appended to %s", LOGFILE)
    print("Done — check", LOGFILE)

if __name__ == "__main__":
    main()
