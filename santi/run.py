"""python run.py <filename>"""

import sys
import time
import importlib
start_time = time.time()
importlib.import_module(sys.argv[1].strip(".py"))
print(f"Process finished --- {time.time() - start_time} seconds ---")