# Fit a logistic regression model
from sklearn import linear_model


#----------------------
# get to know your data
#----------------------

# Assign the number of rows in the basetable to the variable 'population_size'.
population_size  = len(basetable)
# Print the population size.
print(population_size)

# Assign the number of targets to the variable 'targets_count'.
targets_count = sum(basetable["target"])
# Print the number of targets.
print(targets_count)

# Print the target incidence.
print(targets_count / population_size)

# Count and print the number of females.
print(sum(basetable["gender"] == "F"))
# Count and print the number of males.
print(sum(basetable["gender"] == "M"))

#------------------
# train your model
#------------------
predictors = ["age","gender_F","time_since_last_gift"]
X = basetable[predictors]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Assign the coefficients to a list coef
coef = logreg.coef_
for p,c in zip(predictors,list(coef[0])):
    print(p + '\t' + str(c))
    
# Assign the intercept to the variable intercept
intercept = logreg.intercept_
print(intercept)

#-------------------------
# prediction with new data
#-------------------------
# Create a dataframe new_data from current_data that has only the relevant predictors 
new_data = current_data[["age", "gender_F",  "time_since_last_gift"]]

# Make a prediction for each observation in new_data and assign it to predictions
predictions = logreg.predict_proba(new_data)
print(predictions[0:5])

# Sort the predictions
predictions_sorted = predictions.sort(["probability"])

# Print the row of predictions_sorted that has the donor that is most likely to donate
print(predictions_sorted.tail(1))