"""python perftest.py <filename>"""

import sys
import importlib
import inspect
import time
from timeit import timeit

iterations = 10000
mod = importlib.import_module(sys.argv[1].strip(".py"))

# Iterate through all functions and call them
start_time = time.time()
for name, obj in inspect.getmembers(mod):
    if inspect.isfunction(obj) and "part" in name:
        avg_time = timeit(obj, number=iterations)/iterations
        print(f"\033[32mAverage time for \033[33m{name}\033[32m --- \033[36m{avg_time}\033[32m seconds ---\n\n\033[0m")
time_elapsed = time.time() - start_time

minutes, sec = divmod(time_elapsed, 60)
seconds, milliseconds = divmod(sec * 1000, 1000)
print(f"\033[33mTotal time: {int(minutes):02}:{int(seconds):02}:{int(milliseconds):03}\033[0m")


