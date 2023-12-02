
-- create the breast cancer data table
create table breast_cancer_data(
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
        fractal_dimension_worst float
);


-- create the lung cancer data table
create table lung_cancer_data(
        patient_id VARCHAR(40),
        age int NOT NULL,
        gender int,
        air_pollution int,
        alcohol_use int,
        dust_allergy int,
        occupational_hazards int,
        genetic_risk int,
        chronic_lung_disease int,
        balanced_diet int,
        obesity int,
        smoking int,
        passive_smoker int,
        chest_pain int,
        coughing_of_blood int,
        fatigue int,
        weight_loss int,
        shortness_of_breath int,
        wheezing int,
        swallowing_difficulty int,
        clubbing_of_finger_nails int,
        frequent_cold int,
        dry_cough int,
        snoring int,
        level varchar(200)
);


