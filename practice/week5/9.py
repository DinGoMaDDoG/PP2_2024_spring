import re

def replF(match_obj):
    return match_obj.group('X') + " " + match_obj.group('Y')

def test(txt, pattern):
    result = re.sub(pattern,replF, txt)
    print(result)
    
txt=input()
pattern = r'(?P<X>[a-zA-Z])(?P<Y>[A-Z])'
test(txt,pattern)
