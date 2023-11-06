# Regression
## Goodness of Maximum Likelihood Estimator for linear Regression 
In the previous week we observed that $w^*$ which comes from the 
squared error equation is the same as $\hat{w}_{\text{ML}}$ which 
came from the maximal Likelihood equation.

Now we are going to look at $\hat{w}_{\text{ML}}$ and its properties ,
which will gives us a better idea of $w$.
For $\hat{w}_{\text{ML}}$ our assumption was that,

$$y|x = w^T x + \epsilon $$

where $\epsilon$ (gaussian noise) belongs to a gaussian distribution with mean 0 and variance $\sigma^2$ 
($\epsilon \sim \mathcal{N}(0 , \sigma^2)$).
For every $x$ in our data $y$ was generated using some $w^T x$ , using some unknown 
but fixed $w$ and then adding 0 mean gasussian noise to it.

Hence , $y$ given $x$ can be thought of as gaussian distribution with mean $w^T x$ and 
variance $\sigma^2$ ($y|x \sim \mathcal{N}(w^T x , \sigma^2)$)

>  For $\hat{w}_{\text{ML}}$ we should now look for a way to test that ,
how good the function is as a guess from true $w$.

A good function to compare $\hat{w}_{\text{ML}}$  to $w$ is

$${||\hat{w}_{\text{ML}} - w ||}^2$$

and to see what happens to this value on an average we will 
look at its expected value over the randomness in $y$, which can be written as 

$$E[{||\hat{w}_{\text{ML}} - w ||}^2]$$

If we solve for the expected value further , we get

$$E[{||\hat{w}_{\text{ML}} - w ||}^2] = \sigma^2 \text{trace}((XX^T)^ \dagger)$$

where $\sigma^2$ is the variance from the gaussian noise

> $\sigma^2$ in the expected value of the above function cant be reduced , 
it is the variance / loss which will always happen.
Only thing we can reduce is the trace of the inverse of covariance matrix

## Cross-validation for minimizing MSE 
