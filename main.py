import pandas as pd

data = pd.read_csv('data.csv', delim_whitespace=True,
                   names=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
                          'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                          'PTRATIO', 'B', 'LSTAT', 'MEDV'])

threshold_high = 0.7
threshold_low = 0.1

corr_matrix = data.corr().round(2)
independent_vars = set(corr_matrix.columns)

print("\nLEGEND:\n"
      "CRIM - per capita crime rate by town\n"
      "ZN - proportion of residential land zoned for lots over 25,000 sq.ft.\n"
      "INDUS - proportion of non-retail business acres per town.\n"
      "CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)\n"
      "NOX - nitric oxides concentration (parts per 10 million)\n"
      "RM - average number of rooms per dwelling\n"
      "AGE - proportion of owner-occupied units built prior to 1940\n"
      "DIS - weighted distances to five Boston employment centres\n"
      "RAD - index of accessibility to radial highways\n"
      "TAX - full-value property-tax rate per $10,000\n"
      "PTRATIO - pupil-teacher ratio by town\n"
      "B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town\n"
      "LSTAT - % lower status of the population\n"
      "MEDV - Median value of owner-occupied homes in $1000's")


print("\nVariables that are likely DEPENDENT: ")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > threshold_high:
            correlation_type = "POSITIVE" if corr_matrix.iloc[i, j] > 0 else "NEGATIVE"
            print(f'{corr_matrix.columns[i]} and {corr_matrix.columns[j]} have a {correlation_type} correlation of {corr_matrix.iloc[i, j]}')
            if corr_matrix.columns[i] in independent_vars:
                independent_vars.remove(corr_matrix.columns[i])
            if corr_matrix.columns[j] in independent_vars:
                independent_vars.remove(corr_matrix.columns[j])
        elif abs(corr_matrix.iloc[i, j]) < threshold_low:
            if corr_matrix.columns[i] not in independent_vars:
                independent_vars.add(corr_matrix.columns[i])
            if corr_matrix.columns[j] not in independent_vars:
                independent_vars.add(corr_matrix.columns[j])

print("\nVariables that are likely INDEPENDENT: ")
for var in independent_vars:
    print(var)
