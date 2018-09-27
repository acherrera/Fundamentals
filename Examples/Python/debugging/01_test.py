"""
Showing how to debug
if you run program with python3 -m pdb file_name.py the debugger will start
from the beginning
"""
# import debugger
import pdb


def combine(s1, s2):
    s3 = s1 + s2 + s1
    s3 = '"' + s3 + '"'
    return s3

a = "aaa"
# Start the debugger here
pdb.set_trace()
b = "bbb"
c = "ccc"

final = combine(a,b)
print(final)

# Use 'n' to go to next line in debugging
# Use Enter to repoeat the previous. 
# n - next
# q - quit
# p !!x_variable- print x_variable
# c - continue program. Not debug pausing
# l - list where program is
# s - same as n, except will show subroutine exection (functions)
# r - "continue till return". Execute rest of subrutine.
# s1 = "bbb" - set var s1 to value "bbb" in the program
# !n = "bbb" - set var n to "bbb". Otherwise program get's confused.
