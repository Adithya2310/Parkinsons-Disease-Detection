# Parkinsons-Disease-Detection
Parkinsons Disease Detection using Spiral and Wave images from the patients. Traditionally the disease is detected using MRI and SPECT scans, but these techniques have
many shortcomings and arent accessible to common people. This project tries to overcome those Issues by trying to detect the disease using minimum eqiupment. It uses 
Handwriting analysis to detect the disease using Machine Learning with a accuracy of 86%.

## Technology used 
1) It uses RandomForestClassifier and XGBoost Algorithms as the models
2) Confusion Matrix and ROC Curve to evaluate the accuracy of the model
3) It use Flask in BackEnd and Jinja2 template for the front end

## Methodology
1. Data Collection: Gather a dataset of spiral and wave drawings from individuals, including 
both healthy individuals and those diagnosed with Parkinson's disease. Each participant should 
be asked to draw spirals on a digitizing tablet or touchpad.
2. Preprocessing: Clean and preprocess the spiral and wave images to remove noise, normalize 
the size, and convert them into a standardized format. Techniques such as smoothing, resizing, 
and cropping can be applied to ensure consistency.
3. Feature Extraction: Extract relevant features from the preprocessed spiral and wave 
images. Some commonly used features for spiral analysis include curvature, pen pressure, 
stroke length, and direction changes using Hog feature extraction.
4. Model Training: Split the dataset into training and testing sets. Apply machine learning 
algorithms such as random forest classifier to train a classification model using the training set. 
The input features will be the extracted spiral and wave image features.
5. Model Evaluation: Evaluate the trained model using the testing set to assess its 
performance. Common evaluation metrics for classification tasks include accuracy, precision, 
recall, roc curve.
6. Model Validation: Validate the trained and optimized model using an independent dataset 
or through clinical trials. This step helps to assess the model's performance in real-world 
scenarios and verify its reliability.
7. Deployment: Once the model is validated, it can be deployed in a practical setting for 
Parkinson's disease detection by creating a user-friendly interface where 
clinicians or patients can input spiral and wave drawings, and the model will provide a 
prediction regarding the likelihood of Parkinson's disease.

## Setup
1) Install all the requirements form the requirement folder
2) run the jupyter Notebook for testing the model and accuracy
3) Use the 'Python main.py' for Starting the Flask application
4) Open localhost:5000 to view the website in your local environment.


