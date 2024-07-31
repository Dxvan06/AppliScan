import requests

def discover_directories(url, wordlist):
    found_dirs = []
    with open(wordlist, 'r') as file:
        for line in file:
            path = url + '/' + line.strip()
            response = requests.get(path)
            if response.status_code == 200:
                found_dirs.append(path)
    return found_dirs
