py_dictionary = {
    'key_string': 'value_string',
    'key_int': 1,
    'key_float': 1.0,
    'key_boolean': True,
    'key_list': [True, 2, 3.0, '5'],
    'key_dictionary': {
        'nested' : [
            'I\'m',
            'nested',
            'data'
        ]
    }
}

print (py_dictionary['key_dictionary']['nested'][1])