import pandas as pd
with open('bfa_girls_p_exp.txt','r') as f:
    txt = f.readlines()

bfa_boys_p_exp = []

for row in txt:
    row = row.split('\t') 
    new_row = []
    for item in row:
        item = item.rstrip("\n")
        new_row.append(item)
    bfa_boys_p_exp.append(new_row)

columns = bfa_boys_p_exp.pop(0)

df = pd.DataFrame(bfa_boys_p_exp, columns=columns)
df.to_csv('bfa_girls_p_exp.csv')