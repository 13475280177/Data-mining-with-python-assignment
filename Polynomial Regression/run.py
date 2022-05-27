import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
# __________________________________________________________________________
grade = pd.read_csv('./specs/markB_question.csv')

reg = LinearRegression()

mcq1 = grade['MCQ1'].to_numpy().reshape(-1, 1)
y_train = grade['final'].to_numpy().reshape(-1, 1)
reg.fit(mcq1, y_train)
predicted_final = reg.predict(mcq1)
grade['final_linear'] = predicted_final

print("coefficient is " + str(reg.coef_.round(2)) + "  intercept is " + str(
    reg.intercept_.round(2)))
# RMSE and R2
mse = metrics.mean_squared_error(grade['final'], grade['final_linear'])
rmse = math.sqrt(mse)
r2 = metrics.r2_score(grade['final'], grade['final_linear'])
print("rmse is" + str(rmse) + "  R2 is" + str(r2))
# __________________________________________________________________________

feature_2 = pd.DataFrame(mcq1)
feature_2["dim2"] = feature_2.iloc[:, 0] ** 2

reg = LinearRegression()
reg.fit(feature_2, y_train)
predicted_final = reg.predict(feature_2)
grade['final_quadratic'] = predicted_final
print("coefficient is " + str(reg.coef_.round(2)) + "  intercept is " + str(
    reg.intercept_.round(2)))
# RMSE and R2
mse = metrics.mean_squared_error(grade['final'], grade['final_quadratic'])
rmse = math.sqrt(mse)
r2 = metrics.r2_score(grade['final'], grade['final_quadratic'])
print("rmse is " + str(rmse) + "  R2 is " + str(r2) + '\n')


# __________________________________________________________________________________
degrees = [ 2, 3, 4, 8, 10]
plt.figure(figsize=(20,5))
for i in range(len(degrees)):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())

    polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    pipeline.fit(mcq1, y_train)

    grade['final_poly'+str(degrees[i])] = pipeline.predict(mcq1)

    X_test = np.linspace(0, 100, 100).reshape(-1,1)
    plt.plot(X_test, pipeline.predict(X_test), label="Model")
    plt.scatter(mcq1, y_train)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Degree {}\nRMSE = {:.2e}\nR2 = {:.2e}".format(
            degrees[i], math.sqrt(metrics.mean_squared_error(grade['final'], grade['final_poly'+str(degrees[i])])), metrics.r2_score(grade['final'], grade['final_poly'+str(degrees[i])]))
        )
grade.to_csv('./output/question_mcq1.csv')
plt.show()

# ______________________________________________________________________________
grade = pd.read_csv('./specs/markB_question.csv')
reg = LinearRegression()
mcq = grade.iloc[:,[0,1]]
reg.fit(mcq, y_train)
predicted_final = reg.predict(mcq)
grade['final_linear'] = predicted_final
print("coefficient is" + str(reg.coef_.round(2)) + "  intercept is" + str(
    reg.intercept_.round(2)))
mse = metrics.mean_squared_error(grade['final'], grade['final_linear'])
rmse = math.sqrt(mse)
r2 = metrics.r2_score(grade['final'], grade['final_linear'])
print("rmse is " + str(rmse) + "  R2 is " + str(r2)+'\n')

# ______________________________________________________________________________
train = PolynomialFeatures(degree=2, include_bias=False).fit_transform(mcq)
polynomial_model_full = LinearRegression()
polynomial_model_full.fit(train,y_train)
predicted_final = polynomial_model_full.predict(train)
grade['final_quadratic'] = predicted_final
grade.to_csv('./output/question_full.csv ')
print("coefficient is " + str(polynomial_model_full.coef_.round(2)) + "  intercept is " + str(
    polynomial_model_full.intercept_.round(2)))
mse = metrics.mean_squared_error(grade['final'], grade['final_quadratic'])
rmse = math.sqrt(mse)
r2 = metrics.r2_score(grade['final'], grade['final_quadratic'])
print("rmse is " + str(rmse) + "  R2 is " + str(r2)+'\n')

