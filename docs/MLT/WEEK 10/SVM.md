# Support Vector Machine
## Perceptrons and Margin
We know that in the Perceptron Algorithm the number of mistakes is given by,
$\text{#mistakes} \leq \frac{R^2}{\gamma^2}$ , we also said that data is linearly 
separable with margin $\gamma$ , which means that there exists some $w^*$ such that 
$w^{*^T} x_i \geq \gamma \forall i , \gamma>0$ 

![](./img/QualityFinalSolution.svg)

??? question 
    If we were given a dataset like in the above image , which of the 2 $w^*$ would be 
    a better choice?

- We can see that $w_1^*$ has a greater margin $\gamma_1$ when compared to $w_2^*$ which 
has a smaller margin $\gamma_2$.

- If we want to decrease the number if mistakes our algorithm makes, we can increase 
the value of $\gamma$ because $\text{#mistakes} \leq \frac{R^2}{\gamma^2}$ , in other
words number of mistakes is inversely proportional to $\gamma^2$.**The greater the $\gamma$
the lower will be the number of mistakes.**

- Therefore , the better of the 2 $w^*$ here is $w_1^*$.

## Maximum Margin: Formulation
Now that we know that $w^*$ which have larger $\gamma$ margin are better than other
$w^*$ , our goal now is to come up with a formulation that maximizes $\gamma$ margin.

$$\underset{w,\gamma}{\max} \quad \gamma \quad
\text{such that } (w^T x_i)y_i \geq \gamma \;\; \forall i$$

> We want to maximize $\gamma$ over $w$ , but we arent choosing any random $w$ ,
the $w$ should satisfy the condition of $(w^Tx x_i)y_i \geq \gamma$.

!!! failure "Problem With Above Formulation"
    Lets say for some $w$ the $\gamma$ margin is , $\{ x:w^T x = 5 \}$ , it can 
    be argued that there exists another $w$ such that $(2 w)^T x = 2 \times 5 = 10$.
    So for this $w$ , there exist infinitely many "scaled versions".

To solve the above stated problem , we will "ground" the value of $w$ such that 
$||w||^2 = 1$. Therefore our new formulation will be,

$$\begin{split}
\underset{w , \gamma}{\max} \gamma \\ 
\\
\text{such that } \\
(w^T x_i)y_i \geq \gamma \quad \forall i \\
\text{and } ||w||^2 = 1
\end{split}$$

### Simplified Formulation
The above maximization can be reformulated into an expression with just 
one variable ($w$). 

$$\begin{split}
\underset{w}{\max} \;\; \text{width}(w) \\
\\
\text{such that} \\
(w^T x_i)y_i \geq 1 \quad \forall i \\
\end{split}$$

> This equation basically means that , we are allowing any $w$ which linearly 
separates our dataset with $\gamma$ margin exactly equals 1 and instead of 
maximizing $\gamma$ we are maximizing is the width. The width here is 
the distance between to parallel lines of $\gamma$ margins.

!!! question "What is width(w)?"
    For some $w$ which classifies a dataset , $x_1$ and $x_2$ be the points lying on 
    the $\gamma$ margins. The distance between these points (width(w)) can be given by,

    $$\begin{equation*}
    \begin{split}
    x_1 ^T w - x_2 ^T w &= 2 \\
    (x_1 - x_2)^T w &= 2 \\ 
    ||x_1 - x_2||_2 \; ||w||_2 \; \cos(\theta) &= 2 \quad \quad (\theta =  0°) \\ 
    \therefore || x_1 - x_2 ||_2 &= \frac{2}{||w||_2}
    \end{split}
    \end{equation*}$$

    ![](./img/WidthW.svg)

Now that we know what width(w) is , we can reformulate our maximization equation as ,

$$\begin{split}
\underset{w}{\max} \;\; \frac{2}{||w||^2} \\
\\
\text{such that} \\
(w^T x_i)y_i \geq 1 \quad \forall i \\
\end{split}$$

Equivalently , the above experession can be turned into a minimization equation,

$$\begin{split}
\boxed{\underset{w}{\min} \;\; \frac{1}{2} ||w||^2} \\
\\
\text{such that} \\
(w^T x_i)y_i \geq 1 \quad \forall i \\
\end{split}$$
