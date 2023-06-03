A function $f(x,y)$ is said to be a joint density function if 
- $f(x,y) \geq 0$ , i.e. $f$ is non-negative
- $\int \int^{\infty}_{ - \infty} f(x,y)dxdy = 1$
- Technical : $f(x,y)$ is piecewise continuous in each random variable.

**support(X,Y)** = $\set{(x,y):f_{XY}(x,y) > 0}$
```ad-example 
Let $X$ and $Y$ have joint density 
$$f_{XY} = \begin{cases}
1 & 0 < x < 1 , 0 < y < 1
\\
0 & otherwise
\end{cases}$$

This specific example is also known as uniform unit square.
```
To get the probability find the area of the region using integration.

# 2D Uniform Distribution 
For some (reasonable) region D in $\mathbb{R}^2$ with total area $|D|$. We say that $(X,Y) \sim D$ if they have the joint density
$$
f_{XY} = \begin{cases}
\frac{1}{|D|} & (x,y) \in D
\\
0 & otherwise
\end{cases}
$$
For any sub region $A$ of $D$ , $P((X,Y) \in A) = \frac{|A|}{|D|} = \frac{\text{Area of A}}{\text{Area of D}}$

# Marginal Density 
Suppose $(X,Y)$ have joint density $f_{XY}(x,y).$ Then,
- $X$ has the marginal density $f_X(x)$ = $\int^{\infty}_{y = - \infty} f_{XY}(x,y)dy$
- $Y$ has the marginal density $f_Y(y)$ = $\int^{\infty}_{x = - \infty} f_{XY}(x,y)dy$

 $\[D = \{(x, y): [0, 2]\times [0, -2] \cup [-1, 0]\times [0, 1]\}\]$
 