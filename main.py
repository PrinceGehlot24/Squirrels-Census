import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
white_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "cinnamon", "White"],
    "Count": [gray_squirrels, cinnamon_squirrels, white_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_color.txt")
