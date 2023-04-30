# -*- codeing =utf-8 -*-
# @Time : 2022/3/10 2:48 下午
# @Author : 朱赫
# @File : cv01.py
# @Software:PyCharm




from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
import pandas as pd
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
print(knn.score(X_test,y_test))



from sklearn.model_selection import cross_val_score


#使用K折交叉验证模块
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')

#将5次的预测准确率打印出
print(scores)
# [ 0.96666667  1.          0.93333333  0.96666667  1.        ]
#将5次的预测准确平均率打印出
print(scores.mean())

import matplotlib.pyplot as plt


k_range= range(1,31)























