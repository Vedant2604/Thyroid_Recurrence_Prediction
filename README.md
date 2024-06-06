
# Thyroid Recurrence Prediction
## Overview
This project focuses on predicting thyroid cancer recurrence using various machine-learning algorithms. The goal is to enhance our understanding of the factors influencing recurrence and to develop predictive models that can aid in early detection and treatment planning.

## Libraries 


```bash
pip install seaborn
pip install matplotlib
pip install numpy
pip install scikit-learn
pip install pandas
```

## Insights and Interpretations
### 1. Age vs Cancer Stage by Smoking Status
The analysis indicates a higher incidence of cancer at the initial stages with a relatively low proportion (7.5%) of smokers in Stage I, which dramatically increases to 34.375% in Stage II. This suggests a potential link between smoking and the progression of cancer. In the advanced Stage IVA, where the sample size is small, all patients were smokers, supporting the hypothesis that smoking is associated with more severe stages of cancer.* These findings highlight smoking as a significant risk factor for both the development and progression of cancer, emphasizing the need for robust anti-smoking campaigns and targeted public health interventions. Enhanced screening and smoking cessation programs, particularly for individuals diagnosed in earlier stages, could significantly impact cancer severity and patient outcomes.*

### 2. Age Distribution by Recurrence Status Concerning History of Smoking
Age and Tumor/Cancer Severity: Older age seems to correlate with more advanced tumor characteristics and cancer stages, which may reflect cumulative exposure to risk factors over time.


Smoking Influence: Smoking appears to influence the age at which cancer recurs, with smokers showing recurrence at younger ages. This could highlight the role of smoking in the aggressiveness of the cancer or its treatment resistance.


Clinical Implications: These findings underscore the importance of targeted surveillance and treatment strategies based on age and smoking history, particularly focusing on early detection and intervention strategies for smokers.

These interpretations suggest potential areas for further research, particularly in exploring how smoking accelerates cancer progression and impacts treatment across different age groups. These insights can be used in patient education, screening, and treatment approaches more effectively.

### 3. Age Distribution by Treatment Response Concerning History of Smoking and Smoking Status
Monitoring and Intervention: Older smokers or those with a smoking history might require more aggressive monitoring and potentially different therapeutic strategies due to their different response patterns and age distribution.

Preventive Measures: The data underscores the importance of smoking cessation programs, especially targeting younger populations to prevent long-term impacts on health, which may influence treatment outcomes later.

Research and Policy: Further research could investigate the biological or social mechanisms by which smoking history impacts treatment responses, potentially influencing public health policies and clinical guidelines.

The analysis reveals significant insights into how smoking status correlates with age and treatment response in thyroid cancer patients. These findings can guide more personalized treatment approaches and emphasize the need for targeted smoking cessation support as part of comprehensive cancer care.

## Classifiers



``` bash
Random Forest Classification Report:
              precision    recall  f1-score   support

           0       0.98      1.00      0.99        58
           1       1.00      0.95      0.97        19

    accuracy                           0.99        77
   macro avg       0.99      0.97      0.98        77
weighted avg       0.99      0.99      0.99        77


XGBoost Classification Report:
              precision    recall  f1-score   support

           0       0.98      0.97      0.97        58
           1       0.90      0.95      0.92        19

    accuracy                           0.96        77
   macro avg       0.94      0.96      0.95        77
weighted avg       0.96      0.96      0.96        77
```
### Insights 
Upon using multiple machine learning models such as DecisionTreeClassifier, RandomForestClassifier, KNeighborsClassifier, LogisticRegression, and XGBClassifier, The RandomForest and XGboost performed the best, out of these two RandomForest show signs of overfitting with the recall of 1.0, considering XGBoost performed the best with the recall of 0.97 and 0.95 for both the cases.