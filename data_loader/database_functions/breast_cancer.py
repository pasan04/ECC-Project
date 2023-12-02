from library import backend_util
import psycopg2

def add_data(id, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
             concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
             perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,
             radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,
             concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst):
    try:
        with backend_util.get_db_cursor() as cur:
            # Data insertion SQL statement
            data_insertion_query = """
            INSERT INTO breast_cancer_data (
                id, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
                perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,
                radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,
                concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            ) RETURNING id;
            """

            cur.execute(data_insertion_query, (id, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean,
                                               smoothness_mean, compactness_mean, concavity_mean, concave_points_mean,
                                               symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
                                               perimeter_se, area_se, smoothness_se, compactness_se, concavity_se,
                                               concave_points_se, symmetry_se, radius_worst, texture_worst,
                                               perimeter_worst, area_worst, smoothness_worst, compactness_worst,
                                               concavity_worst, concave_points_worst, symmetry_worst,
                                               fractal_dimension_worst))

            result = {}
            if cur.rowcount > 0:
                record_id = cur.fetchone()[0]
                result = {"record_id": record_id}
            return result
    except psycopg2.Error as ex:
        raise Exception(f"Error while adding data: {ex}")
