#!/usr/bin/env python
import subprocess
import time

CMD = 'imapsync --nolog --host1 172.30.249.111 --user1 D03\\\\NebehayG --password1 dO9dmG0LE1 --host2 imap.googlemail.com --port2 993 --user2 gnebehay@gmail.com --password2 Bahmei9A --ssl1 -ssl2 --folder INBOX --delete1'

if __name__ == '__main__':
    while True:
        subprocess.call(CMD, shell=True)
        time.sleep(600)


