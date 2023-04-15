COLORS = {
    "Absolute Zero": "#0048ba","AliceBlue": "##f0f8ff",
    "Baby Blue": "#89cff0","Baby Pink": "#f4c2c2",
    "Cadet Grey": "#91a3b0","CadetBlue1": "#98f5ff",
    "Dark Sky Blue": "#8cbed6","DarkOrchiz": "#9932cc",
    "Earth Yellow": "#e1a95f","Electric Blue": "#7df9ff",
}
print(COLORS)

while True:
    color_name = input('Choice color:').strip().upper()
    if not color_name:
        break
    try:
        color_code = COLORS[color_name]
        print(f"{color_code}")
    except KeyError:
        print(f"Unable to find color name: {color_name}")