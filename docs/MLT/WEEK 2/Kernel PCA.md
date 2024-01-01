# Kernel PCA

## Issues with PCA
In the previous week we learned about using PCA to reduce 
the number of features required to represent the dataset 
without much loss.

There are 2 main issues/concerns with PCA

- **Time Complexity** : Finding the eigenvector and eigenvalues of 
matrix $C \in \mathbb{R}^(d \times d)$ typically takes $O(d^3)$ time.
This becomes an issue when the number of features is much higher than number
of points.

- **PCA works only linearly** : For a dataset with 3 features , if the 
features are not related linearly then using PCA does not give good 
results.

## Time Complexity Issue with PCA
The time complexity issue occurs when the number of features is 
much much greater than the number of points in the dataset , i.e. 
$d >> n$.

According to our algorithm the solution for maximizing the variance 
of the dataset was to find the eigenvector corresponding to the max 
eigenvalue of $C$ , where $C = \frac{1}{n}\sum_{i=1}^{n}x_ix_i^T$

if $X \in \mathbb{R}^{d \times n}$ is the matrix which represents 
all the points in the dataset , $C$ can also be written as $C = \frac{1}{n}XX^T$

> This was just recalling and putting in the context to what is 
about to happen now 

Let $w_k$ be the eigenvector corresponding to the $k^{th}$ largest eigenvalue 
of $C$ ($\lambda_k$).

$$\begin{equation*} 
\begin{split}
C w_k &= \lambda_k w_k \\
\left(\frac{1}{n} \sum_{i=1}^{n} x_ix_i^T \right) w_k &= \lambda_k w_k \\
w_k &= \frac{1}{n \lambda_k} \sum_{i=1}^{n} (x_i^Tw_k)x_i \\
w_k &= \sum_{i=1}^{n} \left( \frac{x_i^Tw_k }{n \lambda_k} \right)x_i \\
\end{split}
\end{equation*} \tag{1} \label{Wk1}$$

From this equation we can obeserve that **$\mathbf{w_k}$ is a linear combination of datapoints**,
assuming $\lambda_k \neq 0$.

$$\implies w_k = X\alpha_k \tag{2} \label{Wk2}$$ 

for some $\alpha_k \in \mathbb{R}^n$

> To find the value $w_k$ from the above equation , we need to know the value of $\alpha_k$

> But if we compare $\eqref{Wk1}$ and $\eqref{Wk2}$ we can see that , 
$\alpha_k = \sum_{i=1}^{n} \left( \frac{x_i^Tw_k }{n \lambda_k} \right)$

> From the above equation , if we want to find $\alpha_k$ we need to know the 
value $w_k$ itself. This is a chicken and egg problem,to solve this problem
we will take a look at another equation.

We know,

$$\begin{equation*}
\begin{split}
w_k &= X \alpha_k \;\;\;\;\;\;\;\;\; \forall k \\
\\
Cw_k &= \lambda_k w_k \\
\left( \frac{1}{n} XX^T \right)(X \alpha_k) &= \lambda_k X \alpha_k \\
\\
\text{Premultiplying by} X^T \\
\\
X^T((XX^T) X \alpha_k) &= X^T(n \lambda_k X \alpha_k) \\
(X^TX)(X^TX)\alpha_k &= n \lambda_k (X^TX) \alpha_k \\
\\
\text{Let} X^TX = K \\ 
\\
K^2 \alpha_k &= n \lambda_k K \alpha_k \\ 
\boxed{K \alpha_k = (n \lambda_k) \alpha_k} \\
\end{split}
\end{equation*}$$

> It is observed that for any $\alpha_k$ lets say $u$ which satisfies 
this equation , there exists a scaled version of $u$ (Example $4u$) which 
also satisfies this equation.

> To prevent the possibilities of scaled values of $\alpha_k$ , we will 
narrow down the possible values using the idea that length of $w_k$ is 1 i.e.
$||w_k|| = 1$.


We know,

$$\begin{equation*}
\begin{split}
w_k &= X \alpha_k \\ 
w_k^Tw_k &= (X\alpha_k)^T(X\alpha_k) = \alpha_k^T (X^TX) \alpha_k \\
&\boxed{1 = \alpha_k^T K \alpha_k} \\
\end{split}
\end{equation*}$$

Now we have 2 equations , which $\alpha_k$ must satisfy.

> Up until now , we wanted the eigenvectors of $XX^T$ which is $d \times d$ 
matrix , but now we are saying we can solve the eigenequation of $K$ , where
$K = X^TX$ which is a $n \times n$ matrix.

> But now the issue is , to get the value of $K$ in the 
equation 

> $$K \alpha_k = (n \lambda_k) \alpha_k$$

> the value of $\lambda_k$ is required  , which we can only get when we 
solve for $XX^T$ matrix. Back to square one 😭.

Now to find $\lambda_k$ we will find a relation between eigenvalues of 
$XX^T$ and $X^TX$.

!!! success ""
    **Linear Algebra Fact** :The non zero eigenvalues of $XX^T$ and $X^TX$ are exactly the same.


$$\begin{equation*}
\begin{split}
\text{For } C, \\
C &= \frac{1}{n} XX^T \hspace{1cm} & \text{Eigenvectors} = \{w_1 , w_2 .... , w_n \} \hspace{1cm} & \forall k , ||w_k||^2 = 1 \\ 
&& \text{Eigenvalues} = \{ \lambda_1 \geq \lambda_2 \geq .... \geq \lambda_n \}  \\ 
\\
\\
\text{For  } XX^T,
\\
XX^T &= n \times C & \text{Eigenvectors} = \{ w_1 , w_2 .... , w_l \}  \\
&& \text{Eigenvalues} = \{ n\lambda_1 \geq n\lambda_2 \geq .... \geq n\lambda_l \}  \\ 
\\
\\
\text{For } X^TX \\
&X^TX & \text{Eigenvectors} = \{\beta_1 , \beta_2 , ..... \beta_l  \} \hspace{1cm} &  \forall k, ||\beta_k||^2 = 1 \\
&& \text{Eigenvalues} = \{ n\lambda_1 \geq n\lambda_2 \geq .... \geq n\lambda_l \}  \\ 
\end{split}
\end{equation*}$$

> Note that the eigenvalues of $XX^T$ are the same $X^TX$ from the 
linear algebra fact.

This gives us the final result as,

$$\boxed{K \beta_k = (n \lambda_k)\beta_k}$$ 

> Now we need to check if $\beta_k = \alpha_k$?

$$\begin{equation*}
\beta_k^T K \beta_k = \beta_k^T(n \lambda_k \beta_k) = n \lambda_k \beta_k^T\beta_k = \boxed{n \lambda_k}
\end{equation*}$$

Therefore,

$$\alpha_k = \frac{\beta_k}{\sqrt{n\lambda_k}} , \;\;\;\; \forall k $$

The gist of this solution is that , when  $d >> n$  we use the eigenvectors of 
$X^TX \in \mathbb{R}^{n \times n}$ instead of $XX^T \in \mathbb{R}^{d \times d}$
which reduces the computation time required to get the eigenvectors.


!!! success "New Algorithm when $d >> n$"
    1. Compute $K = X^TX$ , where  $K \in \mathbb{R}^{n \times n}$
    2. Compute the eigendecomposition of $K$ to get the eigenvectors and the 
    eigenvalues.
    3. Calculate for $\alpha_k$ , $\alpha_k = \frac{\beta_k}{\sqrt{n \lambda_k}} \;\;\;\;\; \forall k$
    4. $\boxed{w_k = X\alpha_k} \;\;\;\;\;\; \forall k$

## Non-Linear Relationship of Datapoints 
The issue of non-linear relationship arises when the datapoints 
are related to each other in a "non-linear" way , it might be quadratic , cubic or 
even biquadratic.

![](./img/MultipleBestFitLines.svg)

Now if the points of the dataset lie in a circle , determining the "best fit line"
is pointless , almost all of the lines will be the best fit lines for this circle with
a marginal difference of "reconstruction error" between them.

The relation features of in this dataset can be represented using equation of a circle,

$$(f_1 - a)^2 + (f_2 - b)^2 = r^2$$

> We can see that this equation has quadratic terms which cannot be 
represented linearly. To solve this problem , we will map it to function
with more features in order to represent it linearly.

$$\begin{equation*}
\begin{split}
\underset{\mathbb{R}^2}{[f_1 , f_2]} \xrightarrow{\phi} \overset{\phi(x)}{\underset{\mathbb{R}^6}{[1 , f_1^2 , f_2^2 , f_1 f_2 , f_1 , f_2]}} \\ 
\\
\text{Let } u \in \mathbb{R}^6  \hspace{1cm} [a^2 + b^2 - r^2 , 1 , 1, 0 , -2a , -2b] \\
\end{split}
\end{equation*}$$

The function to map $[f_1 , f_2]$ to $\mathbb{R}^6$ is called $\phi$ and $u$
is a point such that each datapoint of the original circular dataset satisfies,

$$\boxed{\phi(x)^Tw = 0}$$

The equation above shows that the datapoints after mapping to $\mathbb{R}^6$
lie in a linear subspace.

!!! note 
    Mapping $d$ features to a polynomial of power $p$ results in $^{d+p} C_d$ new features.

    In the above equation of circle , it can be see in that mapping 2 features ($d$) 
    to a polynomial of degree 2 ($p$), results in ($^{2+2} C_2$) 6 features.

!!! question "How does this solve our problem of non linear datapoints?"
    For a dataset $S$ , whose datapoints have a non-linear relationship ($x_i \in \mathbb{R}^d$),
    we can map this dataset to a higher dimension (linear subspace), 
    such that after mapping , $x_i \in \mathbb{R}^D$.

    **Note** that $D > d$

    As the points (after mapping to higher dimension) are in a linear subspace , our PCA algorithm 
    will work much better than before.

    Also note that , we already have a solution for the case when dimension of the datapoints is much 
    much larger than the number of datapoints ($d >> n$). 

## Kernel Functions 

!!! failure "Issues with Calculating $\phi(x)$"
    - To run PCA on non-linear features , we came up with the solution of mapping ($\phi(x)$) the 
    features to a higher dimension and then instead of calculating eigenvectors for a $d \times d$ 
    (Covariance) matrix , we calculated eigenvectors for $n \times n$ ($X^TX$) if $d >> n$.
    - The issue with current implementation of PCA is that calculating $\phi(x)$ is nearly 
    the same number of calculations as $O(d^p)$. 
        - This means that as the power of the polynomial increases , the calculation of individual 
        features in the mapping $\phi(x)$ rises exponentially.
        - **Example**: If 2 features are mapped to a 20 power polynomial , the resulting number of 
        features will be nearly $2^{20}$ , which is simply too many calculations.
    - To solve this problem we will now take a look at Kernel Functions.

The eigendirections we compute (when mapping datapoints to a higher dimension) in PCA is of $\phi(x)^T \phi(x)$.

![](./img/KernelFunctions.svg)

> To get to $K_{ij}$ we first need to calculate $\phi(x_i)^T \phi(x_j)$ , but is there a way to directly go from 
$x_i \quad x_j$ to $K_{ij}$ without computing $\phi(x)$ ?

The function $(x^T x^{'} + 1)^2$ is one such function through which we can directly get to  $\phi(x)^T \phi(x^{'})$, 
without having to compute $\phi(x)$ and $\phi(x^{'})$.

Lets say, $x = [f_1 , f_2] \quad x^{'} = [g_1 , g_2]$

$$\begin{equation*}
\begin{split}
(x^T x^{'} + 1)^2 &= \left( \begin{bmatrix}f_1 & f_2 \end{bmatrix} \begin{bmatrix} g_1 \\ g_2 \end{bmatrix} + 1 \right)^2 \\
&= (f_1 g_1 + f_2 g_2 + 1)^2 \\ 
&= f_1^2 g_1^2 + f_2^2 g_2^2 + 1 + 2f_1 g_1 f_2 g_2 + 2f_1 g_1 + 2f_2 g_2 \\
\end{split}
\end{equation*}$$

This can also be written as ,

$$\begin{equation*}
\begin{split}
(x^T x^{'} + 1)^2 &= \begin{bmatrix}f_1^2 & f_2^2 & 1 & \sqrt{2}f_1 f_2 & \sqrt{2}f_1 & \sqrt{2}f_2 \end{bmatrix} 
\begin{bmatrix}g_1^2 \\ g_2^2 \\ 1 \\ \sqrt{2}g_1 g_2 \\ \sqrt{2}g_1 \\ \sqrt{2}g_2 \end{bmatrix} \\
&= \phi(x)^T \phi(x^{'}) \\
\\
\text{where,}\\
\\
\phi(x) &= \phi \left( \begin{bmatrix} a \\ b \end{bmatrix}\right) = \begin{bmatrix}a^2 \\ b^2 \\ 1 \\ \sqrt{2}a b \\ \sqrt{2}a \\ \sqrt{2}b \end{bmatrix} \\\end{split}
\end{equation*}$$

We can see that , to calculate $\phi(x)^T \phi(x^{'})$ we can instead solve for $(x^T x^{'} + 1)^2$ and 
skip the step for calculating $\phi(x)$ and $\phi(x^{'})$.

### Valid Kernel Functions
There are 2 ways to check if a function is a valid kernel function,

1. There exists a mapping from $\mathbb{R}^d$ to $\mathbb{R}$ such that $k(x , x^{'}) = \phi(x)^T \phi(x^{'})$.
2. A kernel function is considered valid if ,
    - $k$ is symmetric , i.e. , $k(x , x^{'}) = k(x^{'} , x)$
    - The kernel matrix $K$ , where $K_{ij} = k(x_i , x_j)$ , is positive semi-definite.

!!! note "Common Kernel Functions"
    1. **Polynomial Kernel**: $k(x , x^{'}) = (x^Tx^{'} + 1)^p$
    2. **Gaussian Kernel**: $k(x , x^{'}) = \exp \left( - \frac{|| x - x^{'}||^2}{2 \sigma^2} \right)$ , for some $\sigma > 0$.
        - $\phi(x)$ in this case is mapped to infinite dimension.

## Kenrel PCA
Now we need everything that is required to perform Kernel PCA on a non-linear dataset , lets put down an 
algorithm for Kernel PCA.

- Input $\{x_1 , x_2 , \cdots , x_n \}$ $x_i \in \mathbb{R}^d$ , kernel $k : \mathbb{R}^d \times \mathbb{R}^d \to \mathbb{R}$
- Compute $K \in \mathbb{R}^{n \times n}$ where $K_{ij} = k(x_i,x_j) \quad \forall i,j$
- Center the kernel using,

$$K^C = K - IK - KI + IKI$$

where $K^C$ is the centered kernel and $I \in \mathbb{R}^{n \times n}$ is a matrix with all elements equal to $\frac{1}{n}$

- Compute $\beta_1 , \beta_2 , \cdots , \beta_l$ eigenvectors and $n\lambda_1 , n\lambda_2 , \cdots , n\lambda_l$ eigenvectors of K
and normalize to get $\alpha_k = \frac{\beta_k}{\sqrt{n \lambda_k}}$
- Compute the compressed representation using,

$$\begin{equation*}
\begin{split}
\phi(x_i)^T w_k &= \phi(x_j)^T \left( \sum_{j=1}^n \phi(x_i) \alpha_{kj} \right) \\
&= \sum_{j=1}^n \alpha_{kj} \phi(x_i)^T \phi(x_j) \\
&= \sum_{j=1}^n \alpha_{kj} K_{ij} \\
\end{split}
\end{equation*}$$

- Compute $\sum_{j=1}^n \alpha_{kj} K_{ij} \quad \forall k$

$$\phi(\mathbf{x}_i)^T\mathbf{w} \in \mathbb{R}^{d} \to
\left [
\begin{array}{cccc}
\displaystyle \sum_{j=1}^{n} \alpha_{1j} \mathbf{K}^C_{ij} & \displaystyle \sum_{j=1}^{n} \alpha_{2j} \mathbf{K}^C_{ij} & \ldots & \displaystyle \sum_{j=1}^{n} \alpha_{nj} \mathbf{K}^C_{ij}
\end{array}
\right ]$$
