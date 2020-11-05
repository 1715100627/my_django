import re


def get_paginated_response(datas):
    list = []
    for i in datas:
        mtch = re.search(r'(.*)T(.*)\..*?', i['create_time'])
        i['create_time'] = mtch.group(1) + ' ' + mtch.group(2)
    return list.append(datas)
