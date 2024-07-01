import re

S = input()
k = input()

matches = list(re.finditer(r"(?={})".format(re.escape(k)), S))

if matches:
    for match in matches:
        print(f"({match.start()}, {match.end() + len(k) - 1})")
else:
    print("(-1, -1)")