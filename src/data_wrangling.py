suns_1_rows = raw_data.loc[raw_data['sy_snum'] == 1 ]

suns_1_planets_1 = suns_1_rows.loc[suns_1_rows['sy_pnum'] == 1]

suns_2_rows = raw_data.loc[raw_data['sy_snum'] == 2 ]

suns_2_planets_1 = suns_2_rows.loc[suns_2_rows['sy_pnum'] == 1]


print("\n Number of planets in single star systems ", suns_1_rows.size)
print("\n Number of binary star systems: ", suns_2_rows.size)
print("\n Number of single star, single planets: ", suns_1_planets_1.size)
print("\n Number of binary star, single planets: ", suns_2_planets_1.size)

print("\n\n Single star, single planets are henceforth called: 'Sample 1'")
print("\n Binary star, single planets are henceforth called: 'Sample 2'")

sample1 = suns_1_planets_1['pl_eqt']
sample2 = suns_2_planets_1['pl_eqt']

sample1 = sample1.dropna()
sample2 = sample2.dropna()

print("\n\n 'NA' temps removed from Sample 1, now contains:", sample1.size, "planets.")
print("\n 'NA' temps removed from Sample2, now contains:", sample2.size, "planets.")



