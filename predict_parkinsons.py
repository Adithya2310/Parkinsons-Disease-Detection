from skimage import feature
import joblib
import cv2

def quantify_image(image):
    features = feature.hog(image, orientations=9,
                           pixels_per_cell=(10, 10), cells_per_block=(2, 2),
                           transform_sqrt=True, block_norm="L1")
    
    return features


def predict_image(img,model):
    image=cv2.imread(img)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image=cv2.resize(image,(200,200))
    image = cv2.threshold(image, 0, 255,
                          cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    features=quantify_image(image)
    # load the saved model
    loadedModel=joblib.load(model)
    preds=loadedModel.predict([features])
    label="Parkinsons" if preds[0] else "Healthy"
    return label
