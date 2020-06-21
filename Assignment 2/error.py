## module error
'''err(string).
Prints ’string’ and terminates program.30 Introduction to Python'''

import sys
def err(string):
    print(string)
    input('Press return to exit')
    sys.exit()