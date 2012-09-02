#coding: utf-8

import requests
import json

from build_color import _get_color_lists

URL = 'http://localhost:5000/color/add/'


def post_color(raw):
    def _get_en_keys(keys):
        ret = []
        for key in keys:
            if key.find('EN') != -1:
                ret.append(key)
        return ret

    def _get_descriptions(raw):
        ret = [raw['Chinese']]
        for key in _get_en_keys(raw.keys()):
            ret.append(raw[key])
        return ret

    def _post(payload):
        ret = requests.post(
                URL,
                data=json.dumps(payload),
                headers={'Content-Type':'application/json'}
                )
        return ret
    
    descs = _get_descriptions(raw)
    keys = ['r', 'g', 'b', 'name', 'short_name', 'med_name']
    for key in raw.keys():
        if key not in keys:
            raw.pop(key)
    raw['descriptions'] = descs

    return _post(raw)


def _main():
    return _get_color_lists(post_color)


if __name__ == '__main__':
    _main()
