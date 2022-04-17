from sys import displayhook
import matplotlib.pyplot as plotDatGoodness
import pandas as pandapaco

sa = pandapaco.read_csv("merged/species_merged.csv")

# Plots the data
ott = [
  sa.loc[sa['Species'] == 'ArcticFox'].count()[0] + sa.loc[sa['Species'] == 'Fox'].count()[0] + sa.loc[sa['Species'] == 'Foxes'].count()[0],
  sa.loc[sa['Species'] == 'Raccoon'].count()[0],
  sa.loc[sa['Species'] == 'Wolf'].count()[0] + sa.loc[sa['Species'] == 'Wolf?'].count()[0] + sa.loc[sa['Species'] == 'Wolves'].count()[0],
  sa.loc[sa['Species'] == 'Panda'].count()[0] + sa.loc[sa['Species'] == 'Pandas'].count()[0],
  sa.loc[sa['Species'] == 'Dragon'].count()[0] + sa.loc[sa['Species'] == 'Dragons'].count()[0],
  sa.loc[sa['Species'] == 'Otter'].count()[0],
  sa.loc[sa['Species'] == 'Bunny'].count()[0] + sa.loc[sa['Species'] == 'Rabbit'].count()[0],
  sa.loc[sa['Species'] == 'Dog'].count()[0],
  sa.loc[sa['Species'] == 'Bear'].count()[0],
  sa.loc[sa['Species'] == 'RadPanda'].count()[0] + sa.loc[sa['Species'] == 'RedPanda'].count()[0],
]

ott_label = [
  'Foxes',
  'Raccoons',
  'Wolves',
  'Pandas',
  'Dragons',
  'Otters',
  'Rabbits',
  'Dogs',
  'Bears',
  'Red Pandas'
]

plotDatGoodness.pie(ott, labels=ott_label, autopct='%.2f%%')
plotDatGoodness.title("Total of species drawn")
plotDatGoodness.show()

# I can't believe that I've spent more than 2 days trying to figure out how to get the sum of each species and despite
# hoping through Stack Overflow, Dev.to, and other dev blogs, I couldn't get to figure it out and starting to go insane
# with errors throwing at my face, so screw it, I'll just hard-code arrays since I'm tired of it I might be me being
# new coding in Python or I'm just a dumbass who couldn't figure things out but whatever, I can't be bothered anymore

# Sorry but I lowkey had a mental breakdown while doing all this data analysis crap lmfao

# sa = pandapaco.read_csv("data/merged/species_merged.csv")
# total = sa.groupby('Species').count()
# print(total)

# There has to be a better way to implement this god-awful code...
# lmao who needs a for loop for this heidious chunk of code lol

huge_chunk_of_abominaton = [
  ['African Wild Dog', sa.loc[sa['Species'] == 'AfricanWildDog'].count()[0]],
  ['Albino Raccoon', sa.loc[sa['Species'] == 'AlbinoRaccoon'].count()[0]],
  ['Arctic Wolf', sa.loc[sa['Species'] == 'ArcticWolf'].count()[0]],
  ['Armadillo', sa.loc[sa['Species'] == 'Armadillo'].count()[0]],
  ['Bat', sa.loc[sa['Species'] == 'Bat'].count()[0]],
  ['Bear', sa.loc[sa['Species'] == 'Bear'].count()[0]],
  ['Beaver', sa.loc[sa['Species'] == 'Beaver'].count()[0]],
  ['Border Collie', sa.loc[sa['Species'] == 'Collie'].count()[0]],
  ['Bird', sa.loc[sa['Species'] == 'Bird'].count()[0]],
  ['Burb', sa.loc[sa['Species'] == 'Burb'].count()[0]],
  ['Cat', sa.loc[sa['Species'] == 'Cat'].count()[0]],
  ['Cheetah', sa.loc[sa['Species'] == 'Cheetah'].count()[0]],
  ['Crocodile', sa.loc[sa['Species'] == 'Crocodile'].count()[0]],
  ['Deer', sa.loc[sa['Species'] == 'Deer'].count()[0]],
  ['Digimon', sa.loc[sa['Species'] == 'Digimon'].count()[0]],
  ['Dingoroo', sa.loc[sa['Species'] == 'Dingoroo'].count()[0]],
  ['Dog', sa.loc[sa['Species'] == 'Dog'].count()[0]],
  ['Dognut', sa.loc[sa['Species'] == 'Doghnut'].count()[0]],
  ['Quoll', sa.loc[sa['Species'] == 'EasternQuoll'].count()[0]],
  ['Gryphon', sa.loc[sa['Species'] == 'EgyptianGryphon'].count()[0]],
  ['Flying Fox', sa.loc[sa['Species'] == 'FlyingFox'].count()[0]],
  ["Fox-Dragon", sa.loc[sa['Species'] == "Fox-Dragon"].count()[0]],
  ['Folf', sa.loc[sa['Species'] == 'Folf'].count()[0]],
  ['Mutt', sa.loc[sa['Species'] == 'Mutt'].count()[0] + sa.loc[sa['Species'] == 'MuttPup'].count()[0]],
  ["Dragons", sa.loc[sa['Species'] == 'Dragon'].count()[0] + sa.loc[sa['Species'] == 'Dragons'].count()[0]],
  ['German Shepherd', sa.loc[sa['Species'] == 'GermanShepherd'].count()[0]],
  ['Goat', sa.loc[sa['Species'] == 'Goat'].count()[0]],
  ['Golden Retriever', sa.loc[sa['Species'] == 'GoldenRetriever'].count()[0]],
  ['Hyena', sa.loc[sa['Species'] == 'Hyena'].count()[0]],
  ['Jackalope', sa.loc[sa['Species'] == 'Jackalope'].count()[0]],
  ['Kenga', sa.loc[sa['Species'] == 'Kenga'].count()[0]],
  ['Kitsune', sa.loc[sa['Species'] == 'Kitsune'].count()[0]],
  ['Labrador', sa.loc[sa['Species'] == 'Labrador'].count()[0]],
  ['Leopard', sa.loc[sa['Species'] == 'Leopard'].count()[0]],
  ['Lizard', sa.loc[sa['Species'] == 'Lizard'].count()[0]],
  ['Meercat', sa.loc[sa['Species'] == 'Meercat'].count()[0]],
  ['Omnikin', sa.loc[sa['Species'] == 'Omnikin'].count()[0]],
  ['Opossum', sa.loc[sa['Species'] == 'Opossum'].count()[0]],
  ['Otter', sa.loc[sa['Species'] == 'Otter'].count()[0]],
  ['Owl', sa.loc[sa['Species'] == 'Owl'].count()[0]],
  ['Phox', sa.loc[sa['Species'] == 'Phox'].count()[0]],
  ['Poodle', sa.loc[sa['Species'] == 'Poodle'].count()[0]],
  ['Porcupine', sa.loc[sa['Species'] == 'Porcupine'].count()[0]],
  ['Pup', sa.loc[sa['Species'] == 'Pup'].count()[0]],
  ['Raptor', sa.loc[sa['Species'] == 'Raptor'].count()[0]],
  ['Reindeer', sa.loc[sa['Species'] == 'Reindeer'].count()[0]],
  ['Sabertooth', sa.loc[sa['Species'] == 'Sabertooth'].count()[0]],
  ['Skunk', sa.loc[sa['Species'] == 'Skunk'].count()[0]],
  ['Snew Leopard', sa.loc[sa['Species'] == 'SnewLeopard'].count()[0]],
  ['Surmelle', sa.loc[sa['Species'] == 'Surmelle'].count()[0]],
  ['Turtle', sa.loc[sa['Species'] == 'Turtle'].count()[0]],
  ['Velociraptor', sa.loc[sa['Species'] == 'Velociraptor'].count()[0]],
  ['Tigers', sa.loc[sa['Species'] == 'WhiteTiger'].count()[0] + sa.loc[sa['Species'] == 'Tiger'].count()[0]],
  ['Winged Wolf', sa.loc[sa['Species'] == 'WingedWolf'].count()[0]],
  # ['Wusky', sa.loc[sa['Species'] == "Wolf/Husky"].count()],[0] # this throws a syntax error due to slash being parsed :sadge:
  ['Wuskylynx', sa.loc[sa['Species'] == 'Wuskylynx'].count()[0]],
  ['Lion', sa.loc[sa['Species'] == 'Lion'].count()[0] + sa.loc[sa['Species'] == 'LionCub'].count()[0]],
  ['Mice', sa.loc[sa['Species'] == 'Mice'].count()[0] + sa.loc[sa['Species'] == 'Mouse'].count()[0]],
  ['Panda', sa.loc[sa['Species'] == 'Panda'].count()[0] + sa.loc[sa['Species'] == 'Pandas'].count()[0]],
  ['Red Panda', sa.loc[sa['Species'] == 'RadPanda'].count()[0] + sa.loc[sa['Species'] == 'RedPanda'].count()[0]],
  ['Rabbit', sa.loc[sa['Species'] == 'Bunny'].count()[0] + sa.loc[sa['Species'] == 'Rabbit'].count()[0]],
  ['Fox', sa.loc[sa['Species'] == 'ArcticFox'].count()[0] + sa.loc[sa['Species'] == 'Fox'].count()[0] + sa.loc[sa['Species'] == 'Foxes'].count()[0]],
  ['Raccoon', sa.loc[sa['Species'] == 'Raccoon'].count()[0]],
  ['Wolves', sa.loc[sa['Species'] == 'Wolf'].count()[0] + sa.loc[sa['Species'] == 'Wolf?'].count()[0] + sa.loc[sa['Species'] == 'Wolves'].count()[0]]
]

total = pandapaco.DataFrame(huge_chunk_of_abominaton, columns = ["Species", "Count"])
total.set_index('Species')
total_fr = total.sort_values(total.columns[1], ascending=False)

# Saves to a CSV file -- will rework this sooner or probably never
# with open('data/csv/species_min.csv', 'w') as f:
  # species_final = total_fr.to_string(index=False)
  # f.write(species_final)

# species_final_csv = pandapaco.read_csv('data/csv/species_min.csv')
displayhook(total_fr.head(10))
