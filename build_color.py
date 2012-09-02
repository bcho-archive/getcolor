#coding: utf-8

import csv
import json


SRCFILE = 'data/allLang_simp.csv'
DESTFILE = 'data/colornames.json'


def _get_color_lists(func=None):
    f = open(SRCFILE, 'r')
    handler = csv.DictReader(f)
    if not func:
        func = lambda x:x
    return [func(color) for color in handler]


def _write(data, dest):
    f = open(dest, 'w')
    f.write(data)
    f.close()


def _get_fields(raw):
    def _get_en_keys(keys):
        ret = []
        for key in keys:
            if key.find('EN') != -1:
                ret.append(key)
        return ret

    keys = ['r', 'g', 'b', 'name', 'short_name', 'med_name', 'Chinese']
    keys.extend(_get_en_keys(raw.keys()))
    for key in raw.keys():
        if key not in keys:
            raw.pop(key)

    return raw

def _main():
    _write(json.dumps(_get_color_lists(_get_fields)), DESTFILE)


if __name__ == '__main__':
    _main()
