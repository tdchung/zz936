# -*- coding: utf-8 -*-
"""
Usage


python code_parser.py



"""

import os
import glob
import fire
from posixpath import dirname, split
import re
import pandas as pd


# ====================================================================================
# Functions
# ====================================================================================
def get_list_function_name(file_path):
    """The function use to get all functions of the python file
    Args:
        IN: file_path         - the file path input
        OUT: list_functions   - List all python functions in the input file
    Example Output:
        ['func1', 'func2']
    """
    all_lines = _get_and_clean_all_lines(file_path)
    re_check = r"def (\w+)"
    list_functions = list()
    for line in all_lines:
        re_response = re.match(re_check, line.rstrip())
        if re_response:
            list_functions.append(re_response.group(1))
    return list_functions


def get_list_class_name(file_path):
    """The function use to get all classes of the python file
    Args:
        IN: file_path         - the file path input
        OUT: list_classes     - List all python classes in the input file
    Example Output:
        ['Class1', 'Class1']
    """
    all_lines = _get_and_clean_all_lines(file_path)
    re_check1 = r'class (\w+)'
    # re_check2 = r'class (\w+)'

    list_classes = list()
    for line in all_lines:
        re_response = re.match(re_check1, line.rstrip())
        if re_response:
            list_classes.append(re_response.group(1))
            # print(list_classes)
        # re_response2 = re.match(re_check2, line.rstrip())
        # if re_response2:
        #     list_classes.append(re_response2.group(1))
        #     print(list_classes)
    return list_classes


def get_list_class_methods(file_path):
    """The function use to get all classes and all methods in this class of the python file
    Args:
        IN: file_path         - the file path input
        OUT: An array of class info [{dict}, {dict}, ...]
    Example Output:
    [
        {"class_name": "Class1", "listMethods": ["method1", "method2", "method3"]},
        {"class_name": "Class2", "listMethods": ["method4", "method5", "method6"]},
    ]
    """
    list_names = []
    all_lines = _get_and_clean_all_lines(file_path)
    for class_name in get_list_class_name(file_path):
        class_info = {}
        class_info["class_name"] = class_name
        class_lines, class_indent = _get_all_lines_in_class(class_name, all_lines)
        re_check = f"{class_indent}def (\w+)"
        class_info["listMethods"] = []
        for line in class_lines:
            re_response = re.match(re_check, line.rstrip())
            if re_response:
                class_info["listMethods"].append(re_response.group(1))
        list_names.append(class_info)
    return list_names


def get_list_variable_global(file_path):
    """The function use to get all global variable of the python file
    Args:
        IN: file_path         - the file path input
        OUT: list_var         - Array of all global variable
    Example Output:
        ['Var1', 'Var2']
    """
    all_lines = _get_and_clean_all_lines(file_path)
    re_check1 = r'(\w+)\s+='
    re_check2 = r'(\w+)='
    list_var = []
    for line in all_lines:
        re_response = re.match(re_check1, line.rstrip())
        if re_response:
            list_var.append(re_response.group(1))
        re_response2 = re.match(re_check2, line.rstrip())
        if re_response2:
            list_var.append(re_response2.group(1))
    return list(dict.fromkeys(list_var))


def get_list_function_info(file_path):
    """The function use to get functions stars
    Args:
        IN: file_path         - the file path input
        OUT: Array of functions, lines of the function, and variable in function
    Example Output:
        [
            {"name": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
            {"name": "function_name2", "lines": 30, "variables": []},
        ]
    """
    all_lines = _get_and_clean_all_lines(file_path)
    all_functions = get_list_function_name(file_path)
    output = []
    for function in all_functions:
        data = {}
        data["name"] = function
        lines, indent = _get_all_lines_in_function(function, all_lines)
        data["n_lines"] = len(lines)
        data["variables"], data["n_loop"], data['n_ifthen'] = _get_function_stats(lines, indent)
        data["type"] = "function"

        # calculate code_source
        data["code_source"] = ""
        for line in lines:
            data["code_source"] += line

        # get input variable stats
        lines, indent = _get_all_lines_define_function(function, all_lines)
        data['arg_name'], data['arg_type'], data['arg_value'] = _get_define_function_stats(lines)

        output.append(data)
    return output


def get_list_class_info(file_path):
    """The class use to get functions stars
    Args:
        IN: file_path         - the file path input
        OUT: Array of functions, lines of the function, and variable in function
    Example Output:
        [
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
            {"function": "function_name2", "lines": 30, "variables": []},
        ]
    """
    all_lines = _get_and_clean_all_lines(file_path)
    all_classes = get_list_class_name(file_path)
    output = []
    for class_name in all_classes:
        # print(class_name)
        data = {}
        data["name"] = class_name
        lines, indent = _get_all_lines_in_class(class_name, all_lines)
        data["n_lines"] = len(lines)
        data["variables"], data["n_loop"], data['n_ifthen'] = _get_function_stats(lines, indent)
        data["type"] = "class"

        # calculate code_source
        data["code_source"] = ""
        for line in lines:
            data["code_source"] += line

        data['arg_name'], data['arg_type'], data['arg_value'] = [], [], []

        output.append(data)
    return output


def get_list_method_info(file_path):
    """get_list_method_info
    Args:
        IN: file_path         - the file path input
        OUT: Array of methods in class
    Example Output:
        [
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
            {"function": "function_name2", "lines": 30, "variables": []},
        ]
    """
    all_lines = _get_and_clean_all_lines(file_path)
    all_methods = get_list_class_methods(file_path)

    output = []

    for method in all_methods:
        class_lines, class_indent = _get_all_lines_in_class(method['class_name'], all_lines)
        for method_name in method['listMethods']:
            data                                                = {}
            data["name"]                                        = f"{method['class_name']}:{method_name}"
            lines, indent                                       = _get_all_lines_in_function(method_name, class_lines, class_indent)
            data["n_lines"]                                     = len(lines)
            data["variables"], data["n_loop"], data['n_ifthen'] = _get_function_stats(lines, indent)
            data["type"]                                        = "method"

            # calculate code_source
            data["code_source"] = ""
            for line in lines:
                data["code_source"] += line

            # get input variable stats
            lines, indent = _get_all_lines_define_function(method_name, class_lines, class_indent)
            data['arg_name'], data['arg_type'], data['arg_value'] = _get_define_function_stats(lines)

            output.append(data)
    return output


def get_list_method_stats(file_path):
    """The function use to get methods stars
    Args:
        IN: file_path         - the file path input
        OUT: Dataframe with bellow fields
            uri:   path1/path2/filename.py:function1
            name: function1
            n_lines
            n_words
            n_words_unqiue
            n_characters
            avg_char_per_word = n_charaecter / n_words
            n_loop  : nb of for, while loop
            n_ifthen  : nb of if_then
        
        **** return None if no function in file
    Example Output:
                                                    uri                                               name    type  n_variable  n_words  n_words_unique  n_characters  avg_char_per_word  n_loop  n_ifthen
    0   d:/Project/job/test2/zz936/parser/test/keys.py...                              VerifyingKey:__init__  method           2       11              11           100           9.090909       0         1      
    1   d:/Project/job/test2/zz936/parser/test/keys.py...                     VerifyingKey:from_public_point  method          10       13              12           185          14.230769       0         0      
    2   d:/Project/job/test2/zz936/parser/test/keys.py...                           VerifyingKey:from_string  method          17       45              39           504          11.200000       0         1      
    3   d:/Project/job/test2/zz936/parser/test/keys.py...                              VerifyingKey:from_pem  method           2        2               2            39          19.500000       0         0      
    4   d:/Project/job/test2/zz936/parser/test/keys.py...                              VerifyingKey:from_der  method          19       64              38           683          10.671875       0         3      
    5   d:/Project/job/test2/zz936/parser/test/keys.py...              VerifyingKey:from_public_key_recovery  method           4        8               8           137          17.125000       0         0      
    6   d:/Project/job/test2/zz936/parser/test/keys.py...  VerifyingKey:from_public_key_recovery_with_digest  method          13       24              23           288          12.000000       0         0      
    7   d:/Project/job/test2/zz936/parser/test/keys.py...                             VerifyingKey:to_string  method           6       11               8           145          13.181818       0         0      
    8   d:/Project/job/test2/zz936/parser/test/keys.py...                                VerifyingKey:to_pem  method           2        4               4            42          10.500000       0         0  
    """
    list_info = get_list_method_info(file_path)
    if (len(list_info)):
        df = pd.DataFrame.from_records(list_info)
        return get_stats(df, file_path)
    else:
        return None


def get_list_class_stats(file_path):
    """The class use to get functions stars
    Args:
        IN: file_path         - the file path input
        OUT: Dataframe with bellow fields
            uri:   path1/path2/filename.py:function1
            name: function1
            n_lines
            n_words
            n_words_unqiue
            n_characters
            avg_char_per_word = n_charaecter / n_words
            n_loop  : nb of for, while loop
            n_ifthen  : nb of if_then
        
        **** return None if no function in file
    Example Output:
                                                    uri               name   type  n_variable  n_words  n_words_unique  n_characters  avg_char_per_word  n_loop  n_ifthen
    0  d:/Project/job/test2/zz936/parser/test/keys.py...  BadSignatureError  class           0        1               1             4           4.000000       0         0
    1  d:/Project/job/test2/zz936/parser/test/keys.py...     BadDigestError  class           0        1               1             4           4.000000       0         0
    2  d:/Project/job/test2/zz936/parser/test/keys.py...       VerifyingKey  class          84      301             189          3584          11.906977       0         7
    3  d:/Project/job/test2/zz936/parser/test/keys.py...         SigningKey  class         138      482             310          4615           9.574689       3         9
    """
    list_info = get_list_class_info(file_path)
    if (len(list_info)):
        df = pd.DataFrame.from_records(list_info)
        return get_stats(df, file_path)
    else:
        return None


def get_list_function_stats(file_path):
    """The function use to get functions stars
    Args:
        IN: file_path         - the file path input
        OUT: Dataframe with bellow fields
            uri:   path1/path2/filename.py:function1
            name: function1
            n_lines
            n_words
            n_words_unqiue
            n_characters
            avg_char_per_word = n_charaecter / n_words
            n_loop  : nb of for, while loop
            n_ifthen  : nb of if_then
        
        **** return None if no function in file
    Example Output:
            uri                                 name  n_variable  n_words  n_words_unique  n_characters  avg_char_per_word  n_loop  n_ifthen
        0   d:\Project\job\test2\zz936\parser/test/test2.p...     prepare_target_and_clean_up_test           8       92              32           535           5.815217       0         0
        1   d:\Project\job\test2\zz936\parser/test/test2.p...                 clean_up_config_test           6       55              19           241           4.381818       0         1
        2   d:\Project\job\test2\zz936\parser/test/test2.p...         check_default_network_config          22      388              74           955           2.461340       1         5
        3   d:\Project\job\test2\zz936\parser/test/test2.p...                     check_module_env           9      250              54           553           2.212000       1         1
        4   d:\Project\job\test2\zz936\parser/test/test2.p...     provision_certificates_to_target           7      101              29           384           3.801980       0         3
        5   d:\Project\job\test2\zz936\parser/test/test2.p...            config_session_connection           2       14               8            97           6.928571       0         0
        6   d:\Project\job\test2\zz936\parser/test/test2.p...  config_cipher_suite_and_tcps_action           8      101              30           335           3.316832       0         3
    """
    #### Calcualte Stats:
    list_info = get_list_function_info(file_path)
    if (len(list_info)):
        df = pd.DataFrame.from_records(list_info)
        return get_stats(df, file_path)

    else:
        return None


def get_stats(df:pd.DataFrame, file_path:str):
    """ Calculate stats from datafaframe
    Args:
        df: pandas DataFrame

    Returns:
        pandas DataFrame

    """
    df['uri']               = df['name'].apply(lambda x : f"{file_path}:{x}".replace('\\','/'))
    df['n_variable']        = df['variables'].apply(lambda x : len( x ))
    df['list_words']        = df.apply( lambda x : _get_words(x), axis=1)
    df['n_words']           = df['list_words'].apply(lambda x : len( x ))
    df['n_words_unique']    = df['list_words'].apply(lambda x : len(set( x )))
    df['n_characters']      = df['code_source'].apply(lambda x : len(x.strip().replace(" ","") ))
    df['avg_char_per_word'] = df.apply(lambda x : _get_avg_char_per_word(x), axis=1)
    # print(df)

    cols = ['uri', 'name', 'type', 'n_variable', 'n_words', 
            'n_words_unique', 'n_characters', 'avg_char_per_word', 
            'n_loop', 'n_ifthen', 'arg_name', 'arg_type', 'arg_value']

    df = df[cols]
    # print(df)
    # df.to_csv('functions_stats.csv', index=False)
    return df


def get_file_stats(file_path):
    """The function use to get file stars
    Args:
        IN: file_path         - the file path input
        OUT: Dict of file stars
    Example Output:
        {
            "total_functions": 22,
            "avg_lines" : 110.2,
            "total_class": 3
        }
    """
    output = {}
    res = get_list_function_stats(file_path)
    output["total_functions"] = len(res)
    avg_lines = 0
    for data in res:
        avg_lines += data["lines"]
    output["avg_lines"] = avg_lines/len(res)
    output["total_class"] = len(get_list_class_name(file_path))
    return output


# ====================================================================================
# internal Functions
# ====================================================================================


def _get_words(row):
    data = [row['code_source'].strip().split(" ")]
    # print(data)
    for ele in data[0].copy():
        if ele in ['', '-', '+', '=', '*', '/', '==', '<=', '>=', '!=']:
            data[0].remove(ele)
    # print(data)
    return data[0]


def _get_avg_char_per_word(row):
    return (round(row['n_characters']/row['n_words'], 2)) if (row['n_words'] > 0) else 0


def _validate_file(file_path):
    """Check if the file is existed and it's a python file
    """
    if not os.path.exists(file_path):
        print("Input file is not exists")
        return False
    if not os.path.isfile(file_path):
        print("Input is not a file")
        return False
    if file_path[-3:] != ".py":
        print("The input file is not python file")
        return False
    return True


def _clean_data(array):
    """Remove empty lines and comment lines start with #
    """
    response = array.copy()
    for line in array:
        if _remove_empty_line(line) or _remmove_commemt_line(line):
            response.remove(line)

    detect_block = False
    for line in response.copy():
        # start block comments detected
        if not detect_block:
            if line.strip()[:3] == '"""':
                if line.strip()[-3:] == '"""':
                    response.remove(line)
                else:
                    detect_block = True
                    response.remove(line)
        else:
            # end block comments detected
            if line.strip()[-3:] == '"""':
                detect_block = False
            response.remove(line)

    detect_block = False
    for line in response.copy():
        # start block comments detected
        if not detect_block:
            if line.strip()[:3] == "'''":
                if line.strip()[-3:] == "'''":
                    response.remove(line)
                else:
                    detect_block = True
                    response.remove(line)
        else:
            # end block comments detected
            if line.strip()[-3:] == "'''":
                detect_block = False
            response.remove(line)

    return response


def _remove_empty_line(line):
    return True if line.strip() == "" else False


def _remmove_commemt_line(line):
    if line.strip()[0] == '#' and ('"""' not in line.strip() or "'''" not in line.strip()):
        return True
    return False


def _get_and_clean_all_lines(file_path):
    """Prepare all lines of the file
    """
    if not _validate_file(file_path):
        return []
    all_lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        all_lines = (f.readlines())
    all_lines = _clean_data(all_lines)
    return all_lines


def _get_all_lines_in_function(function_name, array, indentMethod=''):
    """The function use to get all lines of the function
    Args:
        IN: function_name - name of the function will be used to get all line
        IN: array         - list all lines of the file have this input function
        OUT: list_lines   - Array of all line of this function
        OUT: indent       - The indent of this function (this will be used for another calculation)
    """
    re_check = f"{indentMethod}def {function_name}"

    response = array.copy()

    # 1. get start line
    for line in array:
        re_response = re.match(re_check, line.rstrip())
        if re_response == None:
            response.remove(line)
        else:
            break

    # 2. get indent
    start_idx = 0
    if response[0].rstrip()[-1] == ':':
        indent = re.match(r"(\s+)\w*", response[1]).group(1)
        start_idx = 1
    else:
        for i in range(len(response)):
            if response[i].rstrip()[-1] == ':':
                start_idx = i+1
                break
        indent = re.match(r"(\s+)\w*", response[start_idx]).group(1)

    # 3. get all lines in function
    list_lines = list()
    for line in response[start_idx:]:
        if re.match(re_check, line.rstrip()):
            list_lines.append(line)
        elif (len(line) > len(indent) and line[:len(indent)] == indent):
            list_lines.append(line)
        else:
            break

    return list_lines, indent


def _get_all_lines_define_function(function_name, array, indentMethod=''):
    """The function use to get all lines define_function
    Args:
        IN: function_name - name of the function will be used to get all line
        IN: array         - list all lines of the file have this input function
        OUT: list_lines   - Array of all line used to define the function
        OUT: indent       - The indent of this function (this will be used for another calculation)
    """
    re_check = f"{indentMethod}def {function_name}"

    list_lines = list()
    response = array.copy()

    # 1. get start line
    for line in array:
        re_response = re.match(re_check, line.rstrip())
        if re_response == None:
            response.remove(line)
        else:
            break

    # 2. check if the is one or multi lines
    start_idx = 0
    if response[0].rstrip()[-1] == ':':
        indent = re.match(r"(\s+)\w*", response[1]).group(1)
        start_idx = 1
        list_lines.append(response[0])
    else:
        for i in range(len(response)):
            list_lines.append(response[i])
            if response[i].rstrip()[-1] == ':':
                start_idx = i+1
                break
        indent = re.match(r"(\s+)\w*", response[start_idx]).group(1)
    return list_lines, indent


def _get_define_function_stats(array):
    """The function use to get define function stats: arg_name, arg_type, arg_value
    Args:
        IN: array         - list all lines of function to get variables
        OUT: function stats: arg_name, arg_type, arg_value
    """
    arg_name  = []
    arg_type  = []
    arg_value = []
    data      = ''
    if len(array) == 1:
        data = array[0].strip()[array[0].strip().find('(') + 1: array[0].strip().find(')')]
    elif len(array) > 1:
        data = ''
        for line in array:
            if line.strip().find('(') >= 0:
                data += line.strip()[line.strip().find('(')+1:]
            elif line.strip().find(')') >= 0:
                data += line.strip()[: line.strip().find(')')]
            else:
                data += line.strip()
    else:
        print("Invalid array data")
    if data != '':
        check = ([ i.start() for i in re.finditer('"', data)])
        if len(check) > 0 and len(check)%2 == 0:
            for i in range(0, len(check), 2):
                data = (data.replace(data[check[i]+1:check[i+1]], data[check[i]+1:check[i+1]].replace(',', '^^^')))

        check = ([ i.start() for i in re.finditer("'", data)])
        if len(check) > 0 and len(check)%2 == 0:
            for i in range(0, len(check), 2):
                data = (data.replace(data[check[i]+1:check[i+1]], data[check[i]+1:check[i+1]].replace(',', '^^^')))

        args = data.split(',')
        for arg in args:
            arg = arg.replace('^^^', ',')
            arg = arg.strip()
            # print(arg)
            if arg.find(':') >= 0:
                arg_name.append(arg[: arg.find(':')])
                if arg.find('=') >= 0:
                    arg_type.append(arg[arg.find(':')+1: arg.find('=')])
                    arg_value.append(arg[arg.find('=')+1 : ])
                else:
                    arg_type.append(arg[arg.find(':')+1: ])
                    arg_value.append(None)
            else:
                arg_type.append(None)
                if arg.find('=') >= 0:
                    arg_name.append(arg[ : arg.find('=')])
                    arg_value.append(arg[arg.find('=')+1 : ])
                else:
                    arg_name.append(arg)
                    arg_value.append(None)

    # print(array, data)
    # print(arg_name, arg_type, arg_value)
    return arg_name, arg_type, arg_value


def _get_function_stats(array, indent):
    """The function use to get all lines of the function
    Args:
        IN: indent        - indent string
        IN: array         - list all lines of function to get variables
        OUT: list_var     - Array of all variables
    """
    list_python_kwd = ["if", "elif", "else", "True", "False", "for", "while", "not", "None", "global", "self",
                       "try", "except", "Exception", "as", "e", "in", "def", "class", "assert",
                       "int", "float", "list", "set", "dict", "len", "yield", "is", "then", "pass", "raise"]
    check_array = array.copy()

    list_var = []
    n_loops = 0
    n_ifthen = 0

    is_detect = False
    for line in check_array.copy():
        # clear multi line function
        if not is_detect:
            if line.rstrip().find('(') > 0:
                if line.rstrip().find(')') < 0:
                    is_detect = True
                line = line.rstrip()[:line.rstrip().find('(')]
            else:
                line = line.rstrip()
        else:
            check_array.remove(line)
            if line.rstrip().find(')') > 0:
                is_detect = False

    is_detect = False
    for line in check_array.copy():
        # clear multi line function
        if not is_detect:
            if line.rstrip().find('[') > 0:
                if line.rstrip().find(']') < 0:
                    is_detect = True
                line = line.rstrip()[:line.rstrip().find('[')]
            else:
                line = line.rstrip()
        else:
            check_array.remove(line)
            if line.rstrip().find(']') > 0:
                is_detect = False

    for line in check_array.copy():
        # clear string
        if line.rstrip().find('(') >= 0:
            line = line.rstrip()[:line.rstrip().find('(')]
        elif line.rstrip().find('r"') >= 0:
            line = line.rstrip()[:line.rstrip().find('r"')]
        elif line.rstrip().find('b"') >= 0:
            line = line.rstrip()[:line.rstrip().find('b"')]
        elif line.rstrip().find('f"') >= 0:
            line = line.rstrip()[:line.rstrip().find('f"')]
        elif line.rstrip().find('"') >= 0:
            line = line.rstrip()[:line.rstrip().find('"')]
        elif line.rstrip().find("r'") >= 0:
            line = line.rstrip()[:line.rstrip().find("r'")]
        elif line.rstrip().find("b'") >= 0:
            line = line.rstrip()[:line.rstrip().find("b'")]
        elif line.rstrip().find("f'") >= 0:
            line = line.rstrip()[:line.rstrip().find("f'")]
        elif line.rstrip().find("'") >= 0:
            line = line.rstrip()[:line.rstrip().find("'")]
        else:
            line = line.rstrip()

        keywords = [work.replace(':', '').replace(',', ' ')
                    for work in line.split()]
        for work in keywords:
            if (re.match(r'\w+', work) or re.match(r'\w+.\w+', work)) and \
                    re.match(r'\d+', work) == None and work not in list_python_kwd:
                list_var.append(work)
            
            # get for while loops
            if work  in ["for", "while"]:
                n_loops += 1
            if work  in ["if", "then"]:
                n_ifthen += 1

    # return list_var
    return list(dict.fromkeys(list_var)), n_loops, n_ifthen


def _get_all_lines_in_class(class_name, array):
    """The function use to get all lines of the class
    Args:
        IN: class_name    - name of the class will be used to get all line
        IN: array         - list all lines of the file have this input class
        OUT: list_lines   - Array of all line of this class
    """
    re_check1 = f"class {class_name}\("
    re_check2 = f"class {class_name}:"
    response = array.copy()

    # 1. get start line
    for line in array:
        re_response1 = re.match(re_check1, line.rstrip())
        re_response2 = re.match(re_check2, line.rstrip())

        if re_response1 == None and re_response2 == None:
            response.remove(line)
        else:
            break

    # 2. get indent
    if re.match(r"(\s+)\w*", response[1]):
        indent = re.match(r"(\s+)\w*", response[1]).group(1)
    else:
        return [], ''

    # 3. get all line in class
    list_lines = list()
    for line in response[1:]:
        if re.match(re_check1, line.rstrip()) or re.match(re_check2, line.rstrip()):
            list_lines.append(line)
        elif (len(line) > len(indent) and line[:len(indent)] == indent):
            list_lines.append(line)
        else:
            break
    return list_lines, indent


# ====================================================================================
# MAIN
# ====================================================================================
def export_stats_pertype(in_path:str=None, type:str=None, out_path:str=None):
    """
        python code_parser.py type <in_path> <type> <out_path>
    Returns:

    """
    file = in_path
    if type == "function":
        df = get_list_function_stats(file)
        print(df)
        if df is not None:
            df.to_csv(f'{out_path}', index=False)
    elif type == "class":
        df = get_list_class_stats(file)
        print(df)
        if df is not None:
            df.to_csv(f'{out_path}', index=False)
    elif type == "method":
        df = get_list_method_stats(file)
        print(df)
        if df is not None:
            df.to_csv(f'{out_path}', index=False)
    else:
        print("Type is invalid. ")


def export_stats_perfile(in_path:str=None, out_path:str=None):
    """
        python code_parser.py  export_stats_perfile <in_path> <out_path>

    Returns:

    """
    file = in_path
    df = get_list_function_stats(file)
    print(df)
    if df is not None:
        df.to_csv(f'{out_path}', index=False)

    df = get_list_class_stats(file)
    print(df)
    if df is not None:
        df.to_csv(f'{out_path}', mode='a', header=False, index=False)

    df = get_list_method_stats(file)
    print(df)
    if df is not None:
        df.to_csv(f'{out_path}', mode='a', header=False, index=False)


def export_stats_perrepo(in_path:str=None, out_path:str=None):
    """ 
        python code_parser.py  export_stats_perfile <in_path> <out_path>

    Returns:
        1  repo   --->  a single file stats for all sub-diractory
    """
    root = in_path
    flist = glob.glob(root +"/*.py")
    flist = flist + glob.glob(root +"/*/*.py")
    flist = flist + glob.glob(root +"/*/*/*.py")
    flist = flist + glob.glob(root +"/*/*/*/*.py")
    flist = flist + glob.glob(root +"/*/*/*/*/*.py")

    # print(flist)
    for i in range(len(flist)):
        # output_file = re.search(r'(\w+).py', file).group(1)
        # export_stats_perfile(file, f"{out_path}/file_{output_file}.csv")
        df = get_list_function_stats(flist[i])
        print(df)
        if df is not None:
            if i == 0:
                df.to_csv(f'{out_path}', index=False)
            else:
                df.to_csv(f'{out_path}', mode='a', header=False, index=False)
        df = get_list_class_stats(flist[i])
        print(df)
        if df is not None:
            df.to_csv(f'{out_path}', mode='a', header=False, index=False)

        df = get_list_method_stats(flist[i])
        print(df)
        if df is not None:
            df.to_csv(f'{out_path}', mode='a', header=False, index=False)


def test_example():
    # export_stats_pertype('parser/test3/arrow_dataset.py', "function", "parser/output/output_function.csv")
    # export_stats_pertype('parser/test3/arrow_dataset.py', "class", "parser/output/output_function.csv")
    export_stats_pertype('parser/test3/arrow_dataset.py', "method", "parser/output/output_function.csv")
    export_stats_perfile('parser/code_parser.py', "parser/output/output_file.csv")
    export_stats_perrepo('parser/test3', "parser/output/output_repo.csv")

if __name__ == "__main__":
    fire.Fire({
      'type': export_stats_pertype,
      'file': export_stats_perfile,
      'repo': export_stats_perrepo,
    })
    # test_example()

    '''List example to run:
        python code_parser.py type parser/test3/arrow_dataset.py method parser/output/output_method.csv
        python code_parser.py file parser/code_parser.py method parser/output/output_file.csv
        python code_parser.py repo parser/test3 parser/output/output_repo.csv
    '''
