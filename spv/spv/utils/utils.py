def hashmap(keys, args):
    sanitized = {}
    for index in args:
        if index in keys:
            sanitized[index] = args[index]
    return sanitized