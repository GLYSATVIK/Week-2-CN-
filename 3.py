from ftplib import FTP

def ftp_test():
    try:
        with open("test.txt","w") as f: f.write("Hello FTP test")

        f = FTP("ftp.dlptest.com"); f.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")
        f.storbinary("STOR test.txt", open("test.txt","rb"))
        f.retrbinary("RETR test.txt", open("out.txt","wb").write)
        f.retrlines("LIST"); f.quit()
        print("Uploaded, downloaded, listed.")
    except Exception as e: print("Error:", e)

ftp_test()
