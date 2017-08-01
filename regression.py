import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import csv
from sklearn.model_selection import train_test_split

file = "combined_data_jul25.csv"
data = pd.read_csv(file, index_col=0)


def split_data(data, test_data_size):
    train, test = train_test_split(data, test_size=test_data_size)
    return train, test


def scatter_plot(indep, dep, dataset):

    filename = str(dep + "~" + indep)
    var1 = "data."+indep+".min()"
    exec1 = eval(var1)
    var2 = "data."+indep+".max()"
    exec2 = eval(var2)
    X_new = pd.DataFrame({indep: [exec1, exec2]})
    lm = smf.ols(formula=dep + " ~ " + indep, data=data).fit()

    print(filename)
    print("rsquared: " + str(lm.rsquared))
    print(dir(lm))
    print(lm.pvalues)
    preds = lm.predict(X_new)

    data.plot(kind='scatter', x=indep, y=dep)
    plt.plot(X_new, preds, c='red', linewidth=2)
    plt.savefig("figures/" + str(filename) + ".png")


def get_coefficients(data_str, dataset):
    lm = smf.ols(formula=data_str, data=dataset).fit()
    return lm.params


def print_regression_results(data_str, dataset):
    lm = smf.ols(formula=data_str, data=dataset).fit()
    print(lm.summary())


def predict(coeffs, dataset):

    coef_len = len(coeffs)
    prediction_count = 0
    vs_35_count = 0
    vs_NCAA_3_count = 0

    file = open("volume_data.csv", 'a')

    for index, row in dataset.iterrows():
        college_3_percent = row['threeP_percent']
        college_ft_percent = row['FT_percent']
        threePAG = row['threePAG']
        NBA_3 = row['NBA_3P_percent']


        predicted_NBA_3 = float(coeffs[0]) + (float(coeffs[1]) * float(college_3_percent)) + (float(coeffs[2]) * float(college_ft_percent))

        print(str(NBA_3) + "," + str(predicted_NBA_3) + "," + str(threePAG))
        file.write(str(NBA_3 - predicted_NBA_3) + "," + str(threePAG) + "," + str(row['3PA']) + "," + str(row['3PG']) + "," + str(row['G']) + "," + str(row['PTS']) + '\n')

        if predicted_NBA_3 <= NBA_3 + 0.02 and predicted_NBA_3 >= NBA_3 - 0.02:
            prediction_count += 1

        if NBA_3 >= 0.33 and NBA_3 <= 0.37:
            vs_35_count += 1

        if NBA_3 <= college_3_percent + 0.02 and NBA_3 >= college_3_percent - 0.02:
            vs_NCAA_3_count += 1

    print("Number of regression predictions that are within 2% of actual NBA 3FG%: " + str(prediction_count))
    print("Number of times a player's NBA 3FG% is between 33% - 37%: " + str(vs_35_count))
    print("Number of times a player's NBA 3FG% is within 2% of his NCAA 3FG%: " + str(vs_NCAA_3_count))

    file.close()
    return prediction_count, vs_35_count, vs_NCAA_3_count








