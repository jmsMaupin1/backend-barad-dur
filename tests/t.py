def dict_diff(d1, d2):
    """Takes two dicts and returns the difference between them"""
    diff = {}
    for k in d1.keys():
        if k not in d2:
            diff[k] = [d1[k], None]
        elif d1[k] != d2[k]:
            diff[k] = [d1[k], d2[k]]
    for k in d2.keys():
        if k not in d1:
            diff[k] = [None, d2[k]]
    return diff