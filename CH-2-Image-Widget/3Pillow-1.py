from PIL import Image

img1 = Image.open("C:\Users\HP\Downloads\profile.png")
reImg = img1.resize((920, 920))
reImg.save("re.png", "png")

