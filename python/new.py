dict1 = {'yojana': 100, 'dip': 50}
dict2 = {'asim': 50, 'sujal': 40}

merged = defaultdic(int)

for d in [dict1, dict2]:
    for k,v in d.items:
        merged[k]+=v
        
print(dict(merged))