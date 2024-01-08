import re

# Your string representation
data_str = '[city_id=0001 user_id="0001"]'

# Extract key-value pairs using regular expressions
pairs = re.findall(r'(\w+)="?(\w+)"?', data_str)

print(pairs)
# Convert pairs to a dictionary
result = dict(pairs)
print(result)
