# -*- coding: utf-8 -*-
"""
python code_parse.py
List functions:
- get_list_function_name(file_path)
    The function use to get all functions of the python file
    Args:
        IN: file_path         - the file path input
        OUT: list_functions   - List all python functions in the input file
    Example Output:
        ['func1', 'func2']
- get_list_class_name(file_path):
    The function use to get all classes of the python file
    Args:
        IN: file_path         - the file path input
        OUT: list_classes     - List all python classes in the input file
    Example Output:
        ['Class1', 'Class1']
- get_list_class_methods(file_path):
    The function use to get all classes and all methods in this class of the python file
    Args:
        IN: file_path         - the file path input
        OUT: An array of class info [{dict}, {dict}, ...]
    
    Example Output:
    [
        {"name": "Class1", "listMethods": ["method1", "method2", "method3"]},
        {"name": "Class2", "listMethods": ["method4", "method5", "method6"]},
    ]
- get_list_variable_global(file_path):
    The function use to get all global variable of the python file
    Args:
        IN: file_path         - the file path input
        OUT: list_var         - Array of all global variable
    Example Output:
        ['Var1', 'Var2']
- get_list_function_stats(file_path):
    The function use to get functions stars
    Args:
        IN: file_path         - the file path input
        OUT: Array of functions, lines of the function, and variable in function
    Example Output:
        [
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
            {"function": "function_name2", "lines": 30, "variables": []},
        ]
- get_file_stats(file_path):
    The function use to get file stars
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

import os
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
    re_check1 = r'class (\w+)*\(.+\)*:'
    re_check2 = r'class (\w+)*:'

    list_classes = list()
    for line in all_lines:
        re_response = re.match(re_check1, line.rstrip())
        if re_response:
            list_classes.append(re_response.group(1))
        re_response2 = re.match(re_check2, line.rstrip())
        if re_response2:
            list_classes.append(re_response2.group(1))
    return list_classes


def get_list_class_methods(file_path):
    """The function use to get all classes and all methods in this class of the python file
    Args:
        IN: file_path         - the file path input
        OUT: An array of class info [{dict}, {dict}, ...]
    Example Output:
    [
        {"name": "Class1", "listMethods": ["method1", "method2", "method3"]},
        {"name": "Class2", "listMethods": ["method4", "method5", "method6"]},
    ]
    """
    list_names = []
    all_lines = _get_and_clean_all_lines(file_path)
    for class_name in get_list_class_name(file_path):
        class_info = {}
        class_info["name"] = class_name
        class_lines = _get_all_lines_in_class(class_name, all_lines)
        re_check = r"def (\w+)\(.+\):"
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
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
            {"function": "function_name2", "lines": 30, "variables": []},
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

        output.append(data)
    return output


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
    """
        uri:   path1/path2/filename.py:function1
        name: function1
        n_lines
        n_words
        n_words_unqiue
        n_characters
        avg_char_per_word = n_charaecter / n_words
        n_loop  : nb of for, while loop
        n_ifthen  : nb of if_then
    """
    list_info = get_list_function_info(file_path)
    df = pd.DataFrame.from_records(list_info)
    # print(df)

    df['uri']            = df['name'].apply(lambda x : "{}:{}".format(file_path, x).replace('\\','/'))
    df['n_variable']     = df['variables'].apply(lambda x : len( x ))
    df['n_words']        = df['code_source'].apply(lambda x : len( x.split(" ") ))
    df['n_words_unique'] = df['code_source'].apply(lambda x : len(set( x.split(" ") )))
    df['n_characters']   = df['code_source'].apply(lambda x : len(x.strip().replace(" ","") ))
    df['avg_char_per_word']   = df['code_source'].apply(lambda x : len(x.strip().replace(" ",""))/len( x.split(" ")))
    # print(df)

    cols = [
        'uri',
        'name',
        'type',
        'n_variable',
        'n_words',
        'n_words_unique',
        'n_characters',
        'avg_char_per_word',
        'n_loop',
        'n_ifthen',
    ]

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


def _validate_file(file_path):
    """Check if the file is existed and it's a python file
    """
    # print("Validate: {}".format(file_path))
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
    with open(file_path, 'r') as f:
        all_lines = (f.readlines())
    all_lines = _clean_data(all_lines)
    return all_lines


def _get_all_lines_in_function(function_name, array):
    """The function use to get all lines of the function
    Args:
        IN: function_name - name of the function will be used to get all line
        IN: array         - list all lines of the file have this input function
        OUT: list_lines   - Array of all line of this function
        OUT: indent       - The indent of this function (this will be used for another calculation)
    """
    re_check = r"def {}".format(function_name)
    response = array.copy()

    # 1. get start line
    for line in array:
        re_response = re.match(re_check, line.rstrip())
        if re_response == None:
            response.remove(line)
        else:
            # print("Debug: _get_all_lines_in_function. {}".format(line))
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


def _get_function_stats(array, indent):
    """The function use to get all lines of the function
    Args:
        IN: indent        - indent string
        IN: array         - list all lines of function to get variables
        OUT: list_var     - Array of all variables
    """
    list_python_kwd = ["if", "elif", "else", "True", "False", "for", "while", "not", "None", "global", "self",
                       "try", "except", "Exception", "as", "e", "in", "def", "class", "assert",
                       "int", "float", "list", "set", "dict", "len", "yield", "is", "then"]
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
        elif line.rstrip().find('"') >= 0:
            line = line.rstrip()[:line.rstrip().find('"')]
        elif line.rstrip().find("r'") >= 0:
            line = line.rstrip()[:line.rstrip().find("r'")]
        elif line.rstrip().find("b'") >= 0:
            line = line.rstrip()[:line.rstrip().find("b'")]
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
    re_check1 = r"class {}\(.+\):".format(class_name)
    re_check2 = r"class {}:".format(class_name)
    response = array.copy()

    # 1. get start line
    for line in array:
        re_response1 = re.match(re_check1, line.rstrip())
        re_response2 = re.match(re_check2, line.rstrip())

        if re_response1 == None and re_response2 == None:
            response.remove(line)
        else:
            # print("Debug: _get_all_lines_in_class. {}".format(line))
            break

    # 2. get indent
    indent = re.match(r"(\s+)\w*", response[1]).group(1)

    # 3. get all line in class
    list_lines = list()
    for line in response[1:]:
        if re.match(re_check1, line.rstrip()) or re.match(re_check2, line.rstrip()):
            list_lines.append(line)
        elif (len(line) > len(indent) and line[:len(indent)] == indent):
            list_lines.append(line)
        else:
            break
    return list_lines


# ====================================================================================
# MAIN
# ====================================================================================
def main():
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))

    test_files = ['test.py', 'test2.py', 'test3.py',
                  "model_gefs.py", "model_sklearn.py"]

    # for file in test_files:
    #     print('----------------------------------------')
    #     print("Start test with file: {}".format(file))
    #     file = "{}/test/{}".format(CUR_DIR, file)

    #     # get all functions
    #     functions = get_list_function_name(file)
    #     print("     List functions:")
    #     for i in functions:
    #         print("         - {}".format(i))

    #     # get all class
    #     classes = get_list_class_name(file)
    #     print("     List classes:")
    #     for i in classes:
    #         print("         - {}".format(i))

    #     # get all variable
    #     variables = get_list_variable_global(file)
    #     print("     List variables:")
    #     for i in variables:
    #         print("         - {}".format(i))

    #     # get all class methods
    #     class_methods = get_list_class_methods(file)
    #     print("     List class methods:")
    #     for i in class_methods:
    #         print("         {} - {}".format(i['name'], i['listMethods']))

    #     # get function stats
    #     functions_stats = get_list_function_stats(file)
    #     print("     List functions_stats:")
    #     for i in functions_stats:
    #         print("       Name: {} - Lines: {} - Var: {}".format(
    #             i['function'], i['lines'], i['variables']))

    #     # get file stats
    #     file_stats = get_file_stats(file)
    #     print("     File_stats:")
    #     print("       {} ".format(file_stats))

    # Example save in csv format
    file = "{}/test/{}".format(CUR_DIR, "test2.py")
    df = get_list_function_stats(file)
    print(df)
    df.to_csv('functions_stats.csv', index=False)



if __name__ == "__main__":
    ## python code_parser.py   main
    # import fire
    # fire.Fire()
    main()
