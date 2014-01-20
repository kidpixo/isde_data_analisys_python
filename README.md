# ISDE Earthquake data with python

My first attempt to analyze data from [Italian Seismological Instrumental and Parametric Data (ISDE)](http://iside.rm.ingv.it/) using some python libraries, namely:

- numpy
- pylab & matplotlib
- pandas
- scikit-learn

## How to use it

first of all download the data from [ISDE](http://iside.rm.ingv.it/) and adapt the path in the `.py` file or use the data I put in the repository [here](https://raw2.github.com/kidpixo/isde_data_analisys_python/master/events.csv)

Output :

**Data visualization**
![](https://dl.dropboxusercontent.com/u/4762299/github_img/isde_data_analisys_python/XYZ_data_plot.png)

**Kernel PCA reconstructed data**
![](https://dl.dropboxusercontent.com/u/4762299/github_img/isde_data_analisys_python/KPCA_reconstructed.png)

** PCA components **
![](https://dl.dropboxusercontent.com/u/4762299/github_img/isde_data_analisys_python/PCA_components.png)


** Classification on lat,lon,prof with k-means **
![](https://dl.dropboxusercontent.com/u/4762299/github_img/isde_data_analisys_python/kmeans_classes.png)