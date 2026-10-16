import pandas as pd 

House_Prices=pd.read_csv(r"C:/Users/dell/Downloads/House_Prices.csv")
print(House_Prices.isnull().sum())
print(House_Prices.columns)
print(House_Prices.mean(numeric_only=True))
House_Prices.fillna(House_Prices.mean(numeric_only=True), inplace=True)
print(House_Prices)
print(House_Prices.isnull().sum())
print(House_Prices.duplicated().sum())
House_Prices=House_Prices.drop_duplicates()

House_Prices = pd.get_dummies(
    House_Prices,
    columns=["SUBURB","NEAREST_STN"],
    dtype=int
)

print(House_Prices.head())