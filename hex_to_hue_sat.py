import colorsys


def get_hex(val):
    h = hex(val)
    r = int(h[2:4], 16)
    g = int(h[4:6], 16)
    b = int(h[6:8], 16)
    return r, g, b


def from_rgb_hex(r, g, b):
    h = hex(r)[2:] + hex(g)[2:] + hex(b)[2:] + '0'
    print(hex(b))
    return h




def convert_to_hue_sat(r,g,b):
    print(r,g,b)
    hue, sat, val = colorsys.rgb_to_hsv(r, g, b)
    return hue*255, sat*255, val*255


def from_hue_sat_convert_to_rgb(hue, sat, val):
    hue, sat, val = hue/255, sat/255, val/255
    r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
    return int(r), int(g), int(b)


if __name__ == "__main__":
    r, g, b = get_hex(16766720)
    hue, sat, val = convert_to_hue_sat(r, g, b)

    print(hue, sat, val)
    r,g,b = from_hue_sat_convert_to_rgb(hue, sat, val)
    print(r,g,b)
    hex_val = from_rgb_hex(r,g,b)

    print(int(hex_val, 16))
