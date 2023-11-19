# read Taipei City Energy Poverty Cleaned.csv
# and convert it to json format
# output: Taipei City Energy Poverty Cleaned.json

"""
[input]
"Area","District","X2018income","X2018power","X2018datanum","X2019income","X2019power","X2019datanum","X2020income","X2020power","X2020datanum","power_per_house_2018","power_per_house_2019","power_per_house_2020"
"士林區","三玉里",3582996,2587782,2194,2949318,2455577,2192,2788618,2934344,2188,1179.48131267092,1120.24498175182,1341.10786106033


[output]
{
  "data": [
    {
      "name": ">40年",
      "data": [
        15742, 20453, 6060, 6410, 10855, 12653, 15154, 12984, 11563, 17647,
        20243, 12710
      ]
    },
    ...
}
"""

# %%
import pandas as pd

# read csv as df
df = pd.read_csv("Taipei City Energy Poverty Cleaned.csv")


# %%
# categories: list = ["北投區", "士林區", "內湖區", "南港區", "松山區", "信義區", "中山區", "大同區", "中正區", "萬華區", "大安區", "文山區" ]

# %%
# for each row in df, create a dict
# and append it to a list
data = []
year = 2018
for i, row in df.iterrows():
    data.append({
        "name": row["Area"],
        "data": [
            row[f"X{year}income"],
            row[f"power_per_house_{year}"]
        ]
    })
# %%

# wrap data as list in a pandas dict called data_dict
data_dict = pd.DataFrame({"data": data})

# %%

# dump to json use pd
# data should be a list, not index value pairs


with open(f"Taipei City Energy Poverty Cleaned_{year}.json", 'w', encoding='utf-8') as file:
    data_dict.to_json(file, orient="records", force_ascii=False)

# %%
