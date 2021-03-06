import pandas as pd

import re
from sklearn.model_selection import train_test_split
import csv
from copy import deepcopy
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np

from Classifiers.FeatureImportanceV3 import feature_importance_rf_new, feature_importance_rf_old, \
    feature_importance_dt_new


def read_dataset_with_feature():
    print("Feature engineered dataset\n")
    symbols = ['Bot', 'bot', 'b0t', 'B0T', 'B0t', 'random', 'http', 'co', 'every', 'twitter', 'pubmed', 'news',
               'created', 'like', 'feed', 'tweeting', 'task', 'world', 'x', 'affiliated', 'latest', 'twitterbot',
               'project', 'botally', 'generated', 'image', 'reply', 'tinysubversions', 'biorxiv', 'digital', 'rt',
               'ckolderup', 'arxiv', 'rss', 'thricedotted', 'collection', 'want', 'backspace', 'maintained',
               'things', 'curated', 'see', 'us', 'people', 'every', 'love', 'please']

    file_path = 'final_merged.csv'

    bot_array = []
    user_array = []

    with \
            open(file_path,
                 'r+',
                 encoding="utf-8") as inp:
        reader = csv.DictReader(inp)

        for row in reader:
            array_feature = [float(any(x in row['screen_name'] for x in symbols)),
                             float(any(x in row['description'] for x in symbols))]

            if row['bot'] == '1':
                arraybot = [0 if float(row['age']) < 0 else float(row['age']),
                            0 if float(row['in_out_ratio']) < 0 else float(row['in_out_ratio']),
                            0 if float(row['favorites_ratio']) < 0 else float(row['favorites_ratio']),
                            0 if float(row['status_ratio']) < 0 else float(row['status_ratio']),
                            0 if float(row['account_rep']) < 0 else float(row['account_rep']),
                            0 if float(row['avg_tpd']) < 0 else float(row['avg_tpd']),
                            0 if float(row['hashtags_ratio']) < 0 else float(row['hashtags_ratio']),
                            0 if float(row['user_mentions_ratio']) < 0 else float(row['user_mentions_ratio']),
                            0 if float(row['url_ratio']) < 0 else float(row['url_ratio']),
                            0 if float(row['cce']) < 0 else float(row['cce']),
                            0 if float(row['spam_ratio']) < 0 else float(row['spam_ratio']),
                            array_feature[0],
                            array_feature[1]]

                bot_array.append(deepcopy(arraybot))

            else:
                array = [0 if float(row['age']) < 0 else float(row['age']),
                         0 if float(row['in_out_ratio']) < 0 else float(row['in_out_ratio']),
                         0 if float(row['favorites_ratio']) < 0 else float(row['favorites_ratio']),
                         0 if float(row['status_ratio']) < 0 else float(row['status_ratio']),
                         0 if float(row['account_rep']) < 0 else float(row['account_rep']),
                         0 if float(row['avg_tpd']) < 0 else float(row['avg_tpd']),
                         0 if float(row['hashtags_ratio']) < 0 else float(row['hashtags_ratio']),
                         0 if float(row['user_mentions_ratio']) < 0 else float(row['user_mentions_ratio']),
                         0 if float(row['url_ratio']) < 0 else float(row['url_ratio']),
                         0 if float(row['cce']) < 0 else float(row['cce']),
                         0 if float(row['spam_ratio']) < 0 else float(row['spam_ratio']),
                         array_feature[0],
                         array_feature[1]]

                user_array.append(deepcopy(array))

    print(len(bot_array))
    print(len(user_array))

    features = user_array + bot_array[:len(user_array)]
    labels = ([0] * len(user_array)) + ([1] * len(user_array))

    return features, labels


def read_dataset():
    print("Normal dataset\n")
    file_path = 'final_merged.csv'
    bot_array = []
    user_array = []

    with \
            open(file_path,
                 'r+',
                 encoding="utf-8") as inp:
        reader = csv.DictReader(inp)

        for row in reader:
            if row['bot'] == '1':
                array = [0 if float(row['age']) < 0 else float(row['age']),
                         0 if float(row['in_out_ratio']) < 0 else float(row['in_out_ratio']),
                         0 if float(row['favorites_ratio']) < 0 else float(row['favorites_ratio']),
                         0 if float(row['status_ratio']) < 0 else float(row['status_ratio']),
                         0 if float(row['account_rep']) < 0 else float(row['account_rep']),
                         0 if float(row['avg_tpd']) < 0 else float(row['avg_tpd']),
                         0 if float(row['hashtags_ratio']) < 0 else float(row['hashtags_ratio']),
                         0 if float(row['user_mentions_ratio']) < 0 else float(row['user_mentions_ratio']),
                         0 if float(row['url_ratio']) < 0 else float(row['url_ratio']),
                         0 if float(row['cce']) < 0 else float(row['cce']),
                         0 if float(row['spam_ratio']) < 0 else float(row['spam_ratio'])]
                bot_array.append(deepcopy(array))

            else:
                array = [0 if float(row['age']) < 0 else float(row['age']),
                         0 if float(row['in_out_ratio']) < 0 else float(row['in_out_ratio']),
                         0 if float(row['favorites_ratio']) < 0 else float(row['favorites_ratio']),
                         0 if float(row['status_ratio']) < 0 else float(row['status_ratio']),
                         0 if float(row['account_rep']) < 0 else float(row['account_rep']),
                         0 if float(row['avg_tpd']) < 0 else float(row['avg_tpd']),
                         0 if float(row['hashtags_ratio']) < 0 else float(row['hashtags_ratio']),
                         0 if float(row['user_mentions_ratio']) < 0 else float(row['user_mentions_ratio']),
                         0 if float(row['url_ratio']) < 0 else float(row['url_ratio']),
                         0 if float(row['cce']) < 0 else float(row['cce']),
                         0 if float(row['spam_ratio']) < 0 else float(row['spam_ratio'])]
                user_array.append(deepcopy(array))

    features = user_array + bot_array[:len(user_array)]
    labels = ([0] * len(user_array)) + ([1] * len(user_array))

    return features, labels


def main():
    features, labels = read_dataset()
    #features, labels = read_dataset_with_feature()
    features_train, features_test, labels_train, labels_test = train_test_split(
        features,
        labels,
        test_size=0.1,  # use 10% for testing
        random_state=0)

    scaler = MinMaxScaler()
    scaler.fit(features_train)
    transformed_features = scaler.transform(features_train)
    test_transformed = scaler.transform(features_test)

    clf_mnb = MultinomialNB(alpha=0.0009)
    clf_rf = RandomForestClassifier(random_state=0)
    clf_dt = DecisionTreeClassifier(random_state=0)

    clf_mnb.fit(transformed_features, labels_train)
    clf_rf.fit(transformed_features, labels_train)
    clf_dt.fit(transformed_features, labels_train)

    # Finding out feature importance for each classifier
    # feature_importance_rf_new(features_train, clf_rf)
    # feature_importance_dt_new(features_train, clf_dt)

    predicted_mnb = clf_mnb.predict(test_transformed)
    predicted_rf = clf_rf.predict(test_transformed)
    predicted_dt = clf_dt.predict(test_transformed)

    accuracy_mnb = metrics.accuracy_score(labels_test, predicted_mnb)
    accuracy_rf = metrics.accuracy_score(labels_test, predicted_rf)
    accuracy_dt = metrics.accuracy_score(labels_test, predicted_dt)

    print('Accuracy Naive Bayes' + str(accuracy_mnb))
    print('Accuracy Random Forest' + str(accuracy_rf))
    print('Accuracy Decision Tree' + str(accuracy_dt))

    fpr_rf, tpr_rf, threshold_rf = roc_curve(labels_test, predicted_rf)
    roc_auc_rf = auc(fpr_rf, tpr_rf)
    fpr_dt, tpr_dt, threshold_dt = roc_curve(labels_test, predicted_dt)
    roc_auc_dt = auc(fpr_dt, tpr_dt)
    fpr_nb, tpr_nb, threshold_nb = roc_curve(labels_test, predicted_mnb)
    roc_auc_nb = auc(fpr_nb, tpr_nb)
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr_rf, tpr_rf, 'b', label='Random Forest AUC = %0.2f' % roc_auc_rf)
    plt.plot(fpr_dt, tpr_dt, 'y', label='Decision Tree AUC = %0.2f' % roc_auc_dt)
    plt.plot(fpr_nb, tpr_nb, 'g', label='Naive Bayes AUC = %0.2f' % roc_auc_nb)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()


if __name__ == '__main__':
    main()
