Suppose $X$ is a random variables defined in the range of $T_X$ and PMF of $X$ is $f_X$ . The expected value of the random variables $X$ will be
$$
E[X] = \sum_{t \in T_X} t \times f_X(t) = \sum_{t \in T_X} t \times P(X =t)
$$


````ad-note 
$E[X]$ has the same unit of $X$

$E[X]$ may or may not belong to range of $X$

```ad-info 
title: Expectation Properties
$E[c \times X] = c \times E[X]$ , where $c$ is a constant and $X$ is a random variable.

$E[X + Y] = E[X] + E[Y]$ , where $X$ and $Y$ are 2 random variables.
$E[X - Y] = E[X] + E[Y]$ , this is right dont worry (to future self)


**If X and Y are independent**

$E[XY] = E[X]E[Y]$
```
````


# Types of Random Variables 
## Uniform Random Variable 
Given that , $X \sim Uniform \set{a , a+1 , a+2 , ... b}$
$$
E[X] = \frac{a+b}{2}
$$
### Variance 
$$
Var(X) = \frac{(b-a)^2}{12} = \sigma^2
$$


## Geometric Random Variable
Given that , $X \sim Geometric(p)$
$$
E[X] = \sum^{\infty}_{t=1} t(1-p)^{t-1}p = \frac{1}{p}
$$
### Variance 
$$
Var(X) = \frac{1-p}{p^2} = \sigma^2
$$


## Poisson Random Variable 
Given that , $X \sim Poisson(\lambda)$
$$
E[X] = \sum^{\infty}_{t = 0} t \times e^{- \lambda} \times \frac{\lambda ^ {t}}{t!} = \lambda
$$
### Variance 
$$
Var(X) = \lambda = \sigma^2
$$


## Binomial Random Variable 
Given that , $X \sim Binomial(n,p)$
$$
E[X] = \sum^{n}_{t=0} t \times {n \choose x} p^t (1-p)^{n-t} = np
$$
### Variance 
$$
Var(X) = np(1-p) = \sigma^2
$$

## Bernoulli Random Variable 
Given that , $X \sim Bernoulli(p)$
$$
E[X] = 0(1-p) + p = p
$$
### Variance 
$$
Var(X) = p(1-p) = \sigma^2
$$



# Variance and Standard Deviation Properties 
Let $X$ be a random variable. Let $a$ be a constant real number.
$$
Var(X) = E[X^2] - E[X]^2
$$

````ad-info 
title: Variance Properties 
- $Var(aX) = a^2Var(X)$
- $SD(aX) = |a|SD(X)$
- $Var(X + a) = Var(X)$
- $SD(X + a) = SD(X)$

```ad-info 
**If X and Y are independent**

$Var(X+Y) = Var(X) + Var(Y)$
```
````



# More Important Formulas 
## Standardized Random Variables 
A random variable $X$ is said to be standardized if $E[X] = 0 , Var(X) = 1$

Also,
If $X$ is a random variable.  Then,
$$
\frac{X - E[X]}{SD(X)}
$$
is a standardized random variable.

## Covariance Formula
$$
Cov(X,Y) = E[XY] - E[X] \times E[Y]
$$

## Correlation Coefficient 
$$
Cor(X,Y) = \frac{Cov(X,Y)}{SD(X) \times SD(Y)}
$$

# Bounds In Probabilities 
## Markov's Inequality 
Let $X$ be a random variable.
$$
P(X \geq a) \leq \frac{E(X)}{a}
$$
```ad-example
A shopkeeper sells mobile phones. The expected demand for mobile phones is 4 per week. $X$ is denoting the number of phones sold in a week.

$$
P(X \geq 10) \leq 0.4
$$

Also, 

$P(X < 10) \geq 0.6$
```

## Chebyshev's Inequality 
Let $X$ be a random variable with mean $\mu$ and finite variance $\sigma^2$ , then for any real number $k>0$
$$
P(|X - \mu| < k \sigma) \geq 1 - \frac{1}{k^2}
$$
**Also,**
$$
P(|X - \mu| \geq k \sigma) \leq \frac{1}{k^2}
$$


