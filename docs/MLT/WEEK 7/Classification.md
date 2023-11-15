# Classification
## Introduction to Binary Classification 
For a set of datapoints $\{ x_1 , x_2 , x_3 ... x_n \}$ where 
$x \in \mathbb{R}^d$ and labels $\{ y_1 , y_2 , y_3 ... y_n \}$ 
where $y \in \{ 0,1 \} / \{ -1,1 \}$.
Our goal is to get a function $h$ which maps the datapoints 
to the classes ($h:\mathbb{R}^d \to \{ 0,1 \}$).

### Loss Function 

$$\text{Loss}(h) = \frac{1}{n} \sum_{i=1}^n \mathbb{1}(h(x_i) \neq y_i)
\quad \quad \quad \mathbb{1}(z) = \begin{cases} 1 & \text{if true} \\
0 & \text{otherwise} \end{cases}$$

> Like in the case of linear regression , where we restricted the 
space for the loss function , to a linear space ; We can do something 
similar to that here too

$$\begin{equation*}
\begin{split}
\underset{h \in \mathcal{H}_\text{linear}}{\min} \sum_{i=1}^n \mathbb{1}(h(x_i) \neq y_i) \\
\\
\text{where,}\\
\\
\mathcal{H}_\text{linear} = \{ h_w : h_w(x) = \text{sign}(w^T x) \} \\
\text{sign}(z) = \begin{cases} 1 & \text{if z>0} \\ 0 & \text{otherwise} \end{cases}
\end{split}
\end{equation*}$$

![](img/linear_loss.png)

> The above problem is an NP-Hard Problem in general.
In regression we used to take the gradient , set it to zero and find 
the $w$, that doesnt apply here because the loss here can only take 2 
discrete values (0 or 1) which makes this loss function non - differentiable
an non - continuous.

Can we somehow use linear regression to solve for this classification
problem?

For a dataset $\{(x_1 , y_1) , (x_2,y_2) , ... (x_n , y_n) \}$ , then we input
this dataset to a linear regression model which gives out a $w \in \mathbb{R}^d$.
At the end we use this $w$ to get $h_w$ by solving for $w^Tx =0$ ($h_w : \mathbb{R}^d \to \{ 0,1 \}$).

> Is this a good idea? Does this help us?

![](img/datapoint_loss_func.png)

Now if we add more positive label datapoints ,
![](img/skewed_loss_func.png)

We can see that the $w$ gets skewed which in turn changes $h_w$.
The above algorithm depends on a linear regression model which solves for $w$
by taking into account all the datapoints.

From a linear classification point of view , the classifying line $h_w$ shouldnt 
be changed when new datapoints are introduced on either side but from a
regression point of view these datapoints which are far apart from the classifying line 
,we are trying to minimize over all the datapoints , because of which  our $w$ gets 
tilted back and forth. 

> This will give us lines which dont actually classify the datapoints properly.

!!! abstract "Conclusion"
    Regression is sensitive to location of the datapoints and not just the 
    "side" on which the data lies with respect to the separator. 

## K-Nearest Neighbours (KNN)
> For some set of datapoints with corresponding labels , if a new datapoint's (for which we predict the label)
belongs to the training dataset , then we already have an answer for its (new datapoint's) label,
but what to do when it doesnt belong to the training dataset?

- Given a test points $x_\text{test} \in \mathbb{R}^d$ , find the closest 
point $x^*$ to $x_\text{test}$ in the training set.

- Predict $y_\text{test} = y^*$

> Is this a good algorithm? 

!!! failure "Issues with this algorithm" 
    - This algorithm can get affected by outliers. 
    - Lets say our nearest point to $x_\text{test}$ happens to be an outlier,
    then our algorithm will predict the same value as $y^*$ , which may label
    the point wrongly.

!!! note "Simple Fix for Issue Above"
    - Given $x_\text{test}$ , find the $k$ closest points in the training dataset 
    $(x_1^* , x_2^* , ... x_k^*)$.
    - Predict $y_\text{test} = \text{Majority}(y_1^* , y_2^* , ... y_k^*)$

We have to supply the parameter $k$ for the above fix , which the data does 
not tell us, so how many neighbours we should look for?

### Decision Boundry 
#### Case 1 (k = 1)
Lets look at the case when $k=1$,

![](img/dec_boundry_k1.png)

**Note** that these datapoints already have specified labels which comes from
the dataset.

Because $k=1$ we get "holes" in certain regions for the decision boundry,
looking at it objectively the blue point in the red region and vis a vis are 
certainly outliers and should be ignored , but **our classification algorithm is 
sensitive to outliers.**

Also on the extreme right end we can see that there are some red points , which makes 
the whole area on the right region as red , ideally that should have been blue , 
as those extreme right red points are outliers.

> Now we know that taking $k=1$ is a bad idea. ;C

#### Case 2 (k=n)
Now lets look at the case when $k=n$

**Note** that these datapoints already have specified labels which comes from
the dataset.

![](img/dec_boundry_kn.png)

Our algorithm here considers all the datapoints as closest , because $k=n$ , 
hence we take the majority of the labels and make the decision boundry.
In our case the majority of the labels are blue (negative) and hence the whole 
region is considered to be blue (negative).

In other words if we do a prediciton for a label of some point ,
our answer will always be negative (blue) label.

!!! warning "Problems Encountered"
    - Asking too few ($k=1$) neighbours gives us an outlier issue.
    - Asking too many ($k=n$) neighbours gives us the "majority label".

> What to do then?

We must find such a $k^*$ that it ignores the outliers and yet it maintains 
a resonable decision boundry.

![](img/dec_boundry_k_star.png)

> How do find the right number of neighbours ($k^*$)?

#### Chossing k*
We know that we can treat $k$ as an hyperparameter , because its not a part of 
the algorithm but rather the input which goes into the algorithm.

- We also know that , smaller the $k$ the more complicated the decision boundry is.
- To solve this , we choose different values of $k$ and cross validate for them 
respectively.

!!! failure "Issues with KNN Algorithm"
    - Choosing distance function (to identify the closest $k$ neighbours) might 
    become an issue.
    - When predicting a new datapoint $x_\text{test}$ we measure the distance of 
    $x_\text{test}$ from **all** the datapoints and then identify the $k$ nearest neighbours.
    Now if we want to predict the label for another datapoint , we have to repeat the whole 
    procedure again. This shows that we dont actually learn a "model" and our algorithm 
    solely relies on the datapoints. We cannot throw away the datapoints after learning a 
    "model" , because in the first place , **there is no model for KNN**.
    This is the biggest issue with KNN Algorithm.

## Introduction to Decision Trees 
The input for decision tree algorithm is the usual dataset 
$\{ (x_1,y_1) , (x_2,y_2) , ... (x_n,y_n) \}$ where for all $i$ , 
$x_i \in \mathbb{R}^d$ and $y \in \{ +1,-1 \}$.

The output of this algorithm is a "Decision Tree".

!!! question "What is a Decision Tree?"
    It is a tree-like structure where each internal node represents a 
    decision based on the value of a specific feature, each branch 
    represents the outcome of that decision, and each leaf node 
    represents the final predicted outcome or class label.
