# Cumulative Distribution Function 
The CDF of a random variable $X$ , denoted $F_X(X)$ , is a function from $\mathbb{R} \to [0,1]$ is defined as 
$$
F_X(X) = P(X \leq x)
$$

```ad-info 
title: Properties 

$F(X)$ is always a non-decreasing funciton taking values between 0 and 1.

$P(a < X \leq b) = F_X(b) - F_X(a)$

As $X \to - \infty$ , $F_X$ goes to 0.

As $X \to  \infty$ , $F_X$ goes to 1.
```


## CDF Of Standardised Variables 
Let a discrete random variable $X$ have a CDF $F_X$. Assume that $Y = \frac{X - \mu}{\sigma}$ , where $\mu$ and $\sigma$ are the mean and standard deviation of $X$  respectively. If $F_Y$ is the CDF of $Y$ , then 
$$
F_Y(y) = F_X(\mu + Y \sigma)
$$
```ad-note 
title: CDF Formula and More Properties 
Given a child CDF F(x), there exists a random variable $X$ taking values in $\mathbb{R}$ such that 

$$P(X \leq x) = F(x)$$

Probability of $X$ taking a specific value is always 0.

$P(X = 3) = 0$ for a random variable $X$.
```


# Continuous Random Variable 
A random variable $X$ with CDF $F_X(x)$ is said to be continuous random variable if $F_X(x)$ is continuous at every $x$.
- CDF has no jumps or steps.
- So ,$P(X =x) = 0$ for all $x$
- Probability of $X$ falling in an interval will be nonzero $$P(a < X \leq b) = F(b) - F(a)$$
$$
\therefore P(a \leq X \leq b) = P(a < X \leq b) = P(a \leq X < b) = P(a < X < b)
$$
- Graphs of continuous random variables never breaks at any point and does not from one value to another.

## Probability Density Functions 
They are a much better way to represent random variables on a graph. 
$$
\int^{b}_{a}f(x) dx = F(b) - F(a) = P(a < X < b)
$$
Also integral of all the values a variable $X$ takes is always 1.
$\implies \int^{\infty}_{ - \infty} f(x) dx = 1$

# Common Distribution Functions 

## Uniform 
$X \sim Uniform[a,b]$

#### PDF 
$$
f_X(x) = \begin{cases}
\frac{1}{b-a} & a < x < b
\\
0 & \text{otherwise}
\end{cases} 
$$

#### CDF 
$$
F_X(x) = \begin{cases}
0 & x \leq a 
\\ 
\frac{x-a}{b-a} & a < x < b
\\ 
1 & x \geq b
\end{cases}
$$

## Exponential 
$X \sim Exp(\lambda)$

#### PDF 
$$
f_X(x) = \begin{cases}
\lambda \exp(-\lambda x) & x>0
\\
0 & otherwise
\end{cases}
$$

#### CDF 
$$
F_X(x) = \begin{cases}
0 & x \leq 0
\\ 
1 - \exp(-\lambda x) & x >0
\end{cases}
$$

## Normal 
$X \sim Normal(\mu , \sigma^2)$

#### PDF 
$$
F_X(x) = \frac{1}{\sigma \sqrt{2 \pi}} \exp(- \frac{(x - \mu)^2}{2 \sigma^2})
$$

#### CDF 
$$
F_X(x) = \int^{x}_{- \infty} f_X(u)du
$$

