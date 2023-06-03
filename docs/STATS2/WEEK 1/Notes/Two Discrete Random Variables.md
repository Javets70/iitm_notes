# Two Discrete Random Variables 

## Takeaways from this Week 
- You should be able to understand how the joint distribution tables work.
- Marginal PMF and Conditional Distribution are the most important concept in this week and will be used in the future.

## Joint PMF
Suppose $X$ and $Y$ are discrete random variables defined in the same probability space.
Let the range of $X$ and $Y$ be $T_X$ and $T_Y$ , respectively .
The joint PMF of $X$ and $Y$ , denoted by $f_{XY}$ , is a function from $T_X \times T_Y$ to **[0,1]** defined as

$$f_{XY} = P(X = t_1 \ and \ Y=t_2) , t_1 \in T_X , t_2 \in T_Y$$

It is usually written in a table or a matrix.

!!! example
    Let $X_i = 1$ if $i^{th}$ toss is heads and $X_i = 0$ if toss is tales.

    | $t_2$ \ $t_1$ | 0   | 1   |
    | ------------- | --- | --- |
    | 0             | 1/4    | 1/4 |
    | 1             | 1/4    | 1/4 |

    Then , $f_{XY}(0,0) = P(X_1=0,X_2=0) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$  

    !!! info 
        The sum of all the Joint PMFs will always be 1


---

## Marginal PMF (Probability Mass Function)

Suppose $X$ and $Y$ are jointly distributed discrete random variables with joint PMF $f_{XY}$.
The PMF of the individual random variables $X$ and $Y$ are called as marginal PMFs. It can be shown that

$$f_X(t)=P(X=t)=\sum_{t'\in T_Y} f_{XY}(t,t')$$

$$f_Y(t)=P(Y=t)=\sum_{t'\in T_X} f_{XY}(t,t')$$

where $T_X$ and $T_Y$ are the ranges of $X$ and $Y$ , respectively.


!!! example
    | $t_2$ \ $t_1$ | 0 | 1 | $f_{x_{2}}(t_2)$ |
    | ---------------- | --- | --- | ---------------- |
    | 0 | 1/4 | 1/4 | 1/2 |
    | 1 | 1/4 | 1/4 | 1/2 |
    | $f_{x_{1}}(t_1)$ | 1/2 | 1/2 ||

    - Adding along the rows and adding along the columns gives us the Marginal PMF.
    - In our case the marignal PMF of $X_1$ will be

        - $f_{X_1}(0) = f_{X_{1}X_2}(0,0) + f_{X_{1}X_2}(0,1) = \frac{1}{4} + \frac{1}{4}$
        - $f_{X_1}(1) = f_{X_{1}X_2}(1,0) + f_{X_{1}X_2}(1,1) = \frac{1}{4} + \frac{1}{4}$

---

## Conditional distribution of one random variable given another
Suppose $X$ and $Y$ are jointly distributed discrete random variables with joint PMF $f_{XY}$. The conditional PMF of $Y$ given $X=t$ is defined as the PMF:

$$Q(t')=P(Y=t'|X=t)=\frac{P(Y=t' , X=t)}{P(X=t)} = \frac{f_{XY}}{f_{X}(t)}$$

!!! example
    | $t_2$ \\ $t_1$ | 0 | 1 | 2 | $f_Y(t_2)$ |
    | -------------- | --- | --- | --- | ---------- |
    | **0** | 1/4 | 1/8 | 1/8 | 1/2 |
    | **1** | 1/8 | 1/8 | 1/4 | 1/2 |
    | $f_X(t_1)$ | 3/8 | 1/4 | 3/8 | |

    Where , $X \in \{0,1,2\}$ , $Y \in \{0,1\}$ and $(Y|X=0) \in \{0,1\}$

    - $f_{Y|X = 0}(0) = \frac{f_{XY}(0,0)}{f_X(0)} = \frac{1/4}{3/8} = \frac{2}{3}$
    - $f_{Y|X = 0}(1) = \frac{f_{XY}(0,1)}{f_X(0)} = \frac{1/8}{3/8} = \frac{1}{3}$

---

## Factoring
This is just a formula , mug it up 💀.

$$\begin{align*}
f_{X_1X_2X_3X_4}(t_1,t_2,t_3,t_4) = P(X_4 = t_4 , X_3 = t_3 , X_2 = t_2 , X_1 = t_1)
\\
\implies f_{X_4 \mid X_3 = t_3 , X_2 = t_2 , X_1=t_1}(t_4) \times f_{X_3 \mid X_2 = t_2 , X_1=t_1}(t_3) \times f_{X_2 \mid X_1=t_1}(t_1) \times f_{X_1}(t_1)
\end{align*}$$

