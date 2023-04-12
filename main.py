

from requester import *

def main():
    api = Requester()
    results = api.get_trending("movie", "day")
    return results

if __name__ == '__main__':
    print(main())