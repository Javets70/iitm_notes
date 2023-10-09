# Clustering 
Clustering is a technique in unsupervised machine learning that involves 
grouping similar data points together into clusters or groups based 
on some similarity or distance measure. The goal of clustering is 
to discover hidden patterns, structures, 
or natural groupings within a dataset without 
any prior knowledge of the groups or categories.

## Problems with Clustering
> The goal of this weak is to understand the information about
datapoints which are clustered together.

If we were to cluster datapoints into $k$ different clusters 
the total number of ways $n$ datapoints can be clustered is 
$k^n$ (this includes empty clusters).

For a set of datapoints from $\{x_1 , x_2  , x_3 .... x_n \}$ 
and the cluster indicators from $\{z_1 , z_2 , z_3 , .... z_n \}$ ,
we need to develop a metric to get an idea of how good the 
clusters are.

A common algorithm which can be used for this purpose is to 
measure the distance of the datapoints from the mean of their 
respective clusters and summing those values for each cluster 
individually , a lower value indicates that the points are closely
packed within a cluster , while a higher value indicates that the 
points are spread apart.

This algorithm can formalized into a function as follows 

$$ F(z_1 , z_2 , z_3 , .... z_n ) = \sum_{i=1}^{n} ||x_i - u_{z_i}||_2^2 $$

where $\mu_{z_i}$ is mean of each $z_i^{th}$ cluster.

This way of clustering is considered an NP-Hard problem and 
its computationally intensive as there are total of $k^n$ possible
combinations of datapoints.

## K-Means Algorithm
To solve the above problem of clustering we will take a look 
at K-Means Algorithm.

The first step is **Initialization** , where each cluster 
indicator is assigned a cluster between $1$ to $k$ for the 
$0^{th}$ iteration.

$$ z_1^0 , z_2^0 , z_3^0 , .... z_n^0  \;\;\;\; \in \{1,2,3, .... k \}$$

Then until Convergence ,

We first compute the mean of each cluster for the $t^{th}$ iteration.

$$ \mu_k^t = \frac{\sum_{i=1}^{n}x_i \mathbb{1}(z_i^t = k)}{\sum_{i=1}^{n}\mathbb{1}(z_i^t = k)} \;\;\;\;\;\; \forall k $$

The next step is reassignment of the datapoints,

$$ Z_i^{t+1} = \underset{k}{\text{arg } \min} ||x_i  - \mu_t^k ||_2^2 $$

This step compares every point's distance to the mean of every other cluster ,
if the distane to the mean is strictly less than the distance to mean 
of the current cluster then the datapoint is assigned to the next cluster.

!!! note 
    K-Means Algorithm does not always produce the optimal solution but 
    usally produces reasonable clusters.

> But what if the algorithm never actually converges?

