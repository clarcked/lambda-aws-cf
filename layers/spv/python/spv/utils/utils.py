def hashmap(keys, obj) -> dict:
    mapped = {}
    for index in obj:
        if index in keys:
            mapped[index] = obj[index]
    return mapped
