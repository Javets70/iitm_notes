# Joint Continuous Random Variables 
A continuous random variable can take on an uncountable number of values within a certain range.

!!! example 
    Examples include height, weight, time, temperature, 
    and any measurement that can take on a wide range of real numbers.

Joint Continuous random variables deal with the simultaneous behavior of two or more continuous random variables.

!!! example 
    Consider two continuous random variables, $X$ and $Y$. 
    $X$ represents the time it takes for a customer to arrive at a store,
    and $Y$ represents the amount of money the customer spends during their visit. 
    Both $X$ and $Y$ can take on a wide range of real-number values.

## Joint Probability Density Function (PDF) 
- When dealing with two continuous random variables, $X$ and $Y$, the joint PDF $f_{XY}(x,y)$ 
defines the probability density for every pair of values $(x,y)$ that $X$ and $Y$ can take 
simultaneously.

- This function represents how likely it is for $X$ and $Y$ to jointly fall within a 
specific region in their respective value spaces.

- The integral of this joint PDF over a region of the XY plane gives the probability that (X, Y) falls within that region.

!!! note "Properties of PDF"
    A function $f(x,y)$ is said to be a joint density function if 

    - $f(x,y) \geq 0$ , i.e. $f$ is non-negative
    - $\int \int^{\infty}_{ - \infty} f(x,y)dxdy = 1$
    - $f(x,y)$ is piecewise continuous in each random variable.
    
    ??? question "What does Piecewise Continuous mean?"
        "Piecewise continuous" is a term used to describe a function that is continuous except for a finite number of isolated points or intervals where it may have discontinuities. In other words, a piecewise continuous function can be thought of as a function that is continuous over certain subintervals of its domain but may have jumps or discontinuities at specific points or subintervals.

<!-- **support(X,Y)** = $\{(x,y):f_{XY}(x,y) > 0\}$ -->

!!! example
    Let $X$ and $Y$ have joint density 

    $$ f_{XY} = \begin{cases}
    1 & 0 < x < 1 , 0 < y < 1
    \\
    0 & otherwise
    \end{cases} $$

    This specific example is also known as uniform unit square.

    ---

    In the context of the arrival time and spending example, the joint PDF 
    $f_{XY}(x,y)$ might represent the probability density of a customer arriving at time 
    $x$ and spending $y$ dollars. It provides the likelihood of simultaneous occurrences of these two events.

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
- Just as with single random variables,
you can find the marginal PDFs for X and Y from the joint PDF.

- The marginal PDF for $X$ , denoted as $f_X(x)$ , is obtained by integrating 
the joint PDF $f_{XY}(x,y)$ with respect to $Y$ over the entire range of $Y$ values.

- Similarly , the marginal PDF for $Y$ , denoted as $f_Y(y)$ , is obtained by integrating 
the joint PDF $f_{XY}(x,y)$ with respect to $X$ over the entire range of $X$ values.

Suppose $(X,Y)$ have joint density $f_{XY}(x,y).$ Then,

- $X$ has the marginal density $f_X(x)$ = $\int^{\infty}_{y = - \infty} f_{XY}(x,y)dy$
- $Y$ has the marginal density $f_Y(y)$ = $\int^{\infty}_{x = - \infty} f_{XY}(x,y)dy$

<!-- $D = \{(x, y): [0, 2]\times [0, -2] \cup [-1, 0]\times [0, 1]\}$ -->

!!! example 
     From the joint PDF $f_{XY}(x,y)$ , you can find the marginal PDF for $X$ ($f_X(x)$) and 
    $Y$ ($f_Y(y)$) separately. $f_X(x)$ would represent the distribution of arrival times , and 
    $f_Y(y)$ would represent the distribution of spending amounts 

## Independence of Random Variables 
Independence means that the behavior of one random variable does not influence the behavior of the other.

$(X,Y)$ with joint density $f_{XY}(x,y)$ are independent if 

$$ f_{XY}(x,y) = f_X(x)f_Y(y) $$

where $f_X(x)$ and $f_Y(y)$ are marginal densities of $X$ and $Y$ respectively.

!!! example 
    Suppose $X$ represents the temperature in one city, 
    and $Y$ represents the temperature in another city.
    If these cities are far apart and have independent weather patterns,
    then $X$ and $Y$ may be considered independent. 

## Conditional Density 
Conditional Density describe the probability of one random variable given the other.

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

!!! example 
    Continuing with the temperature example, you might want to find
    $f_{X|Y}(x|y)$, which would represent the PDF of temperature in one city 
    given a specific temperature in the other city.
    This could help predict temperature changes in one city based 
    on the observed temperature in the other city.
