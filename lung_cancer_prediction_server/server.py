import numpy as np # linear algebra
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

app = Flask(__name__)
CORS(app)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


#############################################
#IMPORT NECESSARY LIBRARIES
#############################################

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#############################################
#LOAD THE DATASET
#############################################
df=pd.read_csv("/Users/pkamburu/IUNI/ECC-Project/data/lungcancerdata.csv")


#############################################
#BASIC DATA EXPLORATION
#############################################
df.head()

#############################################
#Dataset ShapeDataset Shape
#############################################
df.shape

#############################################
#Dataset Information
#############################################
df.info()

#############################################
#Statistics
#############################################
df.describe()


#############################################
#4. DATA PREPROCESSING
#############################################
#missing values
df.isnull().sum()

#Label Encoding
from sklearn.preprocessing import LabelEncoder,StandardScaler

label_encoder = LabelEncoder()

categorical_columns = ['Level']

# Apply label encoding to each categorical column

for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])


#removing the irrelevant features
df=df.drop(['Patient Id'],axis=1)

#Define features and the target variable
# Split the data into features and target

X=df.drop(['Level'],axis=1)
y=df['Level']


#############################################
#5. DATA VISUALIZATION
#############################################

#Correlation Heatmap
plt.figure(figsize=(20, 20))

df = df.drop(['index'], axis=1 )


# Create a correlation matrix
correlation_matrix = df.corr()

# Adjust font size
sns.set(font_scale=1)

# Set background style
sns.set_style("whitegrid")

# Create the heatmap without the index column
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=.5, square=True)


# Set title
plt.title("Correlation Heatmap", fontsize=18)
plt.xticks(rotation=45)


# # Display the plot
# plt.show()



#############################################
#6. DATA SPLITTING
#############################################

from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



#############################################
#7. MODEL BUILDING
#############################################


#Model Selection
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)


#Model Training
model.fit(X_train, y_train)

# Make predictions on the test set

y_pred = model.predict(X_test)


#############################################
#8. EVALUATION
#############################################
from sklearn.metrics import accuracy_score, classification_report

#Evaluate the model

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")

#Classification Report
print(classification_report(y_test, y_pred))

import pandas as pd

def getResults():
    # Creating a DataFrame with new input data
    new_data = pd.DataFrame({
        'index': [1],
        'Age': [25],
        'Gender': [0],  # Assuming 0 for Male, 1 for Female
        'Air Pollution': [3],
        'Alcohol use': [2],
        'Dust Allergy': [1],
        'OccuPational Hazards': [2],
        'Genetic Risk': [2],
        'chronic Lung Disease': [2],
        'Balanced Diet': [2],
        'Obesity': [2],
        'Smoking': [2],
        'Passive Smoker': [2],
        'Chest Pain': [2],
        'Coughing of Blood': [2],
        'Fatigue': [2],
        'Weight Loss': [2],
        'Shortness of Breath': [2],
        'Wheezing': [2],
        'Swallowing Difficulty': [2],
        'Clubbing of Finger Nails': [1],
        'Frequent Cold': [2],
        'Dry Cough': [2],
        'Snoring': [2],
        'Level': ['High']
    })

    # Assuming new_data is a DataFrame with the same structure as your training data
    # Check if 'Level' column exists before dropping it
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Assuming new_data is a DataFrame with the same structure as your training data
    # Check if 'Level' column exists before dropping it
    if 'Level' in new_data.columns:
        new_data_features_only = new_data.drop('Level', axis=1)

        # Use the already fitted scaler to transform the new data
        X_new_data_preprocessed = scaler.transform(new_data_features_only)

        # Set feature names to X_new_data_preprocessed
        X_new_data_preprocessed = pd.DataFrame(X_new_data_preprocessed, columns=new_data_features_only.columns)

        # Use predict_proba to get probability estimates
        y_new_data_probabilities = model.predict_proba(X_new_data_preprocessed)

        # Assuming there are two classes (0 and 1), you can get the probability of class 1
        # Replace 1 with the actual index of the positive class in your case
        lung_cancer_probability = y_new_data_probabilities[:, 1]

        return lung_cancer_probability
    else:
        return "Bad request", 400

@app.route('/getdata', methods=['GET'])
def get_data_endpoint():
    try:
        resp = getResults()  # Assuming getResults returns a NumPy array
        resp_value = resp.item()  # Extract the single value from the array
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return "Bad request", 400
    else:
        return jsonify(result=resp_value)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=9000)









