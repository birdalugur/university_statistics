import os
import statsmodels.api as sm

if not os.path.exists('statistics'):
    os.mkdir("statistics")


def write_OLS(Y, X, file_name: str):
    X = sm.add_constant(X)

    model = sm.OLS(Y, X)
    results = model.fit()

    with open("statistics/" + file_name + ".html", 'w', encoding='utf-8') as f:
        f.write(results.summary().as_html())
        f.write('\n\n\n')
        f.write("<p>R2: " + str(results.rsquared) + '</p>')
