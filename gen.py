import cloudinary
import dotenv
import os

dotenv.load_dotenv()

KEY = os.environ.get('KEY')
SECRET = os.environ.get('SECRET')

def generate_image(name):
  cloudinary.config( 
    cloud_name = "jvss", 
    api_key = KEY, 
    api_secret = SECRET 
  )

  generated_image = cloudinary.CloudinaryImage("diwali.jpg").image(transformation=[
  {
    'effect': "blur:500"
    },
  {
    'border': "0px_solid_rgb:ffffff",
    'color': "#ffffff",
    'gravity': "center",
    'overlay': {
      'font_family': "montserrat",
      'font_size': 120,
      'font_weight': "bold",
      'text': "Happy%20Diwali"
      }
    },
  {
    'color': "#ffffff",
    'gravity': "south_east",
    'overlay': {
      'font_family': "montserrat",
      'font_size': 60,
      'font_weight': "bold",
      'text': f"%7E%20{name}"
      },
      'x': 30,
      'y': 30
   }
  ])

  return generated_image.split("\"")[1] # To parse url

