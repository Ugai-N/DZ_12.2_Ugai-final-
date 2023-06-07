def get_val(collection, key, default='git'):
    '''
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    '''
    if key.title() in collection.keys():
        for k, v in collection.items():
            if k == key.title():
                return v
    return default
