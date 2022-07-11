#!F:\智慧公交\展示\show\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hdfs==2.5.8','console_scripts','hdfscli-avro'
__requires__ = 'hdfs==2.5.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hdfs==2.5.8', 'console_scripts', 'hdfscli-avro')()
    )
