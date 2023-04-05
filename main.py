

import requester

def main():

    api = requester.Requester()

    api.get_trending("movie", "day")


if __name__ == '__main__':
    main()