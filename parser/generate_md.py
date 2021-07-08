import pandas as pd
from ast import literal_eval

def create_markdown_function(uri, name, type, args_name, args_type, args_value):
    rsp = '''
    <details>
        <summary>
        {} | <a name='{}' href='{}'>{}</a>
        </summary>
        <ul>
        <li>Args:</li>
        <ul>{}</ul>
        <li>Docs:</li>
        </ul>
    </details>'''
    function_name = uri.split(':', 1)[1]
    file = uri.split(':', 1)[0]
    args_name = literal_eval(args_name)
    args_type = literal_eval(args_type)
    args_value = literal_eval(args_value)
    print(args_name)
    args_str = ''
    for arg_name, arg_type, arg_value in zip(args_name, args_type, args_value):
        arg_type = f': {arg_type}' if arg_type != None else ''
        arg_value = f' = {arg_value}' if arg_value != None else ''
        args_str += f'{arg_name}{arg_type}{arg_value},<br>'
    return {'file': file, 'info': rsp.format(type, uri, uri, function_name, args_str)}


def create_markdown_file(list_info):
    rsp = '''
<details>
<summary>
<a name='{}' href='https://github.com'>{}</a>
</summary>
<ul>{}</ul>
</details>
'''
    output_str = ''
    list_files = set([data['file'] for data in list_info])
    for file in list_files:
        eles = ''
        for data in list_info:
            if data['file'] == file:
                eles += '{}'.format(data['info'])
        output_str += rsp.format(file, file, eles)
    # print(output_str)
    return(output_str)


def creat_all_markdown(dfi):
    result = [create_markdown_function(row[0], row[1], row[2], row[3], row[4], row[5]) for row in zip(
        dfi['uri'], dfi['name'], dfi['type'], dfi['arg_name'], dfi['arg_type'], dfi['arg_value'])]
    # print(result)
    list_markdown = create_markdown_file(result)
    return list_markdown


# TABLE
def table_create_row(uri, name, type):
    rsp = '| [{}](#{}) | [{}](#{}) | {} |'
    file = uri.split(':', 1)[0]
    return rsp.format(file, file, name, uri, type)


def table_all_row(list_rows):
    rsp = '''
| file | name | type  |
| ------- | --- | --- |
'''
    for row in list_rows:
        rsp += f'{row}\n'
    return rsp

def create_table(dfi):
    list_rows = [table_create_row(row[0], row[1], row[2])
                for row in zip(dfi['uri'], dfi['name'], dfi['type'])]
    data = table_all_row(list_rows)
    return data


def main():
    input_file = 'parser/output/output_repo.csv'
    output_file = "test.md"

    # with open(input_file, 'r', encoding='utf-8') as f:
    dfi = pd.read_csv(input_file)

    str_table = create_table(dfi)
    with open(output_file, 'w+', encoding='utf-8') as f:
        f.write(str_table)

    str_markdown = creat_all_markdown(dfi)
    with open(output_file, 'a+', encoding='utf-8') as f:
        f.write(str_markdown)


if __name__ == '__main__':
    main()