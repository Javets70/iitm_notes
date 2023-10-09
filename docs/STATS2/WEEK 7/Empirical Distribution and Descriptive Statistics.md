# Empirical Distribution and Descriptive Statistics 
Let $X_1 , X_2 , X_3 .... , X_n \sim X$ be iid samples. Let $\#(X_i = t)$ denote the number 
of times $t$ occurs in the samples. The emperical distribution is the discrete distribution with PMF 

$$ p(t) = \frac{\#(X_i = t)}{n} $$

??? question "Is the empirical distribution random?"
	- Yes , it depends on the actual sample instances 
	- $t$ and $p(t)$ may change from one sampling to another.
	- Example : 20 $\text{Bernoulli}(p)$ samples.

!!! abstract "Properties of Empirical Distribution"
	- Mean ($\mu$) of the distribution.
	- Variance ($\sigma^2$) of the distribution.
	- Probability of an event
	
	!!! note 
		As number of samples increases , the properties of the 
		emperical distribution should become close to that of the
		original distribution.
	

## Sample Mean 
Let $X_1 , X_2 , ...... X_n$ be iid samples. The sample mean , denoted $\overline{X}$ , is defined to be the random variable.

$$\overline{X} = \frac{X_1 + X_2 + X_3 + ...... + X_n}{n}$$

!!! abstract "Expected Value and Variance"
	$$E[\overline{X}] = \mu , \text{Var}(\overline{X}) = \frac{\sigma ^2}{n}$$

??? info "Properties"
	Expected value of a sample means equals the expected value of mean of distribution 

	- Mean of Distribution:	constant real number and not random 
	- Sample Mean: random variable with mean equal to distribution mean 

	Variance of sample mean decreases with $n$ 

	As $n$ increases :-

	- Variance of sample mean tends to zero 
	- The spread of sample mean will decrease 
	- Sample mean will take values close the distribution mean


## Sample Variance 
Let $X_1 , X_2 , ...... X_n$ be iid samples. The sample variance, denoted $S^2$ , is defined to be the random variable.

$$S^2 = \frac{(X_1 - \overline{X})^2 + (X_2 - \overline{X})^2 + .... + (X_n - \overline{X})^2}{n-1}$$

where $\overline{X}$ is the sample mean.

!!! abstract "Expected Value of Sample Variance"
	Let $X_1 , X_2 , ...... X_n$ be iid samples whose distribution has a finite variance $\sigma^2$. 
	The sample variance $S^2$ has expected value given by 

	$$E[S^2]=\sigma^2$$

??? info "Properties"
	Expected value of sample variane equals the variance of the distribution 

	- Variance of distribution: constant real number and not random 
	- Sample Variance: random variable with mean equal to distribution variance 

	Values of sample variance , on average , give the variance of the distribution 

	- Variance of sample variance will decrease with the number of samples (generally)
	- As $n$ increases , sample variance takes values close the distribution variance 

## Sample Proportion 
The sample proportion of $A$ , denoted $S(A)$ , is defined as

$$S(A) = \frac{\# (X_i \text{ for which A is true})}{n}$$


!!! abstract "Expectation and Variance of Sample Proportion"

	Let $X_1 , X_2 , ...... X_n$ be iid samples whose distribution of $X$. Let $A$ be an event defined using $X$ and let $P(A)$ be the probability of $A$. The sample proportion of $A$ , denoted $S(A)$ , 
	has expected value and variance given by

	$$E[S(A)] = P(A) , Var(S(A)) = \frac{P(A)(1 - P(A))}{n}$$

	!!! note ""
		As $n$ increases , values of S(A) will be close to P(A).

## Sum of Independent Random Variables
Let $X_1 , X_2 , ...... X_n$ be random variables. Let $S = X_1 + X_2 +..... + X_n$ be their sum. Then,

$$E[S] = E[X_1] + E[X_2]+ ..... E[X_n]$$

If $X_1 , X_2 ... X_n$ are pairwise uncorrelated, then

$$Var(S) = Var(X_1) + Var(X_2) + .... Var(X_n)$$

??? question "What is Pairwaise Uncorrelated"
	$$E[X_i X_j] = E[X_i] E[X_j]$$

	for all $i,j$ where $i \neq j$

## Weak Law of Large Numbers 
$$X_1 , X_2 ......X_n \sim \text{iid }X$$

Let $\mu = E[X]$ , $\sigma^2 = Var(X)$

Sample Mean: $\overline{X} =\frac{X_1 + X_2 + ... X_n}{n}$

Expected value : $\mu$ , Variance : $\frac{\sigma^2}{n}$

### Weak Law 

$$P(|\overline{X} - \mu|> \delta) \leq \frac{\sigma^2}{n \delta^2}$$

!!! note
	- With Probability more than $1 - \frac{\sigma^2}{n \delta^2}$ lies in $[\mu - \delta , \mu + \delta]$


	- $\delta > \frac{\sigma}{\sqrt{n}}$

### Bernoulli 
For Bernoulli(p) samples 

$$1 - \frac{p(1-p)}{n\delta^2}$$

sample mean lies in  $[p - \delta , p + \delta]$

### Discrete Uniform 
For $\text{Uniform}\{-M, .... M\}$ samples

$$1 - \frac{M(M+1)}{3n\delta^2}$$

sample mean lies in $[-\delta , \delta]$

### Normal 
For $\text{Normal}(0 , \sigma^2)$ 

$$1 - \frac{\sigma^2}{n\delta^2}$$

sample mean lies in $[-\delta , \delta]$

### Continuous Uniform 
For $\text{Uniform}[-A , A]$ samples 

$$1 - \frac{A^2}{3n\delta^2}$$

sample mean lies in $[-\delta , \delta]$
