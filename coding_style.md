In Python, variable names follow the [snake_case](https://en.wikipedia.org/wiki/Snake_case) naming convention. This means that variable names should be all lower case initially, and an underscore should separate any potential need for multiple words in the name. While ignoring these naming conventions will not cause any issues for the script - Python could care less about what we call our things - other Python developers may get thrown off if they expect one set of rules but face others.

The main point here is that our code should be easy to follow and read. Every programmer has their style and preferences when it comes to writing code. There are even several style guides for Python, such as [PEP8](https://www.python.org/dev/peps/pep-0008/#type-variable-names), which describes certain types of variable or function definitions. Having a style guide is very important when we want someone to read the code we write. We usually write code so that someone can use it, benefit from it and possibly work on it or learn something new from it. Without a style guide, debugging, improving, or extending becomes immensely difficult. Of course, there are many other things besides the style guide that we as professional programmers need to pay attention to, such as code architecture, general principles for code quality, etc.

# From PEP8:

## Function and Variable Names

- Function names should be lowercase, with words separated by underscores as necessary to improve readability.

- Variable names follow the same convention as function names.

- mixedCase is allowed only in contexts where that’s already the prevailing style (e.g. threading.py), to retain backwards compatibility.


## Function and Method Arguments

- Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.

If a function argument’s name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)
Method Names and Instance Variables

Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a. (An insistent user could still gain access by calling Foo._Foo__a.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

Note: there is some controversy about the use of __names (see below).
Constants

Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.
