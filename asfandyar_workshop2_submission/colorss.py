# - Create a two dimensional list (of strings)
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`

# - Print the array in the following format:
#   lime, forest green, oline, pale green, spring green
#   orange red, red, tomato
#   orchid, violet, pink, hot pink

colors = []
reds = ["orange red", "red", "tomato"]
greens = ["lime", "forest green", "olive", "pale green", "spring green"]
pinks = ["orchid", "violet", "pink", "hot pink"]

colors.append(reds)
colors.append(greens)
colors.append(pinks)

for i in colors:
    for j in i:
        print(j, end=", ")
    print("")
