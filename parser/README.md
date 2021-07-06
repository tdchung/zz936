### CODE PARSER
code_parser.py






### Example 
```

python code_parser.py       

```






### Example code

Example1:
```

    # Example save in csv format
    file = "{}/test/{}".format(CUR_DIR, "keys.py")
    df = get_list_function_stats(file)
    print(df)
    if df is not None:
        df.to_csv('functions_stats1.csv', index=False)

    df = get_list_class_stats(file)
    print(df)
    if df is not None:
        df.to_csv('class_stats1.csv', index=False)

    df = get_list_method_stats(file)
    print(df)
    if df is not None:
        df.to_csv('method_stats1.csv', index=False)



```







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

