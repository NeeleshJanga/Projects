Problem:
# The sinking of the Titanic is one of the most infamous shipwrecks in history.
# While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.
# In this challenge, we are asked to build a predictive model that answers the question: “what sorts of people were more likely to survive?” 
  using passenger data (ie name, age, gender, socio-economic class, etc).

Solution:
# Firstly for this classification the target test data is not given so what I did is first k-fold cross-validated with 10 fold to the algorithms KNN, SVM, 
  Logistic Regression & Random Forest and selected the best one among them.
# Mean of Accuracy readings of KNN, SVM, Logistic regression & Random forest are 62.18%, 65.1%, 79.69% & 81.6% respectively.
# Random Forest worked best in this case so I used it for my predictions.
