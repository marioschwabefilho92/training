string = "  xa xo xxxxxxxxaaaaaaaeeeexxxxb      "
print(string.strip(' xae'))

string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))