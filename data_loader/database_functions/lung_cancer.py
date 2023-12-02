from library import backend_util
import psycopg2

def add_lung_cancer_data(patient_id,age,gender,air_pollution,alcohol_use,
                    dust_allergy,occupational_hazards,genetic_risk,chronic_lung_disease,balanced_diet,
                    obesity,smoking,passive_smoker,chest_pain,coughing_of_blood,
                    fatigue,weight_loss,shortness_of_breath,wheezing,swallowing_difficulty,
                    clubbing_of_finger_nails,frequent_cold,dry_cough,snoring,level):
    try:
        with backend_util.get_db_cursor() as cur:
            # Data insertion SQL statement
            data_insertion_query = """
            INSERT INTO breast_cancer_data (
                    patient_id,age,gender,air_pollution,alcohol_use,
                    dust_allergy,occupational_hazards,genetic_risk,chronic_lung_disease,balanced_diet,
                    obesity,smoking,passive_smoker,chest_pain,coughing_of_blood,
                    fatigue,weight_loss,shortness_of_breath,wheezing,swallowing_difficulty,
                    clubbing_of_finger_nails,frequent_cold,dry_cough,snoring,level
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            ) RETURNING patient_id;
            """
            cur.execute(data_insertion_query, (patient_id, age, gender, air_pollution, alcohol_use,
                                               dust_allergy,occupational_hazards, genetic_risk, chronic_lung_disease, balanced_diet,
                                               obesity, smoking, passive_smoker, chest_pain,coughing_of_blood,
                                               fatigue, weight_loss, shortness_of_breath, wheezing,swallowing_difficulty,
                                               clubbing_of_finger_nails, frequent_cold, dry_cough,snoring, level))

            result = {}
            if cur.rowcount > 0:
                record_id = cur.fetchone()[0]
                result = {"record_id": record_id}
            return result
    except psycopg2.Error as ex:
        raise Exception(f"Error while adding data: {ex}")