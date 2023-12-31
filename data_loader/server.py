"""
Purpose:
    This script used to insert items into the table

Outputs:
    - JSON object
Authors: Pasan Kamburugamuwa
"""
from flask import Flask
from flask_cors import CORS
from library import backend_util
import os
import pandas as pd
from database_functions import breast_cancer, lung_cancer


LOG_DIR = "/Users/pkamburu/IUNI/ECC-Project/log"
LOG_FNAME = "database_server.log"

app = Flask(__name__)
CORS(app)

def read_breast_cancer_csv_file_process():

    file_path = '/Users/pkamburu/IUNI/ECC-Project/data/breastcancerdata.csv'
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        breast_cancer.add_data(row['id'], row['diagnosis'], row['radius_mean'], row['texture_mean'], row['perimeter_mean'], row['area_mean'], row['smoothness_mean'], row['compactness_mean'], row['concavity_mean'], row['concave points_mean'], row['symmetry_mean'],
                               row['fractal_dimension_mean'], row['radius_se'], row['texture_se'], row['perimeter_se'], row['area_se'], row['smoothness_se'],row['compactness_se'], row['concavity_se'], row['concave points_se'], row['symmetry_se'], row['radius_worst'], row['texture_worst'],
                               row['perimeter_worst'], row['area_worst'], row['smoothness_worst'] ,row['compactness_worst'] ,row['concavity_worst'], row['concave points_worst'], row['symmetry_worst'], row['fractal_dimension_worst'])



def read_lung_cancer_csv_file_process():

    file_path = '/Users/pkamburu/IUNI/ECC-Project/data/lungcancerdata.csv'
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        lung_cancer.add_lung_cancer_data(row['Patient Id'], row['Age'], row['Gender'], row['Air Pollution'], row['Alcohol use'], row['Dust Allergy'], row['OccuPational Hazards'], row['Genetic Risk'],row['chronic Lung Disease'], row['Balanced Diet'],
                               row['Obesity'], row['Smoking'], row['Passive Smoker'], row['Chest Pain'], row['Coughing of Blood'], row['Fatigue'],row['Weight Loss'], row['Shortness of Breath'], row['Wheezing'], row['Swallowing Difficulty'], row['Clubbing of Finger Nails'], row['Frequent Cold'],
                               row['Dry Cough'], row['Snoring'], row['Level'])

if __name__ == '__main__':
    script_name = os.path.basename(__file__)
    logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)
    logger.info("-" * 50)
    logger.info(f"Begin script: {__file__}")

    read_lung_cancer_csv_file_process()
