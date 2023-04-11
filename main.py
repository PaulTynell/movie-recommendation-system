

import requester

def main():

    api = requester.Requester()

    trending_tv = api.get_trending("tv", "week")
    print(trending_tv)


if __name__ == '__main__':
    main()