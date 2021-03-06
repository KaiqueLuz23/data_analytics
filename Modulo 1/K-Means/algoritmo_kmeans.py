# importando as bibliotecas
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# exemplo K-Means

# dataset
dataset = np.array([[1,4],[2,2],[2,5],[3,3],[3,5],[4,7],[5,6],[6,4],[6,7],[7,6],[7,9],[8,7],[8,9],[9,4],[9,8]])

plt.scatter(dataset[:,0], dataset[:,1])
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10)
pred_y = kmeans.fit_predict(dataset)

plt.scatter(dataset[:,0], dataset[:,1])
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=70, c='red')
plt.show()

plt.scatter(dataset[:,0],dataset[:,1], c=pred_y)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=70, c='red')

X, y = make_blobs(n_samples=500, centers=50, random_state=0)
plt.scatter(X[:,0], X[:,1])

wcss = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 20), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=pred_y)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s=50, c='red')
plt.show()
