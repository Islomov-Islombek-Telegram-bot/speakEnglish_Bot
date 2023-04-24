import json

my_str = ''

try:
    result = json.loads(my_str)
except json.decoder.JSONDecodeError:
    # 👇️ this runs
    print('The string does NOT contain valid JSON')