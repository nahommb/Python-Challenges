import colorgram

colors = colorgram.extract('image.jpg',6)
all_colors = []

print(colors[0].rgb[0])