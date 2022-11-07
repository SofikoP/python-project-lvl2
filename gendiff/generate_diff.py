import json


def remove_indent(string):
    return string[4:]


def generate_diff(path_to_file1, path_to_file2):
    file1 = json.load(open(path_to_file1))
    file2 = json.load(open(path_to_file2))
    common_value = file1.keys() & file2.keys()
    old_value = file1.keys() - file2.keys()
    new_value = file2.keys() - file1.keys()
    begin = '{' + '\n'
    end = '\n' + '}'
    result = []
    for i in common_value:
        if file1[i] == file2[i]:
            result.append(f'    {i}: {file1[i]}')
        else:
            result.append(f'  - {i}: {file1[i]}')
            result.append(f'  + {i}: {file2[i]}')
    for i in old_value:
        result.append(f'  - {i}: {file1[i]}')
    for i in new_value:
        result.append(f'  + {i}: {file2[i]}')
    result.sort(key=remove_indent)
    return begin + '\n'.join(result) + end
