def hashmap(keys, obj):
    mapped = {}
    for index in obj:
        if index in keys:
            mapped[index] = obj[index]
    return mapped
