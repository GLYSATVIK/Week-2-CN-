import ftplib
import io
import logging
import uuid
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ftp_test_dlptest")

HOST = "ftp.dlptest.com"
USER = "dlpuser"
PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"
FILENAME = f"dlp_test_{uuid.uuid4().hex[:8]}.txt"
DATA = f"Test from ftp_test_dlptest.py at {time.strftime('%Y-%m-%d %H:%M:%S')}\n".encode('utf-8')

def main():
    ftp = ftplib.FTP()
    try:
        logger.info("Connecting to %s", HOST)
        ftp.connect(HOST, 21, timeout=15)
        ftp.login(USER, PASS)
        logger.info("Logged in as %s", USER)
    except Exception as e:
        logger.exception("Failed to connect or login: %s", e)
        return

    try:
        bio = io.BytesIO(DATA)
        logger.info("Uploading %s ...", FILENAME)
        ftp.storbinary(f"STOR {FILENAME}", bio)
        logger.info("Upload successful")
    except Exception as e:
        logger.exception("Upload failed: %s", e)
        ftp.quit()
        return

    try:
        listing = ftp.nlst()
        logger.info("Directory listing: %s", listing)
        if FILENAME in listing:
            logger.info("%s found on server", FILENAME)
    except Exception as e:
        logger.warning("Could not list directory: %s", e)

    try:
        buf = io.BytesIO()
        logger.info("Downloading %s ...", FILENAME)
        ftp.retrbinary(f"RETR {FILENAME}", buf.write)
        downloaded = buf.getvalue()
        if downloaded == DATA:
            logger.info("Downloaded content matches uploaded content")
        else:
            logger.warning("Content mismatch!")
    except Exception as e:
        logger.exception("Download failed: %s", e)

    try:
        ftp.quit()
    except Exception:
        ftp.close()

if __name__ == "__main__":
    main()
