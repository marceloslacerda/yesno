# yesno

Quite frequently I need to create simple CLI interfaces for the programs I
write, every time I end up creating a different set of functions that never
have a good set of satisfactory behaviours. For this reason I'm putting this
project publicly, so I can use the same library for those purposes and
improve it continusly.

Example:

    >>> import yesno
    >>> yesno.input_to_bool('Do you like pancakes', default='yes')
    Do you like pancakes[yes]? no
    False

## WARNING

In my projects I have switched to [conz](https://pypi.python.org/pypi/conz)
so this project is no longer going to be maintained.
