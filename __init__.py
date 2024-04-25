"""
Imports the following modules and classes:

Message
-------

>>> Message("Hello, World!",'success')
# prints "[#] Hello, World!" with the # in green
>>> Message("Function failed")
# prints "[#] Function failed" with the # in red. Type 'error' is inferred from the presence of the word 'fail' in the message
>>> Message.mute()
# all messages are no longer printed
# this allows you to silence all messages at once
>>> Message.unmute()
>>> print(Message.red("This is red"))
# Message also has static method that return colored strings, that you can then print

FancyIter
---------
>>> for i in FancyIter(list(range(100))):
>>>     pass
# print progress in % ad remaining time
# last print will be [#] Done! with # in green
>>> for i in FancyIter(list(range(100)), "Computation complete!"):
>>>     pass
# print progress in % ad remaining time.
# last print will be "[#] Computation complete!" with # color infered from the message
>>> for i in FancyIter(range(100)):
>>>     pass
# warning message, singe range has no method __len__, range is first converted to a list, wich might cause performance issues
# prefer the following syntax:
>>> for i in FancyIter(range(100),size=100):
>>>     pass

"""

from .fancy_print import Message
from .fancy_iterator import FancyIter