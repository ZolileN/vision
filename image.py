from PIL import Image, ImageDraw

def mask_image(image_file, boxes):
    img = Image.open(image_file)
    mask = Image.new("L", img.size, color=0)
    draw = ImageDraw.Draw(mask)
    for box in boxes:
        coords = [(box['x'], box['y']),
                  (box['x'] + box['width'],  box['y'] + box['height'])]
        draw.rectangle(coords, fill=255)
    img.putalpha(mask)
    img.save('/tmp/output.png')
