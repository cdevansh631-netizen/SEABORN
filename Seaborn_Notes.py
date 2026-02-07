#SEABPRN NOTES :-
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#LINE PLOT :-
# df=pd.DataFrame({"DAYS":[1,2,3,4,5]
# ,"NOP":[50,40,60,30,44]})
# sns.lineplot(data=df,x=df["DAYS"],y=df["NOP"])
# plt.show()


df=pd.read_csv("MARKSHEET.csv")
## hue :- In matplot we use 2 plot but by using hue it aumatically create 2 line plot in 1.
sns.lineplot(data=df,x="Name",y="Percentage",hue="Gender",style="Ethnicity")
plt.show()
