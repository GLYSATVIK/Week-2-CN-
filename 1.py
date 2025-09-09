import requests

def http_test():
    try:
        url = "https://httpbin.org"
        r1 = requests.get(url+"/get"); r2 = requests.post(url+"/post", data={"k":"v"})
        print("GET", r1.status_code, r1.headers, r1.text[:100])
        print("POST", r2.status_code, r2.headers, r2.text[:100])
    except Exception as e: print("Error:", e)

http_test()
