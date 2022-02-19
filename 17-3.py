#3
import re

s = 'The ghost that says boo haunts the loo'
matches = re.findall(".oo", s, re.IGNORECASE)
print(matches)
