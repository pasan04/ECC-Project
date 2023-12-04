
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#read the csv file
df = pd.read_csv('/Users/pkamburu/IUNI/ECC-Project/data/lungcancerdata.csv')

df.head(10)

#get describe the item.
df.describe()

df.describe(include = 'object')

df.shape


df.info()

df.columns


df.isna().sum()

df.value_counts('Level')

df = df.drop(['index'], axis = 'columns', inplace=False)
df = df.drop(['Patient Id'], axis = 'columns',inplace=False)

df.shape

# Plotting Scatter_Plot
#plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (10 , 6)
sns.scatterplot(df['Age'])
plt.title('Age')
plt.show()


df=df.replace({'Level':{'Low': 1, 'Medium': 2, 'High': 3}})

df.dtypes


sns.set()
plt.figure(figsize = (18,10))
sns.heatmap(df.corr(), cmap='YlGnBu', annot=True)
plt.title('Correlation Graph')
plt.show()


# Plotting the heatmap to check the correlation between the Target Label and other features
sns.heatmap(df.corr()[['Level']].sort_values(by='Level', ascending=False), vmin=-1, vmax=1, annot=True, cmap='YlGnBu')


sea = sns.FacetGrid(df, col = "Level", height = 4)
sea.map(sns.distplot, "Age")


#Before Train Test Split, split X(Input) & y(target) from the original Dataframe

X = df.drop(['Level'], axis = 'columns')
y = df['Level']

X.shape, y.shape


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


y_train.value_counts()


#Feature Scaling using StandardScaler

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_new_scaled = scaler.fit_transform(X_train)
X_test_new_scaled = scaler.transform(X_test)


#Applying Principal Component Analysis (PCA) for dimentionality Reduction

from sklearn.decomposition import PCA
pca = PCA(0.95)
X_train_pca = pca.fit_transform(X_train_new_scaled)
X_test_pca = pca.transform(X_test_new_scaled)


X_train_pca.shape, X_test_pca.shape


y_test.value_counts()


#Feature Scaling using StandardScaler

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_new_scaled = scaler.fit_transform(X_train)
X_test_new_scaled = scaler.transform(X_test)


#Applying Principal Component Analysis (PCA) for dimentionality Reduction

from sklearn.decomposition import PCA
pca = PCA(0.95)
X_train_pca = pca.fit_transform(X_train_new_scaled)
X_test_pca = pca.transform(X_test_new_scaled)

X_train_pca.shape, X_test_pca.shape


#Class Imbalance Handling using SMOTE

from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_pca, y_train)
X_test_resampled, y_test_resampled = smote.fit_resample(X_test_pca, y_test)


X_train_resampled.shape, y_train_resampled.shape


y_train_resampled.value_counts()


y_test_resampled.value_counts()


#############################################
#Model Building and Training
#############################################

#Import Necessary Algorithm for train the model

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


log_model = LogisticRegression()
dt_model = DecisionTreeClassifier()
rf_model = RandomForestClassifier(min_samples_split = 30)
svm_model = SVC()
gnb_model = GaussianNB()
knn_model = KNeighborsClassifier()


models = [
    log_model,
    dt_model,
    rf_model,
    svm_model,
    gnb_model,
    knn_model
]


from sklearn.model_selection import cross_val_score

def train_and_evaluate_models(models, X, y, cv):
    scores = {}
    for model in models:
        model_name = model.__class__.__name__
        cv_scores = cross_val_score(model, X, y, cv=cv)
        scores[model_name] = cv_scores.mean()
    return scores

cv_scores = train_and_evaluate_models(models, X_train_resampled, y_train_resampled, 20)



# Assuming 'scores' is the dictionary of scores
CV_scores_df = pd.DataFrame.from_dict(cv_scores, orient='index', columns=['Score'])

# Display the DataFrame
print(CV_scores_df)



#############################################
#FINAL EVALUATION
#############################################

best_models = [
    log_model,
    dt_model,
    rf_model,
    svm_model,
    knn_model
]

from sklearn.metrics import accuracy_score


def train_and_evaluate_models(models, X_train, y_train, X_test, y_test):
    scores = {}
    for model in models:
        model_name = model.__class__.__name__
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        score = model.score(X_test, y_test)
        scores[model_name] = {
            'accuracy_score': accuracy,
            'score': model.score(X_test, y_test)
        }
    return scores

scores = train_and_evaluate_models(best_models, X_train_resampled, y_train_resampled, X_test_resampled, y_test_resampled)


df_scores = pd.DataFrame(scores)


df_scores


from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def train_and_evaluate_model(model, X_train, y_train, X_test, y_test, cv):
    # Train the model using cross-validation on the training set
    cv_scores = cross_val_score(model, X_train, y_train, cv=cv).mean()

    # Fit the model on the entire training set
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Compute overall accuracy score on the entire dataset
    overall_accuracy = accuracy_score(y_test, y_pred)

    # Generate a classification report
    class_report = classification_report(y_test, y_pred)

    # Generate a confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Greens', cbar=False, xticklabels=['Low', 'Medium', 'High'],
                yticklabels=['Low', 'Medium', 'High'])
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title(f'Confusion Matrix of {model}')
    plt.show()

    # Output all the results
    print("Cross-Validation Score:", cv_scores)
    print("Overall Accuracy:", overall_accuracy)
    print("Classification Report:\n", class_report)

train_and_evaluate_model(log_model, X_train_resampled, y_train_resampled, X_test_resampled, y_test_resampled, 5)

train_and_evaluate_model(rf_model, X_train_resampled, y_train_resampled, X_test_resampled, y_test_resampled, 5)

train_and_evaluate_model(dt_model, X_train_resampled, y_train_resampled, X_test_resampled, y_test_resampled, 5)




