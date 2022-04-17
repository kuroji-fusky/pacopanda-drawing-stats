import pandas as pandapaco

df = pandapaco.read_csv('csv/paco-2021-updated.csv')

species = df.drop(columns=['Date', 'Name', 'Character(s)', 'Expression(s)', 'Type', 'Source'])
species.to_numpy()

pp = 'merged/species_merged.csv'

with open(pp, 'r+') as f:
  bruh = species.to_string(index=False)
  f.write(bruh)
  kiddieland = f.read().replace(' ', '')
  f.write(kiddieland)
  kiddieland = f.read().replace('\n', ',')
  f.write(kiddieland)
  kiddieland = f.read().replace(',', '\n')
  f.write(kiddieland)