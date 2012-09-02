#coding: utf-8

from .models import db, Color, Descriptions

def _to_dict(instance, keys):
    ret = {}
    for key in keys:
        ret[key] = getattr(instance, key, None)
    return ret


def desc_to_dict(desc):
    return _to_dict(desc, ['desc'])


def color_to_dict(color):
    ret = _to_dict(color,
        ['hexcode', 'r', 'g', 'b', 'name', 'med_name', 'short_name'])
    ret['descriptions'] = [desc_to_dict(desc) for desc in color.descriptions]
    return ret


def add_color(data):
    descs = data.pop('descriptions')
    c = Color(**data)
    c.add_descriptions(descs)
    db.session.add(c)
    db.session.commit()

    return c.name


def search_color_by_keyword(keyword, limit):
    descs = db.session.query(Descriptions).filter(Descriptions.desc.like(
        '%' + keyword + '%')).all()
    ret = []
    record = []
    for i in descs:
        if i.color.hexcode not in record:
            ret.append(color_to_dict(i.color))
            record.append(i.color.hexcode)
        if len(ret) >= limit:
            break
    return ret, len(ret)
