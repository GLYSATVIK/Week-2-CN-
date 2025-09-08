import requests
import logging
import json
from pprint import pprint


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("http_test")

def pretty_print_response(resp: requests.Response):
    print("\n--- RESPONSE ---")
    print("Status code:", resp.status_code)
    print("Headers:")
    pprint(dict(resp.headers))
    print("Body:")

    try:
        pprint(resp.json())
    except ValueError:
        print(resp.text[:1000])  

def main():

    get_url = "https://api.chucknorris.io/jokes/random"
    try:
        logger.info("Sending GET to %s", get_url)
        r = requests.get(get_url, timeout=10)
        pretty_print_response(r)
    except requests.RequestException as e:
        logger.exception("GET request failed: %s", e)

    post_url = "https://httpbin.org/post"
    payload = {
        "message": "hello from http_test.py",
        "value": 42,
        "crazy": True
    }
    headers = {"User-Agent": "http-test-script/1.0", "Content-Type": "application/json"}
    try:
        logger.info("Sending POST to %s with payload: %s", post_url, payload)
        r2 = requests.post(post_url, json=payload, headers=headers, timeout=10)
        pretty_print_response(r2)
    except requests.RequestException as e:
        logger.exception("POST request failed: %s", e)

if __name__ == "__main__":
    main()
