import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import rand_score

df = pd.read_csv('./specs/question_1.csv')

plt.figure()
plt.scatter(df[(df['org_cluster'] == 0)]['x'], df[(df['org_cluster'] == 0)]['y'], c='b')
plt.scatter(df[(df['org_cluster'] == 1)]['x'], df[(df['org_cluster'] == 1)]['y'], c='g')
plt.scatter(df[(df['org_cluster'] == 2)]['x'], df[(df['org_cluster'] == 2)]['y'], c='r')
plt.show()
plt.figure()
inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0).fit(df[['x', 'y']])
    inertias.append(kmeans.inertia_)
plt.plot(range(1, 11), inertias, '-')
plt.show()
kmeans = KMeans(n_clusters=3, random_state=0).fit(df[['x', 'y']])
labels = kmeans.labels_
rand = rand_score(df['org_cluster'], labels)
silhouette_avg = silhouette_score(df[['x', 'y']], labels)
print("The silhouette_score is ", silhouette_avg, "The Rand Index is :", rand)
df['cluster_kmeans'] = labels
df.to_csv('output/question_1.csv')
centroids = kmeans.cluster_centers_
plt.figure()
plt.scatter(df[(df['cluster_kmeans'] == 0)]['x'], df[(df['cluster_kmeans'] == 0)]['y'], c='r')
plt.scatter(df[(df['cluster_kmeans'] == 1)]['x'], df[(df['cluster_kmeans'] == 1)]['y'], c='b')
plt.scatter(df[(df['cluster_kmeans'] == 2)]['x'], df[(df['cluster_kmeans'] == 2)]['y'], c='g')
plt.scatter(centroids[0][0], centroids[0][1], c='r', marker='o', s=500)
plt.scatter(centroids[1][0], centroids[1][1], c='b', marker='o', s=500)
plt.scatter(centroids[2][0], centroids[2][1], c='g', marker='o', s=500)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
df = pd.read_csv('./specs/question_2.csv')
dfW = df
del df['NAME']
del df['MANUF']
del df['TYPE']
del df['RATING']
kmeans = KMeans(n_clusters=5, random_state=0, max_iter=100, n_init=5).fit(df)
dfW['config1'] = kmeans.labels_
silhouette_avg = silhouette_score(df, kmeans.labels_)
print( kmeans.inertia_, silhouette_avg)
kmeans = KMeans(n_clusters=5, random_state=0, max_iter=100, n_init=100).fit(df)
df['config2'] = kmeans.labels_
silhouette_avg = silhouette_score(df, kmeans.labels_)
print(kmeans.inertia_,  silhouette_avg)
kmeans = KMeans(n_clusters=3, random_state=0).fit(df)
df['config3'] = kmeans.labels_
silhouette_avg = silhouette_score(df, kmeans.labels_)
print(kmeans.inertia_, silhouette_avg)
df.to_csv('output/question_2.csv')
df = pd.read_csv('./specs/question_3.csv')
del df['ID']
kmeans = KMeans(n_clusters=7, random_state=0, max_iter=100, n_init=5).fit(df)
df['k-means'] = kmeans.labels_
plt.figure()
colors = cm.nipy_spectral(kmeans.labels_.astype(float) / 7)
plt.scatter(df['x'], df['y'], marker=".", s=50, c=colors)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
df_normalize = (df - df.min()) / (df.max() - df.min())
dbscan = DBSCAN(eps=0.4, min_samples=4).fit(df_normalize[['x', 'y']])
df['dbscan1'] = dbscan.labels_
n_clusters_ = len(set(dbscan.labels_))
colors = cm.nipy_spectral(dbscan.labels_.astype(float) / n_clusters_)
plt.figure()
plt.scatter(df_normalize['x'], df_normalize['y'], marker=".", s=50, c=colors)
plt.show()
dbscan = DBSCAN(eps=0.08, min_samples=4).fit(df_normalize[['x', 'y']])
df['dbscan2'] = dbscan.labels_
df_normalize['dbscan2'] = dbscan.labels_
plt.figure()
color = ['r','g','b','k','m','y']
for i in range(-1,5):
    plt.scatter(df_normalize[(df_normalize['dbscan2'] == i)]['x'], df_normalize[(df_normalize['dbscan2'] == i)]['y'],c=color[i], marker='.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
df.to_csv('./output/question_3.csv')
