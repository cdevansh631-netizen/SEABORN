import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
# Distribution: hist, kde, box, violin
# Count: countplot
# Individual points: strip, swarm, scatter
# Relationship: line, scatter, heatmap
# Overview (EDA): pairplot, catplot, relplot

import pandas as pd

import pandas as pd

import pandas as pd

import pandas as pd

df = pd.DataFrame({
    "Region": ["East","West","North","South","East","West"] * 5,
    "Product": ["A","B","C","A","B","C"] * 5,
    "Sales": [120,450,80,900,300,150,
              200,600,100,1200,350,180,
              150,500,90,1500,400,220,
              180,700,110,2000,450,260,
              220,850,130,3000,500,300],
    "Profit": [20,90,10,200,60,25,
               30,120,15,300,80,35,
               25,100,12,400,90,40,
               28,140,18,600,110,50,
               35,180,22,900,130,70],
    "Quantity": [2,5,1,8,4,2,
                 3,6,2,10,5,3,
                 2,5,1,12,6,3,
                 3,7,2,15,7,4,
                 4,9,3,20,8,5],
    "Discount": [0.05,0.10,0.00,0.20,0.15,0.05,
                 0.10,0.15,0.05,0.25,0.20,0.10,
                 0.05,0.10,0.00,0.30,0.25,0.15,
                 0.10,0.20,0.05,0.35,0.30,0.20,
                 0.15,0.25,0.10,0.40,0.35,0.25],
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"] * 5
})



#DISTRIBUTION :__HIST,VIOLIN,BOX,KDE :-

# sns.histplot(data=df,x="Profit",hue="Product")
# sns.boxplot(data=df,y="Sales",showmeans=True)
# sns.violinplot(data=df,y="Quantity")
# sns.kdeplot(data=df,x="Quantity",hue="Product",multiple="stack")
# plt.show()



#FOR COUNT :-
# sns.countplot(data=df,x="Profit")


# INDIVIDUAL POINT :-Strip,swarp,scatter :_
# sns.scatterplot(data=df,x="Sales",y="Profit",hue="Region") ...IN THIS PTS ARE OVERLAPING BUT..
# sns.stripplot(data=df,x="Month",y="Sales",hue="Region",dodge="True")  #POINT MAY OVERLAP BUT USEFULL FOR LARGE DATASET.
# sns.swarmplot(data=df,x="Month",y="Sales",hue="Region")   #Do not overlap.
# plt.show()



#RELATIOINSHIP :-Line,Scatter,Heatmap :-
# sns.lineplot(data=df,x="Month",y="Sales",hue="Region")
# sns.scatterplot(data=df,x="Discount",y="Profit",markers="s",hue="Region")
# gs=df.groupby("Region").agg({"Profit":"mean"})
# sns.heatmap(gs)
# plt.show()




#OVERVIW EDA :- PAIPLOT,CATPLOT,REPLOT :-
# sns.pairplot(data=df,hue="Region")
# sns.catplot(data=df,x="Month",y="Sales",hue="Product",kind="bar")
# sns.relplot(data=df,x="Month",y="Sales",kind="line",col="Region")
plt.show()