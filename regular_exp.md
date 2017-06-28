# Regular Expressions in Python
## Introduction
The `re` module was added in Python 1.5, and provides **Perl-style** regular expression patterns. Earlier versions of Python came with the `regex` module, which provided **Emacs-style** patterns. The regex module was removed completely in Python 2.5.

## Using Regular Expressions
### Compiling regular expressions
Regular expressions are compiled into pattern objects, There are  methods for various operations such as searching for pattern matches or performing string substitutions.
```python
import re
p = re.compile('ab*')
p  
```
