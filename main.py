from flask import Flask, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route('/generate_image')
def generate_image():
    img = Image.new('RGB', (500, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((150, 130), "Generated Image", fill=(0, 0, 0))
    
    # Save and send image
    img_path = "static/generated_image.png"
    img.save(img_path)
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
