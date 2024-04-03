import colorgram

colors = colorgram.extract('image.jpg',6)
all_colors = []

for individual_color in colors:
    r = individual_color.rgb.r
    g = individual_color.rgb.g
    b = individual_color.rgb.b
    all_colors.append((r,g,b))


print(all_colors)