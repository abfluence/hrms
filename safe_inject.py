import sys, re

path    = r'C:\Users\hr\OneDrive\Documents\AB fluence website\hr dashboard.html'
js_path = r'C:\Users\hr\OneDrive\Documents\AB fluence website\func_code.js'

content  = open(path,   'r', encoding='utf-8').read()
new_code = open(js_path,'r', encoding='utf-8').read()

INIT_MARKER = '// \u2550'*1  # just to avoid encoding issues — search inline below
INIT_MARKER = '// \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n// INIT\n// \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\n'

idx = content.find(INIT_MARKER)
if idx == -1:
    print('ERROR: INIT marker not found')
    sys.exit(1)

print('INIT at char:', idx)

result = content[:idx] + new_code + '\n' + content[idx:]

body_count = result.count('<body')
print('body tags:', body_count)
print('lines:', result.count('\n'))

for fn in ['renderKanban','renderClientTable','renderBrandProjects','saveNewClient','loadAll','saveAll']:
    print(fn + ':', fn in result)

if body_count == 1:
    open(path,'w',encoding='utf-8').write(result)
    print('DONE')
else:
    print('ABORTED - body count wrong')
