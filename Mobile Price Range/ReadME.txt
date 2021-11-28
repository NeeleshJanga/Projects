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
# I constructed a Random Forest Classifier to classify multiple classes and the accuracy of my model with default parameters is 79.00%.
# When applied K-Fold Cross-validation with split value = 10, the highest score generated is 83%, lowest is 76% and the average score is 79.75%.
