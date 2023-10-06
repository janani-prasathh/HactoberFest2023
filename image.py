#create image
from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
width, height = 400, 200
image = Image.new("RGB", (width, height), "white")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Add text to the image
text = "Hello, Python!"
font = ImageFont.load_default()
text_width, text_height = draw.textsize(text, font=font)
x = (width - text_width) / 2
y = (height - text_height) / 2
draw.text((x, y), text, fill="black", font=font)

# Save the image to a file
image.save("my_image.png")

# Display the image (optional)
image.show()
