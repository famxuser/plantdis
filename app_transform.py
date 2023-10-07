#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os
import imageio
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow.keras import models, layers

#load model
model =load_model("d:/plandis/models/plantdisease.h5")

print('@@ Model loaded')
CLASS_NAMES = ['Alternaria_leaf_ blight_cotton_disease',
 'Angularleafspot_leaf_cotton_disease',
 'Foliar_cotton_leaf_disease',
 'Fusarium_cotton_leaf_disease',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus',
 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy',
 'diseased cotton leaf',
 'diseased cotton plant',
 'fresh cotton leaf',
 'fresh cotton plant']
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
    
  
    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
app_root = os.path.dirname(os.path.abspath(__file__))
@app.route("/predict", methods = ['GET','POST'])
def index():
    target = os.path.join(app_root, 'static/img/')
    if not os.path.isdir(target):
        os.makedirs(target)
def predict():
     if request.method == 'POST':
        image = request.files["file"]
        image_name = image.filename or ''
        destination = '/'.join([target, image_name])
        image.save(destination)
        image_name = np.array(
            Image.open(image_name).convert("RGB").resize((256, 256)) # image resizing
        )

        image_name = image_name/255 # normalize the image in 0 to 1 range

        img_array = tf.expand_dims(imgage_name, 0)
            
        
        predictions = model.predict(img_array)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        print("@@ Predicting class......")
        print(predicted_class)
        
              
        return render_template("healthy_plant.html",pred1_output = predicted_class,confidence=confidence, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,) 
    
    
