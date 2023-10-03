import requests
import os


class DataLoader:
    def __init__(self, day: int, year: int = 2022) -> None:
        self.day = day
        self.year = year

        _cache_dir = "__cache__"
        _cache_file = f"cache_{self.day}_{self.year}.txt"
        self.full_cache_path = os.path.join(_cache_dir, _cache_file)

    def load(self, cache: bool = True):
        # If cache file exists, read and return data from it
        if os.path.exists(self.full_cache_path) and cache:
            with open(self.full_cache_path, "r") as f:
                return f.read()
        else:
            # If cache file does not exist, request data, write to cache, and return it
            # only require session cookie if data not cached
            session_cookie = os.getenv("SESSION")
            if session_cookie == None:
                exit(
                    "No session cookie found. Please set the SESSION environment variable to your adventofcode.com session cookie."
                )
            self.cookies = {"session": session_cookie}
            data = requests.get(
                f"https://adventofcode.com/{self.year}/day/{self.day}/input",
                cookies=self.cookies,
            ).text[:-1]

        if cache:
            # Make sure the cache directory exists before opening the file
            os.makedirs(os.path.dirname(self.full_cache_path), exist_ok=True)

            # Write to cache
            with open(self.full_cache_path, "w") as f:
                f.write(data)

        return data
