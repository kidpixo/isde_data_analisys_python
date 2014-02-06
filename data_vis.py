import numpy as np
import pylab as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn import cluster
from sklearn import preprocessing
from sklearn.decomposition import PCA, KernelPCA

path = '/Users/damo_ma/Dropbox/work/python/isde/'

df = pd.read_csv(path+'events.csv', header=None,sep=';',skiprows=6,names=['lat','lon','prof','mag','fonte','empty'])

small_df = df #[df.mag > 2]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(small_df.lon.values, small_df.lat.values, small_df.prof.values, c=small_df.mag.values, s=15*small_df.mag.values, marker='o',cmap=plt.cm.RdYlBu_r)
ax.set_zlim3d(small_df.prof.max(),small_df.prof.min())

ax.set_xticks(np.linspace(ax.get_xlim()[0],ax.get_xlim()[1],4))
ax.set_yticks(np.linspace(ax.get_ylim()[0],ax.get_ylim()[1],4))
ax.set_zticks(np.arange(small_df.prof.min().astype('int'),small_df.prof.max().astype('int')+1,10))

ax.set_xlabel('Lon')
ax.set_ylabel('Lat')
ax.set_zlabel('Prof')
plt.show()

# analysis
class_data_index = [0,1,2] # which column from the data frame?
small_data = small_df.ix[:,class_data_index].values

# Principal components analysis : which is the data dimensionality?

kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
small_data_kpca = kpca.fit_transform(small_data)
small_data_kpca_back = kpca.inverse_transform(small_data_kpca)
small_data_kpca.shape,small_data_kpca_back.shape


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(small_data_kpca_back[:,0], small_data_kpca_back[:,1], small_data_kpca_back[:,2], c=small_df.mag.values, s=15*small_df.mag.values, marker='o',cmap=plt.cm.RdYlBu_r)
ax.set_zlim3d(small_df.prof.max(),small_df.prof.min())
ax.set_xticks(np.linspace(ax.get_xlim()[0],ax.get_xlim()[1],4))
ax.set_yticks(np.linspace(ax.get_ylim()[0],ax.get_ylim()[1],4))
ax.set_zticks(np.arange(small_df.prof.min().astype('int'),small_df.prof.max().astype('int')+1,10))

plt.title("KernelPCA reconstructed data")
plt.show()

pca = PCA(n_components = 'mle')
pca.fit(small_data)

print(pca.explained_variance_)
print(pca.explained_variance_ratio_) 
# As we can see, only the 2 first components are useful
pca.n_components = 2
small_data_pca = pca.fit_transform(small_data)
small_data.shape,small_data_pca.shape

plt.figure()
plt.title("PCA explained variance")
plt.plot(np.arange(pca.explained_variance_ratio_.size),pca.explained_variance_ratio_)
plt.plot(np.arange(pca.explained_variance_ratio_.size),pca.explained_variance_ratio_, "r.")
ax.set_yscale('log')
plt.show()

plt.figure()
plt.title("PCA Projected data")
plt.scatter(small_data_pca[:,0], small_data_pca[:,1], s=15*small_df.mag.values, marker='o',cmap=plt.cm.RdYlBu_r,c=small_df.mag.values)

plt.xlabel('PCA 1st component')
plt.ylabel('PCA 2nd component')
plt.show()

# classification 
n_clusters = 3 # how many classes? 

# generate classifier object
k_means = cluster.KMeans(n_clusters=n_clusters)
# define the classes
k_means.fit(small_data)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(small_df.lon.values, small_df.lat.values, small_df.prof.values, c=k_means.labels_, s=15*small_df.mag.values, marker='o',cmap=plt.cm.RdYlBu_r)
ax.set_zlim3d(small_df.prof.max(),small_df.prof.min())
ax.set_xticks(np.linspace(ax.get_xlim()[0],ax.get_xlim()[1],4))
ax.set_yticks(np.linspace(ax.get_ylim()[0],ax.get_ylim()[1],4))
ax.set_zticks(np.arange(small_df.prof.min().astype('int'),small_df.prof.max().astype('int')+1,10))

ax.set_xlabel('Lon')
ax.set_ylabel('Lat')
ax.set_zlabel('Prof')

plt.show()