python_glossary = {
    "variable": "A variable in Python is a named location in memory that can store a value. Variables are used to store data that you want to use later in your program. They can be used to store numbers, strings, lists, dictionaries, and other data types.",
    "string": "A string in Python is a sequence of characters. It is a data type that can be used to store text. Strings are created using quotation marks, either single or double.",
    "list": "A list in Python is a data structure that can store a collection of values. The values in a list can be of any type, and the order of the values in the list is important. Lists are created using square brackets, and the values in the list are separated by commas",
    "dictionary": "A dictionary in Python is a data structure that stores a collection of key-value pairs. The keys are unique, and the values can be of any type. Dictionaries are created using curly braces, and the keys and values are separated by colons.",
    "condition": "A condition in Python is an expression that evaluates to a Boolean value, which is either True or False. Conditions are used in control flow statements, such as if statements and while loops, to determine which code to execute.",
    "keyword": "A reserved word in Python that has a special meaning to the interpreter.",
    "operator": "A symbol that performs a specific operation on one or more operands.",
    "data type": "The type of data that a variable can store.",
    "statement": "A complete instruction that the interpreter can execute.",
    "expresion": "A combination of values, variables, and operators that evaluates to a single value.",
}

for key, value in python_glossary.items():
    print(f'\nA/(an) "Python {key}" is:\n\t{value}')
