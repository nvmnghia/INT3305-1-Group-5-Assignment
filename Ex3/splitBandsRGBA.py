from PIL import Image

imgSplit = Image.open(r'house.png')
imgSplit.load()
r, g, b, a = imgSplit.split()
r.save("redBand.png")
g.save("greenBand.png")
b.save("blueBand.png")
a.save("alphaBand.png")
