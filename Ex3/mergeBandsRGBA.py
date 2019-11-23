from PIL import Image

r = Image.open(r'redBand.png')
r.load()
g = Image.open(r'greenBand.png')
g.load()
b = Image.open(r'blueBand.png')
b.load()
a = Image.open(r'alphaBand.png')
a.load()
imgMerge = Image.merge("RGBA", (r, g, b, a))
imgMerge.save('MergeImage.png')
