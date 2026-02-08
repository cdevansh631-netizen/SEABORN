#SEABPRN NOTES :-
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#LINE PLOT :-
# df=pd.DataFrame({"DAYS":[1,2,3,4,5]
# ,"NOP":[50,40,60,30,44]})
# sns.lineplot(data=df,x=df["DAYS"],y=df["NOP"])
# plt.show()


# df=pd.read_csv("MARKSHEET.csv")
## hue :- SEPRATE DATA USING DIFFERENT COLOR .[----In matplot we use 2 plot but by using hue it aumatically create 2 line plot in 1.
## style :- Seprate data using dashed line and marker .
## palette is used to decide colors for multiple groups.
# sns.lineplot(data=df,x="Name",y="Percentage",hue="Ethnicity")
# plt.show()




##BAR PLOT :--
# df=pd.read_csv("MARKSHEET.csv")
# #ORDER : By order we can change indexes on x .
# sns.barplot(data=df,x="Roll_Number",y="Percentage",hue="Gender",order=[111,110,109,108,107,106,105,104,103,102,101],palette=["blue"],estimator="median")
# plt.show()




##HISTOGRAM PLOBAR :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.histplot(data=df,bins=3,x="Percentage",hue="Gender",kde=True)
# plt.show()
# print(df.head())




##SCATTER PLOT :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.scatterplot(data=df,x="Percentage",y="History",hue="Gender",marker="o")
# plt.show()



##HEATMAP PLOT :-
# df=pd.read_csv("MARKSHEET.csv")
# # print(df.head())
# gs=df.groupby("Ethnicity").agg({"Percentage":"mean"})
# sns.heatmap(gs)
# c
# sns.countplot(data=df,x="Gender")
# plt.show()

##VIOLIN PlOT :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.violinplot(data=df,x="Math")
# plt.show()


##PAIRPLOT SEABORN :-
df=pd.read_csv("MARKSHEET.csv")
sns.pairplot(df)
plt.show()