"""
Purpose:
    Contains functions used to add data to breast_cancer table

Inputs:
    None

Outputs:
    None

Authors: Pasan Kamburugamuwa & Matthew DeVerna
"""
from flask import Flask
from library import backend_util

app = Flask(__name__)

def add_data(id, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,compactness_mean,
             concavity_mean, concave_points_mean, symmetry_mean,fractal_dimension_mean, radius_se, texture_se, perimeter_se,
             area_se,smoothness_se, compactness_se, concavity_se,concave_points_se,symmetry_se, radius_worst,  texture_worst, perimeter_worst,
             area_worst,smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst ):
    """
    Add data to the breast_cancer database table.

    Parameters
    -----------
        id int NOT NULL,
        diagnosis char(10) NOT NULL,
        radius_mean float,
        texture_mean float,
        perimeter_mean float,
        area_mean float,
        smoothness_mean float,
        compactness_mean float,
        concavity_mean float,
        concave_points_mean float,
        symmetry_mean float,
        fractal_dimension_mean float,
        radius_se float,
        texture_se float,
        perimeter_se float,
        area_se float,
        smoothness_se float,
        compactness_se float,
        concavity_se float,
        concave_points_se float,
        symmetry_se float,
        radius_worst float,
        texture_worst float,
        perimeter_worst float,
        area_worst float,
        smoothness_worst float,
        compactness_worst float,
        concavity_worst float,
        concave_points_worst float,
        symmetry_worst float,
        fractal_dimension_worst float,
    Returns
    -----------
    result (dict): {'id': record_id}
    """
    with backend_util.get_db_cursor() as cur:
        try:
            # Table creation SQL statement
            table_creation_query = """
            CREATE TABLE breast_cancer_data (
                id SERIAL PRIMARY KEY,
                diagnosis CHAR(10) NOT NULL,
                radius_mean FLOAT,
                texture_mean FLOAT,
                perimeter_mean FLOAT,
                area_mean FLOAT,
                smoothness_mean FLOAT,
                compactness_mean FLOAT,
                concavity_mean FLOAT,
                concave_points_mean FLOAT,
                symmetry_mean FLOAT,
                fractal_dimension_mean FLOAT,
                radius_se FLOAT,
                texture_se FLOAT,
                perimeter_se FLOAT,
                area_se FLOAT,
                smoothness_se FLOAT,
                compactness_se FLOAT,
                concavity_se FLOAT,
                concave_points_se FLOAT,
                symmetry_se FLOAT,
                radius_worst FLOAT,
                texture_worst FLOAT,
                perimeter_worst FLOAT,
                area_worst FLOAT,
                smoothness_worst FLOAT,
                compactness_worst FLOAT,
                concavity_worst FLOAT,
                concave_points_worst FLOAT,
                symmetry_worst FLOAT,
                fractal_dimension_worst FLOAT
            );
            """

            cur.execute(table_creation_query, (id, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,compactness_mean,
             concavity_mean, concave_points_mean, symmetry_mean,fractal_dimension_mean, radius_se, texture_se, perimeter_se,
             area_se,smoothness_se, compactness_se, concavity_se,concave_points_se,symmetry_se, radius_worst,  texture_worst, perimeter_worst,
             area_worst,smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst ))
            if cur.rowcount > 0:
                id = cur.fetchone()[0]
                result = {"record_id": id}
            return result
        except Exception as ex:
            raise Exception(ex)