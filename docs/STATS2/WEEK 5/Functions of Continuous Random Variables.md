
# CDF of g(X)
- Suppose $X$ is a continuous random variable with CDF $F_X$ and PDF $f_X$
- Suppose $g : \mathbb{R} \to \mathbb{R}$ is a function.
- Then , $Y = g(X)$ is a random variable with CDF $F_Y$ determined as follows.
$$
F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \in \set{x:g(x) \leq y})
$$

# Monotonic , differentiable functions 
Suppose $X$ is continuous random variable with PDF $f_X$.
Let g(x) be monotonic for $x \in supp(x)$ with derivative $g'(x) = \frac{dg(x)}{dx}$. Then, the PDF of $Y = g(X)$ is 
$$
f_Y(y) = \frac{1}{|g'(g^{-1}(y))|}f_X(g^{-1}(y))
$$
### Translation 
$Y = X + a$
$$
f_Y(y) = f_X(y-a)
$$

### Scaling 
$Y = aX$
$$
f_Y(y) = \frac{1}{|a|}f_X(\frac{y}{a})
$$
### Affine
$Y = aX + b$
$$
f_Y(y) = \frac{1}{|a|}f_X(\frac{y-b}{a})
$$

## Affine transformation of normal distributions 
- Given $X \sim Normal(0,1)$
$$
f_X(x) = \frac{1}{\sqrt{2 \pi}}\exp(\frac{-x^2}{2})
$$
If $Y = \sigma X + \mu$
$$
f_Y(y) = \frac{1}{\sigma \sqrt{2 \pi}}\exp(\frac{-(y - \mu)^2}{2 \sigma^2})
$$
$Y \sim Normal(\mu , \sigma^2)$

- $X \sim Normal(\mu , \sigma^2)$
$Y = \frac{X - \mu}{\sigma} \sim Normal(0,1)$

# Expectation 
Let $X$ be a continuous random variable with density $f(x)$. Let $g : \mathbb{R} \to \mathbb{R}$ be a function. The expected value of $g(X)$, denoted $E[g(X)]$ is given by 
$$
E[g(X)] = \int^{\infty}_{ - \infty} g(X)f_X(x)dx
$$
whenever the above integral exists.

### Formulas 
![[Pasted image 20230302183158.png]]



