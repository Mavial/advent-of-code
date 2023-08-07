"""python perftest.py <filename>"""

import sys
import importlib
import inspect
from timeit import timeit

iterations = 100000
mod = importlib.import_module(sys.argv[1].strip(".py"))

# Iterate through all functions and call them
for name, obj in inspect.getmembers(mod):
    if inspect.isfunction(obj):
        avg_time = timeit(obj, number=iterations)/iterations
        print(f"Average time for {name} --- {avg_time} seconds ---\n")