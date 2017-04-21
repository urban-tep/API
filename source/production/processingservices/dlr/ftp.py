#!/usr/bin/python
from ftplib import FTP
import re
import time

def get_file(ftp, path, file_name, seconds):
		"""
		Downloads a file from a ftp server if its size does not change within given time in seconds
		"""
        # set bin mode, ask, wait, ask again, compare
        ftp.sendcmd("TYPE i")
        
		s1 = ftp.size(file_name)
        time.sleep(seconds)
        s2 = ftp.size(file_name)

        # download and delete if unchanged
        if s2-s1 == 0:
                ftp.retrbinary('RETR {}'.format(file_name), open('{}/{}'.format(path, file_name), 'wb').write)
                ftp.delete(file_name)

def main():
		"""
		Downloads files from a ftp server to a local directory
		Usage with crontab
		$ crontab -e
		*/5 * * * * ~/work/getAsar.py 'ASA(.*)zip' ftp.foo.de /put/xxx/in /net/sensors/bar/new 30
		"""
        if len(sys.argv) != 6:
			print('Syntax: {} {}'.format(sys.argv[0], ' filepattern ftphost ftpdir dstdir seconds [e.g. \'ASA(.*)zip\' ftp.foo.de /put/xxx/in /net/sensors/bar/new 30]'))
			sys.exit()
		else:
			pattern = sys.argv[1]
			ftphost = sys.argv[2]
			ftpdir = sys.argv[3]
			dstdir = sys.argv[4]
			seconds = sys.argv[5]
		
			t1 = time.time()
			ftp = FTP(ftphost)
			ftp.login()
			ftp.cwd(ftpdir)

			file_list = ftp.nlst()
			for file in file_list:
					if re.search(r'{}'.format(pattern), file, re.DOTALL):
							get_file(ftp, dstdir, file, seconds)

			ftp.quit()
			print('all finished in {0:6.2f} seconds'.format((time.time()-t1)))

if __name__ == '__main__':
        main()
