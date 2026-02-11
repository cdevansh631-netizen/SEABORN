#SEABPRN NOTES :-
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# 1- LINE PLOT :-
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




# 2- BAR PLOT :--
# df=pd.read_csv("MARKSHEET.csv")
# #ORDER : By order we can change indexes on x .
# sns.barplot(data=df,x="Roll_Number",y="Percentage",hue="Gender",order=[111,110,109,108,107,106,105,104,103,102,101],palette=["blue","pink"],estimator="median")
# plt.show()




# 3- HISTOGRAM PLOBAR :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.histplot(data=df,bins=3,x="Percentage",hue="Gender",kde=True)
# plt.show()




# 4- SCATTER PLOT :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.scatterplot(data=df,x="Percentage",y="History",hue="Gender",marker="o")
# plt.show()



# 5- HEATMAP PLOT :-
# df=pd.read_csv("MARKSHEET.csv")
# # print(df.head())
# gs=df.groupby("Ethnicity").agg({"Percentage":"mean"})
# # sns.heatmap(gs)
# sns.countplot(data=df,x="Gender")
# plt.show()

# 6- VIOLIN PlOT :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.violinplot(data=df,x="Math")
# plt.show()


# 7- PAIRPLOT SEABORN :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.pairplot(df,hue="Gender")
# plt.show()



# 8-STRIP PLOT SEABORN :-
# df=pd.read_csv("MARKSHEET.csv")
# ##dodge :- When hue is used then dodge is used and parameters in hue u provide do not coincide.
# ##jitter :-jitter add small random movement to data point so they dont overlap.
# sns.stripplot(data=df,x="Ethnicity",y="Percentage",hue="Gender",dodge=False,jitter=3.9)
# plt.show()




# 9- BOX PLOT :-
# df=pd.read_csv("MARKSHEET.csv")
# #orient :- Tell direction of plot .
# #fliersize :- Decide how big the outlier pt.
# sns.boxplot(data=df,y="Percentage",x="Gender",showmeans=True,orient="vertical",fliersize=9)
# plt.show()



# 10- CAT PLOT SEABORN :-

# df=pd.read_csv("MARKSHEET.csv")
# ##CAT PLOT : Stand for categorial plot.
# sns.catplot(data=df,x="Ethnicity",y="Percentage",hue="Gender",kind="violin")
# plt.show()



# 11- BAR PLOT :-
# df=pd.read_csv("MARKSHEET.csv")
# sns.set_style(style="ticks")#whitegrid,ticks
# sns.barplot(data=df,x="Ethnicity",y="Percentage")
# plt.show()


# sns.palplot(sns.color_palette("viridis",3))  #("color","No of Color u want" )
# plt.show()






# 12- MULTIPLE PLOT IN SEABORN :-
# df=pd.read_csv("MARKSHEET.csv")
# a=sns.FacetGrid(df,col="Gender",height=3)
# a.map(sns.barplot,data=df,x="Ethnicity",y="Percentage")
# plt.show()



# 13- RELATIONAL PLOT IN SEABORN :-
# df=pd.read_csv("MARKSHEET.csv")
# ##kind :- U want bar or line plot.
# ##size :- like hue but differentiate on bases of size.(-size=Gender-)
# sns.relplot(data=df,x="Roll_Number",y="Percentage",hue="Gender",kind="line",col="Ethnicity")
# plt.show()


# 14- SWARM PLOT :-
#In strip plot data can be overlap that"s why we use jitter.
#And in SWARM PLOT PT DOESN'T OVERLAP.
# df=pd.read_csv("MARKSHEET.csv")
# sns.swarmplot(data=df,x="Ethnicity",y="Percentage")
# plt.show()



# 15- KDE PLOT SEABORN :-__
# df=pd.read_csv("MARKSHEET.csv")
# #multiple=stacK/fill -- [--USED TO CHANGE COLOR AND DESIGN OF PLOT--]
# sns.kdeplot(data=df,x="Percentage",hue="Gender",multiple="stack")
# plt.show()



# 


# print(df.head())