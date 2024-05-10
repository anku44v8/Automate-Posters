# Import Libraries
import os
import pandas as pd
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from utils_img import add_text_to_image,add_overlay_image,add_placename_to_image

# FilePaths
imagePath = "C:\\Users\\ankus\\Documents\\G-Map\\Birthdays\\Data\\Images"
templatePath = "C:\\Users\\ankus\\Documents\\G-Map\\Birthdays\\Data\\BirthdayTemp.jpg"
dataPath = "C:\\Users\\ankus\\Documents\\G-Map\\Birthdays\\Data"
outputPath = "C:\\Users\\ankus\\Documents\\G-Map\\Birthdays\\Output"
namesFile = "Jan.csv"
monthName = namesFile.replace(".csv","")
outputPath = f"{outputPath}\\{monthName}"


# Create directory for output if not already present
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

# Read Names
dataPath = f"{dataPath}\\{namesFile}"
df_names = pd.read_csv(filepath_or_buffer=dataPath)

# Get list of file names in Images folder and add to dataframe
imageNames = os.listdir(path=imagePath)
nrows = df_names.shape[0]
len_imageNames = len(imageNames)

if nrows > len_imageNames:
    # number of times to repeat list
    rep_count = (nrows // len_imageNames) + 1
    imageNames *= rep_count
    imageNames = imageNames[:nrows]
else:
    imageNames = imageNames[:nrows]

df_names['Images'] = imageNames

### create the posters
for i in range(0,nrows):
    birthdate = df_names['Date'][i]
    name = df_names['Name'][i]
    name = name[:30]
    image_path = df_names['Images'][i]
    image_text = image_path.replace(".jpg","")
    image_path = f"{imagePath}\\{image_path}"
    image_out_path = f"{outputPath}\\{birthdate}"

    if not os.path.exists(image_out_path):
        os.makedirs(image_out_path)

    modified_image = add_text_to_image(templatePath, name,font_size=45,text_position=(343,430),text_color=(9,2,76))
    overlay_image = add_overlay_image(modified_image,image_path,resize = (743,560), overlay_position=(704,350),rotate_angle=7.3)
    final_image = add_placename_to_image(overlay_image,(500,50),image_text,(790,890),font_size=24,text_color=(255,255,255),rotate_angle=7.3)
    final_image_path = f"{image_out_path}\\{name}.jpg"
    final_image = final_image.convert('RGB')
    final_image.save(final_image_path)