import pandas as pd

new_s = pd.Series([10,20,30,40], index=["a","b","c","d"])
new_s

colors = ["red","orange","yellow","white"]
degrees = [30,40,50,60]
numbers = [11,12,13,14]

testing = {"colors": colors,"degrees": degrees,"numbers":numbers}

new_df = pd.DataFrame(testing, columns=["colors","degrees","numbers"],index=range(1,5))

#print(new_df)

df_csv = pd.read_csv("sample10.csv",low_memory=False)

#print(df_csv)

csvh=df_csv.head(6)
#print(csvh)

new_url = "https://en.wikipedia.org/wiki/Academy_Awards"
pd_url = pd.read_html(new_url, header=0, index_col=0)[3]

htmlh = pd_url.head(5)

#print(htmlh)

#print(df_csv.describe())

logs=df_csv.loc[df_csv["price"].argmax()][["Cars","price"]]

#print(logs)


new_df2 = pd.read_excel("demo.xlsx", sheet_name=0)

print(new_df2)