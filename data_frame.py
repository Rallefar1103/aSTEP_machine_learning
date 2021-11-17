import pandas as pd
import numpy as np
from decision_class import DecisionTree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

def load_segment_data_dataframe(dataset):
    df = None
    file_name = dataset[0]
    file_extension = dataset[1]
    file_notation = dataset[2]
    column_names = [
        "road_source_id",
        "mileage_from",
        "mileage_to",
        "type",
        "max_axle_load",
        "max_width",
        "max_height",
        "max_length",
        "max_weight",
        "one_way",
        "recommended_speed",
        "type_max_speed",
        "set_max_speed",
        "mean_speed",
        "daily_year",
        "daily_july",
        "daily_trucks",
        "daily_10_axle",
    ]

    if file_notation == "DK" and file_extension == ".csv":
        df = pd.read_csv("dataset/"+file_name+".csv", decimal=",", sep=";", names=column_names, index_col=False)
    elif file_notation == "EN" and file_extension == ".csv":
        df = pd.read_csv("dataset/"+file_name+".csv", decimal=".", sep=",", names=column_names, index_col=False)
    elif file_extension == ".xls":
        df = pd.read_excel("/Users/rasmushenriksen/Desktop/BACHELOR-SOFTWARE/femte_og_sjette/femte_semester/Project/Python/src/Data_set/aalborg_segment_data.xls",
         names=column_names, index_col=False, na_values=["Trafikvej, gennemfart land"], 
        )
    else:
        raise Exception("Notation (" + file_notation + ") or Extension (" + file_extension + ") not added to the function")

    return df

# Import data
execute = False
datasets_with_extension_notation_municipality_mun_source_id_and_source = [
    ("aalborg_segment_data", ".xls", "DK", "Aalborg", "851", "vejman.dk"),
]

df = load_segment_data_dataframe(datasets_with_extension_notation_municipality_mun_source_id_and_source[0])
df.fillna(0.0)

print(df.columns)


# Convert data to numpy format
# data = df.to_numpy()
# print(data.shape)


# Preprocess data to correct format
# n_samples, n_features = data.shape
updated = df.drop('road_source_id', axis=1) 
updated = updated.drop('max_axle_load', axis=1)
updated = updated.drop('max_width', axis=1)
updated = updated.drop('max_length', axis=1)
updated = updated.drop('max_height', axis=1)
updated = updated.drop('max_weight', axis=1)
updated = updated.drop('mean_speed', axis=1)
updated = updated.drop('one_way', axis=1)
updated = updated.drop('type_max_speed', axis=1)
updated = updated.drop('type', axis=1)
updated = updated.drop('recommended_speed', axis=1)
updated['set_max_speed'] = updated['set_max_speed'].fillna(0.0)
updated = updated[:50]

print(updated)

X_input = updated.drop(columns=['daily_trucks'])
y_output = updated['daily_trucks']

X_train, X_test, y_train, y_test = train_test_split(X_input, y_output, test_size=0.2)

### SKL-implemented Decision Tree Model

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions = model.predict(X_test)

# for x in predictions:
#     print(x)

score = accuracy_score(y_test, predictions)
print("Daily trucks Accuracy score: ", score)

### Self-implemented Decision Tree Model

# Split data for training
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=1234
# )

# # Train the data
# clf = DecisionTree(max_depth=10)
# clf.fit(X_train, y_train)

# # Make predictions
# y_pred = clf.predict(X_test)
# acc = accuracy(y_test, y_pred)

# print("Decision Tree Accuracy:", acc)