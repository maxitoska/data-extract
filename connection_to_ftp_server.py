import os
from ftplib import FTP_TLS
import time
from dotenv import load_dotenv


def set_up_ftp_tls_server_connection(current_datetime, csv_file):
    load_dotenv()
    ftp_host = os.getenv("ftp_host")
    ftp_username = os.getenv("ftp_username")
    ftp_password = os.getenv("ftp_password")

    ftp = FTP_TLS()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_host)
    ftp.login(user=ftp_username, passwd=ftp_password)
    print(f"{ftp.getwelcome()}")
    ftp.storbinary(f"STOR _Database_{current_datetime}.csv", open(csv_file, "rb"))
    print(ftp.dir())
    ftp.close()
    time.sleep(10)
