import pandas as pd
import numpy as np
import csv
data=pd.read_csv('input.csv')
cluster=data['cluster_number'].values
date=data['Date'].values
time=data['Time'].values
mess=data['Message'].values
n_la=data['new_lat'].values
n_lo=data['new_long'].values
#print pd.unique(cluster)
j=[]
X=np.array(list(zip(cluster,date)))
for m in j:
    print m
for i in pd.unique(cluster):
    j.append(i)
#print j
'''for t in cluster:
    if t==j[k]:
        print cluster[t],date[t],time[t],mess[t]
        k=k+1'''
for f in range(len(j)):
    filename = "cluster%d.csv" % (j[f])
    g=open(filename,'wb')
    writer= csv.writer(g)
    k=0
    writer.writerow(['Date','Time','Latitude','Longitude','cluster num','Message'])
    for i in cluster:
        if i==j[f]:
            if k<len(X):
            #print cluster[i],mess[i]
                writer.writerow([date[k],time[k],n_la[k],n_lo[k],cluster[k],mess[k]])
        k=k+1
    g.close()
'''for f in range(len(j)):
    print j[f]'''
'''k=0
for i in cluster:
    if i==4:
        print k+2,'\t',i
    k=k+1'''
