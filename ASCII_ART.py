from PIL import Image
img = Image.open(r"C:\Users\Asus\OneDrive\Pictures\Screenshots\Screenshot 2026-04-08 034543.png")
new_width = 150
new_height = 50
tiny_img = img.resize((new_width, new_height))
grayscale_img = tiny_img.convert("L")
pixel_data = list((grayscale_img.getdata()))
idk =[]

for i in pixel_data:
    j = int(i)
    if 0 <= j <= 25:
        i = " "
        idk.append(i)
    if 26 <= j <= 50:
        i = "."
        idk.append(i)
    if 51 <= j <= 75:
        i = ":"
        idk.append(i)
    if 76 <= j <= 100:
        i = "-"
        idk.append(i)
    if 101 <= j <= 125:
        i = "="
        idk.append(i)
    if 126 <= j <= 150:
        i = "+"
        idk.append(i)
    if 151 <= j <= 175:
        i = "*"
        idk.append(i)
    if 176 <= j <= 200:
        i = "#"
        idk.append(i)
    if 201 <= j <= 225:
        i = "%"
        idk.append(i)
    if 226 <= j <= 255:
        i = "@"
        idk.append(i)
final = "".join(idk)   
i = 0
while i < len(final):
    print(final[i:i+new_width])
    i = i + new_width
