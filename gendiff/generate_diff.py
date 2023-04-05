import json


def generate_diff(path_to_file1, path_to_file2):
    file1 = json.load(open(path_to_file1))
    file2 = json.load(open(path_to_file2))
    common_value = set(file1.keys()) & set(file2.keys())
    old_value = set(file1.keys()) - set(file2.keys())
    new_value = set(file2.keys()) - set(file1.keys())
    begin = '{' + '\n'
    end = '\n' + '}'
    result = {}
    for i in common_value:
        if file1[i] == file2[i]:
            result['  ' + i] = file1[i]
        else:
            result['- ' + i] = file1[i]
            result['+ ' + i] = file2[i]
    for i in old_value:
        result['- ' + i] = file1[i]
    for i in new_value:
        result['+ ' + i] = file2[i]
    diff = []
    for k, v in sorted(result.items(), key=lambda x: x[0][2:]):
        if type(v) == bool:
            diff.append(f'  {k}: {str(v).lower()}')
        else:
            diff.append(f'  {k}: {v}')
    return begin + '\n'.join(diff) + end
