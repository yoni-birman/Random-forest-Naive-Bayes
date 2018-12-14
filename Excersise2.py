
files = [
    'iris',
    #'immuno',
    #'phishing',
    #'wine',
    #'brcancer',
    #'yeast',
    #'occupancy',
    #'magic04',
    #'banknote',
    'seeds'
]

print(fname)
for fname in files:
    print("------- %s -------" % fname)
df = pd.read_csv("%s.csv" % fname)
    #evalute_model("data\\%s.csv" % fname)
df.head()
print(df)