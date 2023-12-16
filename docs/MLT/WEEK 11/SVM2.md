## Dual Formation for Soft Margin SVM
We know that SVM works well on a linearly separable dataset, but our
goal was to accommodate outliers/noise in the dataset and hence we
created a new formulation from SVM called "Soft Margin SVM" , given
by the formula,

$$\begin{split} 
\underset{w \in \mathbb{R}^d}{\min} \frac{1}{2}||w||^2 + C \sum_{i=1}^n \xi_i  \\
\text{such that } (w^T x_i)y_i + \xi_i \geq 1 \;\; \forall i \\
\xi_i \geq 0 \;\; \forall i \\
\end{split}$$

We want to kernalize this equation so that it is able to 
perform even on "non-linear" datasets.

!!! example 
    ![](./img/QuadraticStructure.svg)

    This example depicts how we want our "Kernalized Soft Margin SVM" to be.

    - It should be able to work on a non-linearly separable dataset.
    - It should also be able to identify "non-linear" structures within 
    the dataset.

The first step towards our goal would be to form a "Dual Problem" for the 
"Soft Margin SVM" equation.

To formulate the "Dual Problem" we will first make a langrangian function,

$$ \mathcal{L}(w, \xi , \alpha , \beta) = 
\frac{1}{2}||w||^2 + C \sum_{i=1}^{n}\xi_i + \sum_{i=1}^n \alpha_i(1 - w^T x_i y_i - \xi_i) 
+ \sum_{i=1}^n \beta_i (- \xi_i)$$

!!! note
    - $\alpha$ corresponds to the first constraint ($(w^T x_i)y_i + \xi_i \geq 1$).
    - $\beta$ corresponds to the second constraint ($\xi_i \geq 0$).
    - The constraints are written in standard form , in the above equations.

Therefore , the "Dual Problem" will be,

$$ \underset{w , \xi}{\min} \left[ 
\underset{\substack{\alpha \geq 0 \\ \beta \geq 0}}{\max} \frac{1}{2} 
||w||^2 + C \sum_{i=1}^n \xi_i + \sum_{i=1}^n \alpha_i (1 - (w^T x_i)y_i - \xi_i)) + \sum_{i=1}^n \beta_i (- \xi_i)
\right] $$

For a fixed value $\alpha$ and $\beta$,

The derivative of "Dual Problem" with respect to $w$ will be,

$$ w^*_{\alpha , \beta} = \sum_{i=1}^n \alpha_i x_i yi \label{w-star} \tag{1} $$

The derivative of "Dual Problem" with respect to $\xi$ will be,

$$\begin{equation*}
\tag{2}
\begin{split}
C + \alpha_i(-1) + \beta_i(-1) &= 0 \\
\alpha_i + \beta_i &= C \\
\end{split}
\end{equation*}$$

From Equation **1** and Equation **2** , Our new dual problem will be,

$$\boxed{\underset{\substack{\alpha \geq 0 \\ \beta \geq 0 \\ \alpha + \beta = C}}{\max} 
\alpha^T I - \alpha^T Y^T X^TX Y \alpha}$$

**Note** that this is same as the dual problem we had in "SVM/Hard SVM".

$\alpha \geq 0$ and $\alpha + \beta = C$ , which means $\beta$ is restricting 
the range of $\alpha$, in other words , $\alpha$ can be at most $C$.

We can equivalently say that,

$$\boxed{\underset{0 \leq \alpha \leq C}{\max} 
\alpha^T I - \alpha^T Y^T X^TX Y \alpha}$$

### Cases of Different Value of $C$
#### When $C = 0$
If $C = 0$ , this means that $\alpha = 0$ , also from Equation $\eqref{w-star}$,
$w^*_{\alpha , \beta} = 0$.

#### When $C = \infty$
If $C = \infty$ , that means there is no upper bound on $\alpha$ and 
the above "Dual Problem" becomes exactly the same as Hard-Margin SVM.

## Complementary Slackness Conditions for Soft-Margin SVM
- Let ($w^* , \xi^*$) be the "Primal" optimal solutions.
- Let ($\alpha^* , \beta^*$) be the "Dual" optimal solutions.

### Complementary Slackness Conditions 
At optimality , 

$$\forall i \quad \alpha_i^* (1 - (w^{*^T} x_i)y_i - \xi_i^*) = 0 \label{CS1} \tag{1}$$

$$\forall i \quad \beta_i^* (- \xi_i^*) = 0 \label{CS2} \tag{2}$$

#### Cases for Complementary Slackness 
!!! abstract "When $\alpha_i^* = 0$"
    - $\implies \beta_i^* = C$ as $\alpha_i^* + \beta_i^* = C$.
    - $\implies \xi_i^* = 0$ as $\beta_i^* = C$ (From $\eqref{CS2}$)
    - We know that , $w^{*^T} x_i y_i + \xi_i^* \geq 1$
        - $\implies w^{*^T} x_i y_i \geq 1$ as $\xi_i = 0$
        - $w^*$ classifies $(x_i ,y_i)$ correctly.
        ![](./img/CS_Case1.svg)

!!! abstract "When $\alpha*_i \in (0,C)$"
    - $\implies \beta_i^* \in (0,C)$
    - $\implies \xi_i^* = 0$ (From $\eqref{CS2}$)
    - $\implies 1 - (w^{*^T}x_i)y_i - \xi_i = 0$ (From $\eqref{CS1}$)
        - $\implies 1 - (w^{*^T}x_i)y_i  = 0$ as $\xi_i^* = 0$
        - $\implies  (w^{*^T}x_i)y_i  = 1$
        ![](./img/CS_Case2.svg)

!!! abstract "When $\alpha^*_i = C$"
    - $\implies \beta_i^* = 0$ as $\alpha_i^* + \beta_i^* = C$
        - $\xi_i^* \geq 0$ as $\beta_i^* = 0$

    - $1 - (w^{*^T}x_i)y_i + \xi_i = 0$ (From $\eqref{CS1}$)
        - $\implies \xi_i^* = 1 - (w^{*^T}x_i)y_i$
        - $\implies 0 \leq 1 - (w^{*^T}x_i)y_i$ as $\xi_i^* \geq 0$
        - $\implies (w^{*^T}x_i)y_i \leq 1$
            ![](./img/CS_Case3.svg)
        - $w^*$ will either classify the points incorrectly or
        - $w^*$ will correctly classify the points but not with enough margin.

