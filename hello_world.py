from sklearn import tree
features = [[140, 1], [130, 1], [170, 0], [150, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160, 0]]))