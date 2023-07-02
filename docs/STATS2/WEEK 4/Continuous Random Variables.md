# Cumulative Distribution Function 
It is a function that describes the probability distribution of a random variable by specifying the probability that the random variable takes on a value less than or equal to a given value.

The CDF of a random variable $X$ , denoted $F_X(X)$ , is a function from $\mathbb{R} \to [0,1]$ is defined as 

$$F_X(X) = P(X \leq x)$$

!!! info "Properties"
    - $F(X)$ is always a non-decreasing funciton taking values between 0 and 1.
    - $P(a < X \leq b) = F_X(b) - F_X(a)$
    - As $X \to - \infty$ , $F_X$ goes to 0.
    - As $X \to  \infty$ , $F_X$ goes to 1.
    - Probability of $X$ taking a specific value is always 0.


## CDF Of [Standardised Variables](../WEEK 3/Expectation of Random Variables.md#standardized-random-variables)
Let a discrete random variable $X$ have a CDF $F_X$. Assume that $Y = \frac{X - \mu}{\sigma}$ , where $\mu$ and $\sigma$ are the mean and standard deviation of $X$  respectively. If $F_Y$ is the CDF of $Y$ , then 

$$F_Y(y) = F_X(\mu + Y \sigma)$$

# Continuous Random Variable 
A continuous random variable is a type of random variable that can take on any value within a specified range or interval. Unlike discrete random variables, which can only assume a countable set of distinct values, continuous random variables have an infinite number of possible values within a given range.

A random variable $X$ with CDF $F_X(x)$ is said to be continuous random variable if $F_X(x)$ is continuous at every $x$.

!!! info "Properties"
    - $P(X =x) = 0$ for all $x$
    - $\therefore P(a \leq X \leq b) = P(a < X \leq b) = P(a \leq X < b) = P(a < X < b)$
    - Graphs of continuous random variables never breaks at any point and does not jump from one value to another.
    - Probability of $X$ falling in an interval will be nonzero 


## Probability Density Functions 
Probability Density Function (PDF) is a function that describes the probability distribution of a continuous random variable. 

The PDF represents the relative likelihood of different outcomes or values occurring within that range. It is typically denoted as $f(x)$, where $x$ is the variable, and the integral of the PDF over a specific interval gives the probability of the random variable falling within that interval.

$$\int^{b}_{a}f(x) dx = F(b) - F(a) = P(a < X < b)$$

!!! info "Properties"
    - The PDF must be non-negative for all values of x.
    - The total area under the PDF curve must be equal to 1.

        $\implies \int^{\infty}_{ - \infty} f(x) dx = 1$

## Common Distribution Functions 
| Distribution                                    | PDF                                                                                   | CDF                                                                                              |
|-------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Uniform**       $X \sim Uniform[a,b]$         | $f_X(x) = \begin{cases} \frac{1}{b-a} & a < x < b\\ 0 & \text{otherwise} \end{cases}$ | $F_X(x) = \begin{cases} 0 & x \leq a \\ \frac{x-a}{b-a} & a < x < b \\ 1 & x \geq b \end{cases}$ |
| **Exponential**   $X \sim Exp(\lambda)$         | $f_X(x) = \begin{cases} \lambda \exp(-\lambda x) & x>0 \\ 0 & otherwise \end{cases}$  | $F_X(x) = \begin{cases} 0 & x \leq 0 \\ 1 - \exp(-\lambda x) & x >0 \end{cases}$                 |
| **Normal**        $X \sim Normal(\mu , \sigma^2)$ | $F_X(x) = \frac{1}{\sigma \sqrt{2 \pi}} \exp(- \frac{(x - \mu)^2}{2 \sigma^2})$       | $F_X(x) = \int^{x}_{- \infty} f_X(u)du$                                                          |


