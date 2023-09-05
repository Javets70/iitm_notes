##
# Functions of Continuous Random Variables 
## CDF of g(X)
- Suppose $X$ is a continuous random variable with CDF $F_X$ and PDF $f_X$
- Suppose $g : \mathbb{R} \to \mathbb{R}$ is a function.
- Then , $Y = g(X)$ is a random variable with CDF $F_Y$ determined as follows.

$$ F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \in \{x:g(x) \leq y\}) $$

## Monotonic , differentiable functions 
Suppose $X$ is continuous random variable with PDF $f_X$.
Let g(x) be monotonic for $x \in supp(x)$ with derivative $g'(x) = \frac{dg(x)}{dx}$. Then, the PDF of $Y = g(X)$ is 

$$ f_Y(y) = \frac{1}{|g'(g^{-1}(y))|}f_X(g^{-1}(y)) $$

### Translation 
$Y = X + a$

$$ f_Y(y) = f_X(y-a) $$

### Scaling 
$Y = aX$

$$ f_Y(y) = \frac{1}{|a|}f_X(\frac{y}{a}) $$

### Affine
$Y = aX + b$

$$ f_Y(y) = \frac{1}{|a|}f_X(\frac{y-b}{a}) $$

## Affine transformation of normal distributions 
!!! note ""
    - Given $X \sim Normal(0,1)$

    $$ f_X(x) = \frac{1}{\sqrt{2 \pi}}\exp(\frac{-x^2}{2}) $$

    - If $Y = \sigma X + \mu$

    $$ f_Y(y) = \frac{1}{\sigma \sqrt{2 \pi}}\exp(\frac{-(y - \mu)^2}{2 \sigma^2}) $$

    $$\implies Y \sim Normal(\mu , \sigma^2)$$

!!! note ""
    - $X \sim Normal(\mu , \sigma^2)$

    $$ Y = \frac{X - \mu}{\sigma} \sim Normal(0,1) $$

# Expectation 
Let $X$ be a continuous random variable with density $f(x)$. Let $g : \mathbb{R} \to \mathbb{R}$ be a function. The expected value of $g(X)$, denoted $E[g(X)]$ is given by 

$$ E[g(X)] = \int^{\infty}_{ - \infty} g(X)f_X(x)dx $$

whenever the above integral exists.

### Formulas 
| Distribution                                      | PDF                                                                                   | CDF                                                                                              | Expectation                | Variance                         |
|---------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------|----------------------------------|
| **Uniform**       $X \sim Uniform[a,b]$           | $f_X(x) = \begin{cases} \frac{1}{b-a} & a < x < b\\ 0 & \text{otherwise} \end{cases}$ | $F_X(x) = \begin{cases} 0 & x \leq a \\ \frac{x-a}{b-a} & a < x < b \\ 1 & x \geq b \end{cases}$ | $E[X] = \frac{a+b}{2}$     | $\sigma^2 = \frac{(b-a)^2}{2}$   |
| **Exponential**   $X \sim Exp(\lambda)$           | $f_X(x) = \begin{cases} \lambda \exp(-\lambda x) & x>0 \\ 0 & otherwise \end{cases}$  | $F_X(x) = \begin{cases} 0 & x \leq 0 \\ 1 - \exp(-\lambda x) & x >0 \end{cases}$                 | $E[X] = \frac{1}{\lambda}$ | $\sigma^2 = \frac{1}{\lambda^2}$ |
| **Normal**        $X \sim Normal(\mu , \sigma^2)$ | $F_X(x) = \frac{1}{\sigma \sqrt{2 \pi}} \exp(- \frac{(x - \mu)^2}{2 \sigma^2})$       | $F_X(x) = \int^{x}_{- \infty} f_X(u)du$                                                          | $E[X] = \mu$               | $\sigma^2$                       |



