
def introspection_info(obj):

    obj_type = type(obj).__name__  # тип объекта
    attributes = dir(obj)          # атрибуты
    methods = [method for method in attributes if callable(getattr(obj, method))]    # методы
    module = obj.__class__.__module__   # модуль

    dict_ = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}

    return dict_


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('привет')
print(string_info)

dict_info= introspection_info({'w': 3,'e': 6})
print(dict_info)
