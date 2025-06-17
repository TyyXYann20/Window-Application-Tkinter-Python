from PIL import Image

img1 = Image.open("D:/PyGUI/CH-2-Image-Widget/football.png")
# reImg = img1.resize((320, 320))
# reImg.save("re.png", "png")

rotated = img1.rotate(180)
rotated.show()