import matplotlib.pyplot as plotDatGoodness
import pandas as pandapaco

# Get 2021 compiled drawing data and filters digital and
# traditional drawings
paco2021 = pandapaco.read_csv("csv/paco-2021-updated.csv")

types_data = [
  paco2021.loc[paco2021['Type'] == 'Traditional'].count()[0],
  paco2021.loc[paco2021['Type'] == 'Digital'].count()[0]
]

labels = ['Traditional', 'Digital']

plotDatGoodness.pie(types_data, labels=labels, autopct='%.2f%%')
plotDatGoodness.title("Types")
plotDatGoodness.show()
