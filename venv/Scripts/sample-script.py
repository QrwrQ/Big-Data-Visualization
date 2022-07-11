#!F:\智慧公交\展示\show\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'echarts==0.0.0','console_scripts','sample'
__requires__ = 'echarts==0.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('echarts==0.0.0', 'console_scripts', 'sample')()
    )
