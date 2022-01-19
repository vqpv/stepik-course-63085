def format_namelist(lst):
    items = []
    for i in lst:
        items.append(i['name'])
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) > 1:
        return ', '.join(items[:-1]) + ' и ' + items[-1]
