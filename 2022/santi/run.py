"""python run.py <filename>"""

import sys
import time
import importlib
import inspect

mod = importlib.import_module(sys.argv[1].strip(".py"))

# Iterate through all functions and call them
for name, obj in inspect.getmembers(mod):
    if inspect.isfunction(obj):
        start_time = time.time()
        result = obj()
        time_elapsed = time.time() - start_time
        print(f"Function '{name}' finished in --- {time_elapsed:.6f} seconds ---\n")
