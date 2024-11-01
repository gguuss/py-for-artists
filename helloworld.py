# Printing is very useful for debugging when working in command
# workflows
print('This is a print statement\n')

# Concatenation requires casting
# The str(8+10) will turn the integer (number) into a string
print('This is a print statement ' + 'with ' + str(8+10) + ' math')

'''
You can create comments with multiline continuations to avoid prefixing
all of the lines with the hash # symbol
'''

hello_var = 'A variable'
print(hello_var)

hello_var += ' - you can add to the string of the variable with the += operator'

print(hello_var)

# This is a variable created from a multiline continuation
# Note that it is adding the (invisible) newlines after between the string
# You could avoid the newlines as hello_world = '''Hello, this is a variable'''
hello_world = '''
Hello, this is a variable
'''

print(hello_world)