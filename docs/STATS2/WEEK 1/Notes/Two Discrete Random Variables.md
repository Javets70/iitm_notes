# Discrete Random Variables 
Discrete random variables are variables that can take on a countable number of distinct values. 
These values are typically integers or whole numbers and are often the result of counting or enumerating something. 

!!! example 
    - **Coin Toss** : Consider a random variable $X$ which represents the number of heads
    when a coin is tossed $2$ times. We can see that $X$ can only take the values $0 , 1 , 2$.
    Here $X$ is a discrete random variable.
    - **Russian Roulette** : Consider a random variable $Y$. $Y = 0$ when a bullet is not fired and $Y=1$ when 
    a bullet is fired. $Y$ takes the values of $0,1$.
    Here $Y$ is a discrete random variable.
    - **Dice Roll** : Consider a random variable $Z$. $Z$ can only take values $0,1,2,3,4,5,6$ and each of these 
    values has a corresponding probability.
    Here $Z$ is a discrete random variable.


## Takeaways from this Week 
- You should be able to understand how the joint distribution tables work.
- Marginal PMF and Conditional Distribution are the most important concept in this week and will be used in the future.

## Joint PMF
A joint PMF (Probability Mass Function) distribution refers to the probability distribution of two or 
more random variables occurring together. It gives the probabilities for all possible combinations of values of these variables.

Suppose $X$ and $Y$ are discrete random variables defined in the same probability space.
Let the range of $X$ and $Y$ be $T_X$ and $T_Y$ , respectively .
The joint PMF of $X$ and $Y$ , denoted by $f_{XY}$ , is a function from $T_X \times T_Y$ to **[0,1]** defined as

$$f_{XY} = P(X = t_1 \ and \ Y=t_2) , t_1 \in T_X , t_2 \in T_Y$$

It is usually written in a table or a matrix.

!!! example
    **Coin Toss**

    Let $X_i = 1$ if $i^{th}$ toss is heads and $X_i = 0$ if toss is tales.

    | $t_2$ \ $t_1$ | 0   | 1   |
    | ------------- | --- | --- |
    | 0             | 1/4    | 1/4 |
    | 1             | 1/4    | 1/4 |

    Then , $f_{XY}(0,0) = P(X_1=0,X_2=0) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$  

    ---
    **Picking Marbles**

    Consider a bag containing three red marbles (R) and two blue marbles (B). 
    We randomly select two marbles from the bag without replacement and observe their colors.

    Joint PMF Distribution would provide all the possibilites of picking 2 marbles from the bag.

    | Marble 1 | Marble 2 | Probability (P) |
    |----------|----------|-----------------|
    |    R     |    R     |      3/10       |
    |    R     |    B     |      3/10       |
    |    B     |    R     |      3/10       |
    |    B     |    B     |      1/10       |

    Let $X,Y$ represent the color of first and second marbles respectively. Then,

    - $f_{XY}(R,R) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$ (Both marbles are red)
    - $f_{XY}(R,B) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$ ($X$ is red and $Y$ is blue)


    ---

    !!! info 
        The sum of all the Joint PMFs will always be 1


---

## Marginal PMF (Probability Mass Function)
The marginal PMF (Probability Mass Function) refers to the probabilities of a single random variable, 
independently of the other variables in a joint probability distribution.

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
Conditional distribution refers to the probability distribution of one random variable given the knowledge 
or condition of another random variable. It provides the probabilities for the values of one variable, 
taking into account specific conditions or values of another variable.

In simpler terms, it allows us to understand how the distribution of one variable changes 
or is affected when we consider a specific condition or value of another variable.

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
Factoring is used to convert Joint Probabilities into a product of 
Condtional and Marginal Probabilities.

$$\begin{equation*}
\begin{split}
P(Y=t'|X=t)&=\frac{P(Y=t' , X=t)}{P(X=t)} \\
\text{Conditional} &= \frac{\text{Joint}}{\text{Marginal}} \\
\\
\\
P(Y=t' , X=t) &= P(Y=t'|X=t) \times P(X=t)\\
\text{Joint} &= \text{Conditional} \times \text{Marginal}
\end{split}
\end{equation*}$$

For a Joint Probability of 4 variables , 

$$\begin{align*}
f_{X_1X_2X_3X_4}(t_1,t_2,t_3,t_4) = P(X_4 = t_4 , X_3 = t_3 , X_2 = t_2 , X_1 = t_1)
\\
\implies f_{X_4 \mid X_3 = t_3 , X_2 = t_2 , X_1=t_1}(t_4) \times f_{X_3 \mid X_2 = t_2 , X_1=t_1}(t_3) \times f_{X_2 \mid X_1=t_1}(t_2) \times f_{X_1}(t_1)
\end{align*}$$


