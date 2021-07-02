### CODE PARSER
code_parser.py

### List functions

- get_list_function_name(file_path)
- get_list_class_name(file_path)
- get_list_class_methods(file_path)
- get_list_variable_global(file_path)
- get_list_function_stats(file_path)
- get_file_stats(file_path)

### Detail

List functions:
- get_list_function_name(file_path)
    The function use to get all functions of the python file

    Args:
        IN: file_path         - the file path input
        OUT: list_functions   - List all python functions in the input file

    Example Output:
        `['func1', 'func2']`


- get_list_class_name(file_path):
    The function use to get all classes of the python file

    Args:
        IN: file_path         - the file path input
        OUT: list_classes     - List all python classes in the input file

    Example Output:
        `['Class1', 'Class1']`


- get_list_class_methods(file_path):
    The function use to get all classes and all methods in this class of the python file

    Args:
        IN: file_path         - the file path input
        OUT: An array of class info [{dict}, {dict}, ...]
    
    Example Output:
    ```
        [
            {"name": "Class1", "listMethods": ["method1", "method2", "method3"]},
            {"name": "Class2", "listMethods": ["method4", "method5", "method6"]},
        ]
    ```


- get_list_variable_global(file_path):
    The function use to get all global variable of the python file

    Args:
        IN: file_path         - the file path input
        OUT: list_var         - Array of all global variable

    Example Output:
        `['Var1', 'Var2']`


- get_list_function_stats(file_path):
    The function use to get functions stars

    Args:
        IN: file_path         - the file path input
        OUT: Array of functions, lines of the function, and variable in function
    Example Output:
    ```
        [
            {"function": "function_name1", "lines": 20, "variables": ["a", "b", "c"]},
            {"function": "function_name2", "lines": 30, "variables": []},
        ]
    ```


- get_file_stats(file_path):
    The function use to get file stars

    Args:
        IN: file_path         - the file path input
        OUT: Dict of file stars
    Example Output:
    ```
        {
            "total_functions": 22,
            "avg_lines" : 110.2,
            "total_class": 3
        }
    ```

### Example code

```
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))

    test_files = ['test.py', 'test2.py', 'test3.py', "model_gefs.py", "model_sklearn.py"]

    for file in test_files:
        print('----------------------------------------')
        print("Start test with file: {}".format(file))
        file = "{}/test/{}".format(CUR_DIR, file)

        # get all functions
        functions = get_list_function_name(file)
        print("     List functions:")
        for i in functions:
            print("         - {}".format(i))
            
        # get all class
        classes = get_list_class_name(file)
        print("     List classes:")
        for i in classes:
            print("         - {}".format(i))
    
        # get all variable
        variables = get_list_variable_global(file)
        print("     List variables:")
        for i in variables:
            print("         - {}".format(i))

        # get all class methods
        class_methods = get_list_class_methods(file)
        print("     List class methods:")
        for i in class_methods:
            print("         {} - {}".format(i['name'], i['listMethods']))

        # get function stats
        functions_stats = get_list_function_stats(file)
        print("     List functions_stats:")
        for i in functions_stats:
            print("       Name: {} - Lines: {} - Var: {}".format(i['function'], i['lines'], i['variables']))

        # get file stats
        file_stats = get_file_stats(file)
        print("     File_stats:")
        print("       {} ".format(file_stats))
```
