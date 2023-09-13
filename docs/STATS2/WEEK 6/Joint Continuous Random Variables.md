# Joint Continuous Random Variables 
## Joint Density
A function $f(x,y)$ is said to be a joint density function if 

- $f(x,y) \geq 0$ , i.e. $f$ is non-negative
- $\int \int^{\infty}_{ - \infty} f(x,y)dxdy = 1$
- $f(x,y)$ is piecewise continuous in each random variable.

**support(X,Y)** = $\{(x,y):f_{XY}(x,y) > 0\}$

!!! example
    Let $X$ and $Y$ have joint density 

    $$ f_{XY} = \begin{cases}
    1 & 0 < x < 1 , 0 < y < 1
    \\
    0 & otherwise
    \end{cases} $$

    This specific example is also known as uniform unit square.

To get the probability find the area of the region using integration.

## 2D Uniform Distribution 
For some (reasonable) region $D$ in $\mathbb{R}^2$ with total area $|D|$. 

We say that $(X,Y) \sim D$ if they have the joint density

$$
f_{XY} = \begin{cases}
\frac{1}{|D|} & (x,y) \in D
\\
0 & otherwise
\end{cases}
$$

For any sub region $A$ of $D$ , $P((X,Y) \in A) = \frac{|A|}{|D|} = \frac{\text{Area of A}}{\text{Area of D}}$

## Marginal Density 
Suppose $(X,Y)$ have joint density $f_{XY}(x,y).$ Then,

- $X$ has the marginal density $f_X(x)$ = $\int^{\infty}_{y = - \infty} f_{XY}(x,y)dy$
- $Y$ has the marginal density $f_Y(y)$ = $\int^{\infty}_{x = - \infty} f_{XY}(x,y)dy$

<!-- $D = \{(x, y): [0, 2]\times [0, -2] \cup [-1, 0]\times [0, 1]\}$ -->

## Independence of Random Variables 
$(X,Y)$ with joint density $f_{XY}(x,y)$ are independent if 

$$ f_{XY}(x,y) = f_X(x)f_Y(y) $$

where $f_X(x)$ and $f_Y(y)$ are marginal densities of $X$ and $Y$ respectively.
 
## Conditional Density 
Let $(X,Y)$ be random variables with joint density $f_{XY}(x,y)$. Let $f_X(x)$ and $f_Y(y)$ be the marginal 
densities.

-  For $a$ such that $f_X(a) > 0$ , the conditional density of $Y$ given $X=a$ , 
denoted $f_{Y|X=a}(y)$ , is defined as 

$$ f_{Y|X=a} = \frac{f_{XY}(a,y)}{f_X(a)} $$ 

- For $b$ such that $f_Y(b) > 0$ , the conditional density of $X$ given $Y=b$ ,
denoted $f_{X|Y=b}(x)$ , is defined as 

$$ f_{X|Y=b}(x) = \frac{f_{XY}(x,b)}{f_Y(b)} $$

!!! note "Properties of Conditional Density"
    - Both the conditional densities are valid densities in one dimension. So ,
    the "conditional" random variables $(Y|X=a)$ and $(X|Y=b)$ are well defined.

    - $\text{Joint} = \text{Marginal} \times \text{Conditional}$ , for $x=a$ and $y=b$ such that 
    $f_X(a) > 0$ and $f_Y(b) > 0$ 

    $$ f_{XY}(a,b) = f_X(a)f_{Y|X=a}(b) = f_Y(b)f_{X|Y=b}(a) $$
