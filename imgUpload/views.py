from django.shortcuts import render
from .forms import ImageUploadForm

# deep learning libraries required
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Create your views here.
def handle_uploaded_file(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
    return render(request, 'home.html')

def imageprocess(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])

        model = ResNet50(weights='imagenet')
        img_path = 'img.jpg'
        
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        # decode the results into a list of tuples (class, description, probability)
        # (one such list for each sample in the batch)
        print('Predicted:', decode_predictions(preds, top=3)[0])
        # Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]

        html = decode_predictions(preds, top=3)[0]
        res = []
        for e in html:
            res.append((e[1], np.round(e[2]*100, 2)))
        
        return render(request, 'result.html', {'res': res})

    return render(request, 'home.html')