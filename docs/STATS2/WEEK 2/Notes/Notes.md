## Takeaways from this week
- Being able to check whether a given join distribution has indepenedent random variables or not.
- Memoryless Property 


# Independence of Random Variables 
Independent random variables are variables that have no influence or relationship with each other. 
In other words, the occurrence or value of one random variable does not affect the occurrence 
or value of the other random variable.

Formally, two random variables $X$ and $Y$ are considered independent if the probability distribution of one variable is not affected by the other variable.

Let $X$ and $Y$ be two random variables defined in a probability space with ranges $T_X$ and $T_Y$ respectively.
$X$ and $Y$ are considered independent if :

$$f_{XY}(t_1 , t_2) = f_X(t_1) \times f_{Y|X=t_1}(t2)$$

where,

$$f_{Y|X=t_1}(t2) = f_Y(t_2)$$

$$\therefore f_{XY}(t_1 , t_2) = f_X(t_1) \times f_Y(t_2)$$

!!! info "Properties of Independent Variables"
    - Joint PMF is the product of the marginal PMFs when the variables are independent.
    - All the subsets of independent random variables are independent.


## Checking Independence of Random Variables 
For every element in the table of 2 or more random variables.
Each entry must be the product of their respective marginal PMFs then only they are considered **independent.** 

If for any element $f_{XY}(t_1 , t_2) \neq f_X(t_1)f_Y(t_2)$ then the variables are considered **dependent.**

!!! tip "Tips To Identify Independent Random Variables"
    - i.i.ds (independent and identically distributed) are one of the examples for independent random variables for any $f_{XY}(t_1 , t_2) \neq 0$
    - Finding dependent variables is easier when $f_{XY}(t_1)(t_2) =0$.
    The logic behind it is for some $t_1$ and $t_2$ $f_X(t_1) \times f_Y(t_2) \neq 0$ , if it is 0 then it would mean that either or both of the marginals are 0 which is generally not true.

---

## Geometric iid 
### Question 1
Let $X_1 , X_2 , X_3 ... , X_n$ be an iid with a Geometric(p) distribution. What is the probability that all of these random variables are larger than some positive integer $j$.

$$X \sim \{1,2,3,....\}$$

$$P(X=k) = (1-p)^{k-1}p$$

The probability that the random variables are greater than $j$ is :

$$(P(X > j))^n = (1-p)^{jn}$$


### Question 2
Let $X \sim \{\stackrel{\frac{1}{2}}{0},\stackrel{\frac{1}{4}}{1} , \stackrel{\frac{1}{8}}{2} , \stackrel{\frac{1}{16}}{3} , \stackrel{\frac{1}{16}}{4}\}$ , and let $X_1 ..... X_n$ be the iid samples with distribution $X$.

#### What is the probability that 4 is missing in some samples.
- $P(X_1 \neq 4 , X_2 \neq 4 , X_3 \neq 4 , X_4 \neq 4 .... X_n \neq 4)$
- $(P(X \neq 4))^n$ as all the probabilities are same for an iid.
- $(P(X \neq 4))^n = (1 - P(X = 4))^n$
- $(P(X \neq 4))^n = (1 - \frac{1}{16})^n = (\frac{15}{16})^n$

#### What is the probability that 4 appears exactly once. 
$\implies P( \text{4 Appears exactly once})=$

$$\begin{align} \implies P(X_1 = 4 , X_2 \neq 4 , X_3 \neq 4 .... X_n \neq 4) + \\ 
P(X_1 \neq 4 , X_2 = 4 , X_3 \neq 4 ... X_n \neq 4) + ... \\
P(X_1 \neq 4 , X_2 \neq 4 , X_3 \neq 4 .... X_{n-1} \neq 4 , X_n =4) \end{align}$$

$\implies n \times P(X \neq 4)^{n-1} \times P(X=4)$
$\implies n \times (\frac{15}{16})^{n-1} \times (\frac{1}{16})$

---

## Memoryless Property of Geometric Distribution
The memoryless property of geometric random variables states that the past history or 
previous outcomes of the trials do not affect the future outcomes. 
In other words, the probability of success in the next trial remains the same, 
regardless of how many trials have already occurred.

(Just mug up the formula for this one if you dont understand this 💀🥲)

$$P(X \geq s+t | X \geq t  ) = P(X \geq s)$$

<!-- For a detailed proof see the lecture. -->
### Proof 
The PMF of a random variable $X$ is 

$$\begin{align}
f(x) &= p(1-p)^x & x &= 0,1,2,..
\end{align}$$

The probability that $X$ is greater than or equal to $x$ is


$$\begin{align}
P(X \geq x) &= (1-p)^x & x = 0,1,2,...
\end{align}$$

The conditional probability will be

$$\begin{align}
P(X \geq s +t | X \geq t) &= \frac{P(X \geq s + t , X \geq t)}{P(X \geq t)} \\
&= \frac{P(X \geq s+t)}{P(X \geq t)} \\
&=  \frac{(1-p)^{s+t}}{(1-p)^t} \\
&= (1-p)^s \\
&= P(X \geq s)
\end{align}$$

---

