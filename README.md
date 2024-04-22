# Python - Variable Annotations

## Master

By: Emmanuel Turlay, Staff Software Engineer at Cruise
Weight: 1
Migrated to checker v2:
Your score will be updated as you progress.

## Concepts

Advanced Python

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- Validating code with mypy

## Requirements

- Editors: vi, vim, emacs
- Ubuntu 20.04 LTS, Python 3.9
- All files should end with a new line
- First line of files: `#!/usr/bin/env python3`
- Code style: pycodestyle
- All files executable
- Documentation for modules, classes, and functions
- Real sentence explanations for documentation

## Tasks

### 0. Basic annotations - add

Mandatory
Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

### 1. Basic annotations - concat

Mandatory
Write a type-annotated function `concat` that takes strings `str1` and `str2` and returns a concatenated string.

### 2. Basic annotations - floor

Mandatory
Write a type-annotated function `floor` taking a float `n` and returning its floor as an int.

### 3. Basic annotations - to string

Mandatory
Write a type-annotated function `to_str` taking a float `n` and returning its string representation.

### 4. Define variables

Mandatory
Define and annotate variables: `a` (int), `pi` (float), `i_understand_annotations` (bool), `school` (string).

### 5. Complex types - list of floats

Mandatory
Write a type-annotated function `sum_list` taking a list of floats and returning their sum as a float.

### 6. Complex types - mixed list

Mandatory
Write a type-annotated function `sum_mixed_list` taking a list of ints/floats, returning their sum as a float.

### 7. Complex types - string and int/float to tuple

Mandatory
Write a type-annotated function `to_kv` taking a string `k` and an int/float `v`, returning a tuple.

### 8. Complex types - functions

Mandatory
Write a type-annotated function `make_multiplier` taking a float `multiplier`, returning a function that multiplies a float by `multiplier`.

### 9. Let's duck type an iterable object

Mandatory
Annotate function `element_length` to take a list, return a list of tuples containing each element and its length.
