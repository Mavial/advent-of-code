"""python run.py <filename>"""

import sys
import time
import importlib
import inspect

mod = importlib.import_module(sys.argv[1].strip(".py"))

# Iterate through all functions and call them
for name, obj in inspect.getmembers(mod):
    if inspect.isfunction(obj) and "part" in name:
            start_time = time.time()
            result = obj()
            time_elapsed = time.time() - start_time
            print(f"\033[32mFunction \033[33m{name}\033[32m finished in --- \033[36m{time_elapsed:.6f}\033[32m seconds ---\n\033[0mResult: {result}\n")


