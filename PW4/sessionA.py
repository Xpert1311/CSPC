import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.inspection import permutation_importance

os.makedirs("results", exist_ok=True)

#A2
df = pd.read_csv("data/concrete.csv")
duplicates = df.duplicated().sum()
missing = df.isna().sum().sum()
df = df.drop_duplicates().reset_index(drop=True)
X = df.drop(columns=["strength"])
y = df["strength"]

#A3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#A4
lr = LinearRegression()
lr.fit(X_train, y_train)

def adj_r2(r2, n, p):
    return 1 - (1 - r2) * ((n - 1) / (n - p - 1))

y_pred_train = lr.predict(X_train)
y_pred_test = lr.predict(X_test)
r2_train = r2_score(y_train, y_pred_train)

print("\n   Linear Regression")
print(f"R2 Train: {r2_train:.3f}, Adj R2 Train: {adj_r2(r2_train, len(X_train), X.shape[1]):.3f}")
print(f"R2 Test: {r2_score(y_test, y_pred_test):.3f}")
print(f"RMSE Test: {np.sqrt(mean_squared_error(y_test, y_pred_test)):.3f}")

#A5
print("\n   Polynomial Regression")
for d in [1, 2, 3, 4]:
    poly = make_pipeline(PolynomialFeatures(degree=d, include_bias=False),
                         StandardScaler(), LinearRegression())
    poly.fit(X_train, y_train)
    p = poly[0].n_output_features_
    r2_tr = r2_score(y_train, poly.predict(X_train))
    print(f"Degree {d} | Features: {p} | R2 Train: {r2_tr:.3f} | Adj R2 Train: {adj_r2(r2_tr, len(X_train), p):.3f} | R2 Test: {r2_score(y_test, poly.predict(X_test)):.3f}")

#A6
print("\n   Classification")
y_class = (df["strength"] >= 40).astype(int)
Xc_train, Xc_test, c_train, c_test = train_test_split(X, y_class, test_size=0.2, random_state=42, stratify=y_class)

best_knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
best_knn.fit(Xc_train, c_train)

best_tree = DecisionTreeClassifier(criterion="entropy", max_depth=5, random_state=0)
best_tree.fit(Xc_train, c_train)
print("Tree Depth:", best_tree.get_depth(), "| Leaves:", best_tree.get_n_leaves())

#A7
def get_metrics(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    return [tp, fp, fn, tn, accuracy_score(y_true, y_pred), precision_score(y_true, y_pred), recall_score(y_true, y_pred), f1_score(y_true, y_pred)]

knn_pred = best_knn.predict(Xc_test)
tree_pred = best_tree.predict(Xc_test)

metrics_df = pd.DataFrame([get_metrics(c_test, knn_pred), get_metrics(c_test, tree_pred)],
                          columns=["TP", "FP", "FN", "TN", "Accuracy", "Precision", "Recall", "F1"],
                          index=["KNN (K=5)", "Tree (Depth=5)"])
metrics_df.to_csv("results/A_metrics.csv", index=True)
print("Saved A_metrics.csv")

#A8
print("\n   Feature Importance")
scaled_lr = make_pipeline(StandardScaler(), LinearRegression())
scaled_lr.fit(X_train, y_train)
print("Standardised Coefficients:", scaled_lr[-1].coef_)
print("Tree Importances:", best_tree.feature_importances_)
pi = permutation_importance(best_knn, Xc_test, c_test, scoring="f1", n_repeats=20, random_state=0)
print("KNN Permutation Importances:", pi.importances_mean)