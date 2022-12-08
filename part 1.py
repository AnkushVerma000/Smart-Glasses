# import the following libraries
# will convert the image to text string
import pytesseract

# adds image processing capabilities
from PIL import Image
# import library to speech conversion
from gtts import gTTS

# play the converted audio
import os


# opening an image from the source path
img = Image.open('text15.png')

# describes image format in the output
print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)

# Language in which you want to convert text
language = 'en'

# Passing the text and language to the engine,
#  module that the converted text into audio
myobj = gTTS(text=result, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")


