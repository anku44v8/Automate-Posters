from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, font_size=20, text_position=(10, 10), text_color=(0, 0, 0)):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.truetype("MyriadPro-Semibold.ttf", font_size)
    
    # Get bounding box of text
    text_bbox = draw.textbbox(text_position, text, font=font)

    # Calculate centered position
    text_width = text_bbox[2] - text_bbox[0]
    text_position = (text_position[0] - text_width // 2, text_position[1])

    # Add text onto the image
    draw.text(text_position, text, fill=text_color, font=font)
    
    # Save the modified image
    return image

def add_overlay_image(background_image, overlay_image_path, resize, overlay_position=(0, 0), rotate_angle = 0):
    # Open the overlay image
    overlay_image = Image.open(overlay_image_path)

    if overlay_image.mode != 'RGBA':
        overlay_image = overlay_image.convert('RGBA')

    if resize is not None:
        overlay_image = overlay_image.resize(resize)

    if rotate_angle != 0:
        overlay_image = overlay_image.rotate(rotate_angle, resample=Image.BICUBIC,expand=1)
    
    mask_image = overlay_image.split()[3]

    if background_image.mode != 'RGBA':
        background_image = background_image.convert('RGBA')

    background_image.paste(overlay_image,overlay_position,mask_image)

    # Save the modified image
    return background_image

def add_placename_to_image(background_image, canvas_size, text, overlay_position, font_size=20, text_position=(10, 10), text_color=(0, 0, 0),rotate_angle=0):
    # Create a blank canvas
    canvas = Image.new("RGBA", canvas_size, (255,255,255,0))
    
    # Create a drawing object
    draw = ImageDraw.Draw(canvas)
    
    # Load a font
    font = ImageFont.truetype("MyriadPro-Semibold.ttf", font_size)
    
    # Add text onto the canvas
    draw.text(text_position, text, fill=text_color, font=font)

    if rotate_angle != 0:
        canvas = canvas.rotate(rotate_angle, resample=Image.BICUBIC,expand=1)

    if background_image.mode != "RGBA":
        background_image = background_image.convert("RGBA")

    mask_image = canvas.split()[3]
    background_image.paste(canvas,overlay_position,mask_image)

    return background_image

# # Example usage
# image_path = "BirthdayTemp.jpg"
# text = "Ankush"
# modified_image = add_text_to_image(image_path, text,font_size=45,text_position=(343,430),text_color=(9,2,76))
# # modified_image.show()
# overlay_image_path = "Aguada Fort, Goa.jpg"
# overlay_image = add_overlay_image(modified_image,overlay_image_path,resize = (743,560), overlay_position=(704,350),rotate_angle=7.3)
# # overlay_image.show()
# place_name = "Aguada Fort, Goa"
# final_image = add_placename_to_image(overlay_image,(500,50),place_name,(790,890),font_size=24,text_color=(255,255,255),rotate_angle=7.3)
# final_image = final_image.convert('RGB')
# final_image.save("sample.jpg")