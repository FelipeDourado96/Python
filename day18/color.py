import colorgram

def color(amount_of_colors):
    rgb_colors = []
    image = colorgram.extract('image.jpg', amount_of_colors)
    for i in range(amount_of_colors):
        r = image[i].rgb.r
        g = image[i].rgb.g
        b = image[i].rgb.b
        color = (r, g, b)
        rgb_colors.append(color)
    print(rgb_colors)
    return rgb_colors

color(15)