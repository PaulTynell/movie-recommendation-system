# File dict_manipulator
# Author: Heikki Jarvinen
# Description: functions used to manipulate dictionarys

import requester

def print_dict(dicti: dict):
    for x, y in dicti.items():
        return "\n".join(map(str, x))

def get_dictionary_keys(dictionary):
    keys = ""
    for key in dictionary.keys():
        keys += str(key) + "\n"
    return keys

def return_dict(format, time):

    api = requester.Requester()

    trending_tv = api.get_trending(format, time)

    return get_dictionary_keys(trending_tv)
