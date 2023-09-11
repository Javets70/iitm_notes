##
# Functions of Continuous Random Variables 

!!! question "Why do we need functions of continuous random variables?"
    We may model one quantity as a random variable $X$. We may have to work with 
    another closely related quantity.
    
    !!! example 
        Length of a square = $X$

        Area of a square = $Y = g(X) = X^2$

## Cumulative Distribution Function of g(X)
If $X$ is a continuous random variable and $Y=g(X)$ is a function of $X$ , then $Y$ itself is 
a random variable. Thus we should be able to find the CDF and PDF of $Y$.

??? note inline end "Relationship between PDF and CDF of a Random Variable"
    <!-- CDF $\xrightleftharpoons[\text{integration}]{\text{differentiation}}$ PDF -->


    CDF $\overset{\text{differentiation}}{\underset{\text{integration}}{\rightleftarrows}}$ PDF


- Suppose $X$ is a continuous random variable with CDF $F_X$ and PDF $f_X$
- Suppose $g : \mathbb{R} \to \mathbb{R}$ is a function.
- Then , $Y = g(X)$ is a random variable with CDF $F_Y$ determined as follows.

$$ F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \in \{x:g(x) \leq y\}) $$

## Monotonic , differentiable functions 
Suppose $X$ is continuous random variable with PDF $f_X$.
Let g(x) be monotonic for $x \in supp(x)$ with derivative $g'(x) = \frac{dg(x)}{dx}$. 

Then, the PDF of $Y = g(X)$ is 

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

## Expectation 
Let $X$ be a continuous random variable with density $f(x)$. 

$$E[X] = \int^{\infty}_{- \infty} x \times f_X(x)dx$$

Also ,

$$E[X^2] = \int^{\infty}_{- \infty} x^2 \times f_X(x)dx$$

Let $g : \mathbb{R} \to \mathbb{R}$ be a function. The expected value of $g(X)$, denoted $E[g(X)]$ is given by 

$$ E[g(X)] = \int^{\infty}_{ - \infty} g(X)f_X(x)dx $$

whenever the above integrals exists.

!!! question "What is the formula for Variance?"
    The formula for variance remains the same

    $$\text{Var}(X) = E[X^2] - (E[X])^2$$

### Formulas 
| Distribution                                      | PDF                                                                                   | CDF                                                                                              | Expectation                | Variance                         |
|---------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------|----------------------------------|
| **Uniform**       $X \sim Uniform[a,b]$           | $f_X(x) = \begin{cases} \frac{1}{b-a} & a < x < b\\ 0 & \text{otherwise} \end{cases}$ | $F_X(x) = \begin{cases} 0 & x \leq a \\ \frac{x-a}{b-a} & a < x < b \\ 1 & x \geq b \end{cases}$ | $E[X] = \frac{a+b}{2}$     | $\sigma^2 = \frac{(b-a)^2}{2}$   |
| **Exponential**   $X \sim Exp(\lambda)$           | $f_X(x) = \begin{cases} \lambda \exp(-\lambda x) & x>0 \\ 0 & otherwise \end{cases}$  | $F_X(x) = \begin{cases} 0 & x \leq 0 \\ 1 - \exp(-\lambda x) & x >0 \end{cases}$                 | $E[X] = \frac{1}{\lambda}$ | $\sigma^2 = \frac{1}{\lambda^2}$ |
| **Normal**        $X \sim Normal(\mu , \sigma^2)$ | $F_X(x) = \frac{1}{\sigma \sqrt{2 \pi}} \exp(- \frac{(x - \mu)^2}{2 \sigma^2})$       | $F_X(x) = \int^{x}_{- \infty} f_X(u)du$                                                          | $E[X] = \mu$               | $\sigma^2$                       |

## Joint Distributions of Discrete and Continuous Random Variables 
Joint distributions involve the simultaneous analysis of two or more random variables. 
When one of these random variables is discrete, and the other is continuous, 
we have a joint distribution of a discrete and continuous random variable.

!!! example 
    Suppose $X$ represents the number of defective items in a batch (a discrete random variable), 
    and $Y$ represents the time it takes to produce the batch (a continuous random variable). 
    The joint distribution would provide the probability of different combinations, such as P(X = 2, 1 ≤ Y ≤ 2),
    which is the probability of having exactly 2 defective items when the production time is between 1 and 2 hours.

### Joint Probability of Continuous Given Discrete 
Let $X$ and $Y$ be two random variables with $X$ being a discrete random variable and $Y$ being a continous random variable.

- $X$ has the range $T_X$ and PMF $p_X(x)$
- For each $X \in T_X$ , we have continous random variable $Y_X$ with density $f_{Y_X}(y)$ where,
$Y_X$ is $Y$ given $X=x$ , denoted as $(Y|X=x)$.
- $f_{Y_X}(y)$ conditional density of $Y$ given $X=x$ can be denoted as $f_{Y|X=x}(y)$

$\therefore$ Marginal density of $Y$ will be,

$$ f_Y(y) = \sum_{x \in T_X} p_X(x)f_{Y|X=x}(y) $$

### Joint Probability of Discrete Given Continuous 
Suppose $X$ and $Y$ are jointly distributed with $X \in T_X$ being discrete with PMF 
$p_X(x)$ and conditional densities $f_{Y|X=x}(y)$ for $x \in T_X$. The conditional 
probability of $X$ given $Y =y_0 \in \text{supp}(Y)$  is defined as 

$$ P(X=x|Y=y_0) = \frac{p_X(x)f_{Y|X=x}(y_0)}{f_Y(y_0)} $$

where $f_Y$ is the marginal density of $Y$.
