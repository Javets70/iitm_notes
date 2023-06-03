
Let $X_1 , X_2 , X_3 .... , X_n \sim X$ be iid samples. Let #$(X_i = t)$ denote the number of times t occurs in the samples. The emperical distribution is the discrete distribution with PMF 
$$
p(t) = \frac{\#(X_i = t)}{n}
$$
# Sample Mean 
Let $X_1 , X_2 , ...... X_n$ be iid samples. The sample mean , denoted $\overline{X}$ , is defined to be the random variable.

$$
\overline{X} = \frac{X_1 + X_2 + X_3 + ...... + X_n}{n}
$$
### Expectation 
$E[\overline{X}] = \mu$

### Variance 
$\text{Var} \overline{X} = \frac{\sigma ^2}{n}$

# Sample Variance 
Let $X_1 , X_2 , ...... X_n$ be iid samples. The sample variance, denoted $S^2$ , is defined to be the random variable.

$$S^2 = \frac{(X_1 - \overline{X})^2 + (X_2 - \overline{X})^2 + .... + (X_n - \overline{X})^2}{n-1}$$
where $\overline{X}$ is the sample mean.

```ad-note 
As n increases , sample variance takes values close to distribution variance.
```

### Expectation 
Let $X_1 , X_2 , ...... X_n$ be iid samples whose distribution has a finite variance $\sigma^2$. 
The sample variance $S^2$ has expected value given by 
$$E[S^2]=\sigma^2$$

# Sample Proportion 
The sample proportion of $A$ , denoted $S(A)$ , is defined as
$$
S(A) = \frac{\# (X_i \text{for which A is true})}{n}
$$

```ad-note 
As $n$ increases , values of S(A) will be close to P(A).
```

### Expectation 
Let $X_1 , X_2 , ...... X_n$ be iid samples whose distribution of $X$. Let $A$ be an event defined using $X$ and let $P(A)$ be the probability of $A$. The sample proportion of $A$ , denoted $S(A)$ , 
has expected value given by
$$
E[S(A)] = P(A)
$$
### Variance 
Variance is given by 
$$
Var(S(A)) = \frac{P(A)(1 - P(A))}{n}
$$

# Sum of Independent Random Variables
Let $X_1 , X_2 , ...... X_n$ be random variables. Let $S = X_1 + X_2 +..... + X_n$ be their sum. Then,
$$
E[S] = E[X_1] + E[X_2]+ ..... E[X_n]
$$
If $X_1 , X_2 ... X_n$ are pairwise uncorrelated, then
$$Var(S) = Var(X_1) + Var(X_2) + .... Var(X_n)$$
### Pairwise Uncorrelated 
$$
E[X_i X_j] = E[X_i] E[X_j]
$$

# Weak Law of Large Numbers 
$$X_1 , X_2 ......X_n \sim \text{iid}X$$
Let $\mu = E[X]$ , $\sigma^2 = Var(X)$
Sample Mean: $\overline{X} =\frac{X_1 + X_2 + ... X_n}{n}$
	Expected value : $\mu$ , Variance : $\frac{\sigma^2}{n}$

### Weak Law 
$$
P(|\overline{X} - \mu|> \delta) \leq \frac{\sigma^2}{n \delta^2}
$$

```ad-note 
- With Probability more than $1 - \frac{\sigma^2}{n \delta^2}$ lies in $[\mu - \delta , \mu + \delta]$


- $\delta > \frac{\sigma}{\sqrt{n}}$
```

### Bernoulli 
For Bernoulli(p) samples 
$$
1 - \frac{p(1-p)}{n\delta^2} 
$$
sample mean lies in  $[p - \delta , p + \delta]$

### Uniform 
For Uniform{-M, .... M} samples
$$
1 - \frac{M(M+1)}{3n\delta^2}
$$
sample mean lies in $[-\delta , \delta]$

### Normal 
For $Normal(0 , \sigma^2)$ 
$$
1 - \frac{\sigma^2}{n\delta^2}
$$
sample mean lies in $[-\delta , \delta]$

### Continuous Uniform 
For $Uniform[-A , A]$ samples 
$$
1 - \frac{A^2}{3n\delta^2}
$$
sample mean lies in $[-\delta , \delta]$
