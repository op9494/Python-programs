def camel(word):
        import re
        return ''.join(x.capitalize() or ' ' for x in word.split(' '))
l=input()
print(camel(l))
