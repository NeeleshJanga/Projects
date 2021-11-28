Problem Description:
# Bob has started his own mobile company.
# He wants to give a tough fight to big companies like Apple, Samsung, etc.
# He does not know how to estimate the price of mobiles his company creates.
# In this competitive mobile phone market you cannot simply assume things.
# To solve this problem he collects sales data of mobile phones of various companies.

# Bob wants to find out some relation between features of a mobile phone(eg:- RAM, Internal Memory, etc) and its selling price.
# But he is not so good at Machine Learning. So he needs your help to solve this problem.

"In this problem, you do not have to predict the actual price but a price range indicating how high the price is."

My Solution:
# As there is no target test data provided, I opted to go with K-Fold cross-validation first for most of the popular classification algorithms 
  which include SVM, KNN, Random Forest, & Logistic Regression, and the accuracies are 82.05%, 80.4%, 80.35% & 73.55% respectively.
# Considering these metrics I opted for going with SVM among them.
