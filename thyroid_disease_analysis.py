# -*- coding: utf-8 -*-
"""Thyroid disease analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18KJMT9n15AHzCFbZKwjtl8RL0X0KYCbs

##*Importing Libraries*##
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""##*Mounting the google drive*##"""

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/Thyroid Disease analysis /Thyroid_Diff.csv")

df

df.isnull().sum()

"""## ***Making the columns more understandable***"""

df.rename(columns = {
    'Hx Smoking': 'History of Smoking',
    'Hx Radiothreapy' : 'History of Radiotherapy',
    'Pathology' : 'Type of cancer',
    'Focality' : 'Number of tumors',
    'T' : 'Tumor',
    'N' : 'Lymph Nodes',
    'M' : 'Metastasis'
    },
       inplace = True   )

df.describe()

df.info()

df['Stage'].unique()

df['Stage'].replace({'I': 'First-Stage(I)',
                     'II':'Second-Stage(II)',
                     'III' : 'Third-Stage(III)',
                     'IVA' : 'Spreaded in distinct part of body(IVA)',
                     'IVB' : 'Spreaded in more than 1 body part(IVB)'

                     }, inplace = True)

df['Adenopathy']. unique()

df['Adenopathy'].replace({'No' : 'No Lympth Adenopathy' ,
                          'Left' : 'Left Side Body Adenopathy' ,
                          'Right' : 'Right Side Body Adenopathy' ,
                          'Extensive' : 'Extensive and Widespread',
                          'Bilateral' : 'Both side of the body',
                          'Posterior' : 'On neck / back of head'}, inplace = True)

df['Tumor'].unique()

df['Tumor'].replace({'T1a' : 'tumor  is 1 cm or smaller' ,
                      'T1b' : 'tumor > 1 cm and < 2 cm' ,
                     'T2' : 'tumor > 2 cm and < 4 cm' ,
                     'T3a' : 'tumor > 4 cm' ,
                     'T3b' : 'tumor that has grown outside the thyroid' ,
                     'T4a' : 'tumor that has invaded nearby structures' ,
                     'T4b' : 'tumor that has invaded nearby structures'} , inplace =True)

df['Metastasis'].unique()

df['Metastasis'].replace({'M0': 'no evidence of distant metastasis' ,
                          'M1' : 'presence of distant metastasis'} ,
                         inplace =True )

df

"""## ***EDA : Exploratory Data Analysis***"""

plt.figure(figsize = (8, 6))
sns.histplot(df['Age'], bins = 25, kde = True, color = 'pink')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

cat_variables = (['Gender', 'Smoking', 'History of Smoking', 'History of Radiotherapy',
       'Thyroid Function', 'Physical Examination', 'Adenopathy',
       'Type of cancer', 'Number of tumors', 'Risk', 'Tumor', 'Lymph Nodes',
       'Metastasis', 'Stage', 'Response', 'Recurred'])

plt.figure(figsize=(25, 30))

for index, var in enumerate(cat_variables):
    plt.subplot(4, 4, index + 1)
    sns.countplot(x=var, data=df, palette='Set2')
    plt.title(f'Count of {var}')
    plt.xlabel('')
    plt.xticks(rotation=80)  # Rotate x-axis labels for better readability
    plt.tight_layout()

# Show the plot
plt.show()

# Lets find if there is any relation between smoking and age with respect to the stage
# Scatter plot for Age vs Cancer Stage colored by Smoking status
plt.figure(figsize=(12, 10))
sns.scatterplot(data=df, x='Stage', y='Age', hue='Smoking')
plt.title('Age vs Cancer Stage by Smoking')
plt.xlabel('Stage')
plt.ylabel('Age')
plt.show()
print(df.groupby(['Stage', 'Smoking']).size().unstack(fill_value=0))

"""The analysis indicates a higher incidence of cancer at initial stages with a relatively low proportion (7.5%) of smokers in Stage I, which dramatically increases to 34.375% in Stage II. This suggests a potential link between smoking and the progression of cancer. In the advanced Stage IVA, where the sample size is small, all patients were smokers, supporting the hypothesis that smoking is associated with more severe stages of cancer.*** These findings highlight smoking as a significant risk factor for both the development and progression of cancer, emphasizing the need for robust anti-smoking campaigns and targeted public health interventions. Enhanced screening and smoking cessation programs, particularly for individuals diagnosed in earlier stages, could significantly impact cancer severity and patient outcomes.***





---


"""

fig, axes = plt.subplots(1, 2, figsize=(20, 5))

sns.boxplot(x='Tumor', y='Age', data=df, ax=axes[0])
axes[0].set_title('Boxplot of Age by Tumor ')
axes[0].set_xlabel('Tumor Stage')
axes[0].set_ylabel('Age')
axes[0].tick_params(axis='x', rotation=90)

# Boxplot for Stage
sns.boxplot(x='Stage', y='Age', data=df, ax=axes[1])
axes[1].set_title('Boxplot of Age by Cancer Stage ')
axes[1].set_xlabel('Cancer Stage')
axes[1].set_ylabel('Age')
axes[1].tick_params(axis='x', rotation=90)

plt.show()

plt.figure(figsize=(10,7))
sns.boxplot(x='Recurred', y='Age', hue = 'History of Smoking', data=df, palette = 'Set2')
plt.title('Age Distribution by Recurrence Status wih respect to History of Smoking')
plt.xlabel('Recurred')
plt.ylabel('Age')
plt.legend(title='Smoking History', loc='upper right')
plt.show()

"""#Interpretations and insights:#
<br> **Age and Tumor/Cancer Severity:** Older age seems to correlate with more advanced tumor characteristics and cancer stages, which may reflect cumulative exposure to risk factors over time.

<br>**Smoking Influence:** Smoking appears to influence the age at which cancer recurs, with smokers showing recurrence at younger ages. This could highlight the role of smoking in the aggressiveness of the cancer or its treatment resistance.

<br>**Clinical Implications:** These findings underscore the importance of targeted surveillance and treatment strategies based on age and smoking history, particularly focusing on early detection and intervention strategies for smokers.

***These interpretations suggest potential areas for further research, particularly in exploring how smoking accelerates cancer progression and impacts treatment across different age groups. These insights can be used in  patient education, screening, and treatment approaches more effectively.***
"""

# Comparing Age across different responses
fig, axes = plt.subplots(1, 2, figsize=(20, 5))

sns.boxplot(x='Response', y='Age', hue = 'Smoking', data=df, ax=axes[0])
axes[0].set_title('Age Distribution Across Treatment Responses (Current smoker)')
axes[0].set_xlabel('Response Category')
axes[0].set_ylabel('Age')
axes[0].tick_params(axis='x', rotation=80)


sns.boxplot(x='Response', y='Age', hue ='History of Smoking', data=df, ax=axes[1])
axes[1].set_title('Age Distribution Across Treatment Responses (History of Smoking)')
axes[1].set_xlabel('Response Category')
axes[1].set_ylabel('Age')
axes[1].tick_params(axis='x', rotation=80)

plt.show()

"""**Monitoring and Intervention:** Older smokers or those with a smoking history might require more aggressive monitoring and potentially different therapeutic strategies due to their different response patterns and age distribution.

**Preventive Measures:** The data underscores the importance of smoking cessation programs, especially targeting younger populations to prevent long-term impacts on health, which may influence treatment outcomes later.

**Research and Policy:** Further research could investigate the biological or social mechanisms by which smoking history impacts treatment responses, potentially influencing public health policies and clinical guidelines.

***The analysis reveals significant insights into how smoking status correlates
with age and treatment response in thyroid cancer patients. These findings can guide more personalized treatment approaches and emphasize the need for targeted smoking cessation support as part of comprehensive cancer care.***
"""

df

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
encoding_methods = {
    'Gender' : 'label',
    'Smoking' : 'label',
    'History of Smoking' : 'label',
    'History of Radiotherapy' : 'label',
    'Thyroid Function' : 'onehot',
    'Physical Examination' : 'onehot',
    'Adenopathy' : 'onehot',
    'Type of cancer': 'onehot',
    'Number of tumors': 'label',
    'Risk' : 'label',
    'Tumor':'label',
    'Lymph Nodes':'label',
    'Metastasis':'label',
    'Stage':'label',
    'Response':'label',
    'Recurred':'label'
}

for column, method in encoding_methods.items():
    if column in df.columns:
        if method == 'label':
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
        elif method == 'onehot':
            one_hot = OneHotEncoder(sparse=False, drop='first') #sparse = false since we do not need sparse matrix, drop = first to avoid multicollinearity
            encoded = one_hot.fit_transform(df[[column]]) #[[column]] to ensure we select a single column and not a series
            column_names = [f'{column}_{category}' for category in one_hot.categories_[0][1:]]
            df_encoded = pd.DataFrame(encoded, columns=column_names, index=df.index)
            df = pd.concat([df, df_encoded], axis=1)
            df.drop(columns=[column], inplace=True)
    else:
        print(f"Column '{column}' not found in DataFrame")


df.head(15)

corr_matrix = df.corr()
plt.figure(figsize = (20,15))
sns.heatmap(corr_matrix, annot = True, cmap = "RdBu")
plt.title("Correlation Matrix of encoded Variables")
plt.show()

#Preprocessing the data based on correlation matrix to avoid overfitting, underfitting and to improve the performane of machine learning models

df = df.drop(columns = ['Type of cancer_Micropapillary', 'Type of cancer_Papillary',         #are highly negatively correlated
                "Adenopathy_Right Side Body Adenopathy", 'Type of cancer_Hurthel cell'])   #dropping one-hot encoded features since they are mutually exclusive and one is highly prevalent'



from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier

X = df.drop(columns=['Recurred'])
y = df['Recurred']

#split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

ml_models = {
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Logistic Regression': LogisticRegression(),
    'Support Vector Machine': SVC(),
    'XGBoost': XGBClassifier()
}

for name, model in ml_models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(f'{name} Classification Report:\n{report}\n')

for model_name, model in ml_models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    print(f"{model_name} Accuracy: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")

"""##*Conclusion*##

This project demonstrated the potential of machine learning models in predicting thyroid cancer recurrence, providing valuable insights into factors influencing recurrence and aiding in early intervention strategies. Through comprehensive data analysis and model evaluation, we identified the strengths and limitations of different classifiers.

Key takeaways include:

Random Forest and XGBoost models outperformed others in accuracy and overall performance, showing great promise for practical applications in predicting thyroid cancer recurrence.
Decision Tree and Logistic Regression also provided robust results, with Decision Tree offering high precision and recall, and Logistic Regression achieving a balanced performance despite convergence warnings.
K-Nearest Neighbors and Support Vector Machine displayed moderate effectiveness, with KNN performing well in certain metrics but struggling with recall for the positive class, and SVM showing limitations in recall and f1-score for the recurrence class.
Model Performance Summary:
Random Forest: Highest accuracy at 99%, excellent precision and recall.
XGBoost: High accuracy at 96%, strong performance across metrics.
Decision Tree: Accuracy of 92%, balanced performance, notable precision and recall.
Logistic Regression: Accuracy of 94%, solid performance but noted for convergence issues.
K-Nearest Neighbors: Accuracy of 90%, with good precision but lower recall for the recurrence class.
Support Vector Machine: Accuracy of 83%, lower recall and f1-score for the positive class.
These results indicate that advanced ensemble methods like Random Forest and XGBoost are particularly effective in this context, providing reliable predictions that can be valuable in clinical decision-making. The visualizations also offered important insights into how age, smoking history, and treatment responses affect recurrence patterns.

Moving forward, further improvements could involve:

Incorporating additional features such as genetic data and comprehensive treatment histories.
Applying deep learning techniques to potentially enhance predictive accuracy.
Validating models on larger and more diverse datasets to ensure generalizability.
This project underscores the importance of predictive analytics in healthcare, showcasing how data-driven approaches can contribute to better patient outcomes and more informed medical practices.
"""