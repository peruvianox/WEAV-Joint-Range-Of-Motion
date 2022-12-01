# create dataframe of ROM
ROM = pd.DataFrame(columns=['Subj','Trial','Met','Lumbar','Right Arm','Left Arm','Right Elbow','Left Elbow'])
for k in mag_df.keys():
    ks = k.split('_')
    ROM.loc[len(ROM)] = [ks[2], ks[0]+'_'+ks[1], 'MET', mag_df[k]['Lumbar'][0], mag_df[k]['Right Arm'][0],
                        mag_df[k]['Left Arm'][0],mag_df[k]['Right Elbow'][0], mag_df[k]['Left Elbow'][0]]

len(ROM)



ROM.plot.scatter(x='Lumbar', y='Right Arm')
ROM.plot.scatter(x='Left Arm', y='Right Arm')