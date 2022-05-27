import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier,plot_tree
# 1
df = pd.read_csv('./specs/marks_question1.csv')
plt.figure()
plt.xlabel('Mid-term')
plt.ylabel('Final')
plt.plot(df['midterm'],df['final'],'s')
plt.savefig('./output/marks.png')
plt.show()

reg = linear_model.LinearRegression()
# fit
reg.fit(df.iloc[:,[0]], df.iloc[:,[1]])
# y= ax + b;
print("y= "+str(round(reg.coef_[0][0],3))+"x + "+str(round(reg.intercept_[0],3)))

# test
print(round(reg.predict([[86]])[0][0],3))


# 2
df = pd.read_csv('./specs/borrower_question2.csv')
del df['TID']
# fit
label = df.pop('DefaultedBorrower')
train = pd.get_dummies(df)
tree_high = DecisionTreeClassifier(criterion='entropy',min_impurity_decrease=0.5).fit(train,label)
plt.figure()
plot_tree(tree_high)
plt.savefig('./output/tree_high.png')
plt.show()
# fit
tree_low =DecisionTreeClassifier(criterion='entropy',min_impurity_decrease=0.1).fit(train,label)
plt.figure()
plot_tree(tree_low)
plt.savefig('./output/tree_low.png')
plt.show()


