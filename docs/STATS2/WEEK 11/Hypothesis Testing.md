Using samples , decide between a null hypothesis denoted $H_0$ and an alternative hypothesis denoted $H_A$ .

### Acceptance Set and Test 
$X_1 , X_2 .... X_n \sim X , H_0 : \text{null hypothesis , }H_A : \text{alternative hypothesis.}$
- Suppose $X \in \symbfscr{X}$. Then the samples $X_1 , X_2 ... X_n \in \symbfscr{X}^n$
- Subset $A \subseteq \symbfscr{X}$ 
If $X_1 , X_2 ... X_n \in A$ we accept $H_0$ otherwise we reject $H_0$

### Size and Power of Test 
**Type I error:**
It is also known as the size of a test , denoted as $\alpha$
- Reject $H_0$ when $H_0$ is true 
- $\alpha = P(\text{Type I error}) = P(\text{Reject }H_0 | H_0 \text{ is true})$ 
**Type II error:**
It is also known as the power of a test , denoted as $1 - \beta$ 
- Accept $H_0$ when $H_A$ is true 
- $\beta = P(\text{Type II Error}) = P(\text{Accept } H_0|H_A \text{ is true})$


## Types of Tests 

```ad-note 
$c$ = critical value
```

### Right Tailed Test 
$H_0 : \mu = \mu_0$
$H_A : \mu > \mu_0$
$T = \overline{X}$
Rejection Region: $\overline{X} > c$
$Z = \frac{\overline{X} - \mu_0}{\sigma / \sqrt{n}}$

### Left Tailed Test
$H_0 : \mu = \mu_0$
$H_A : \mu < \mu_0$
$T = \overline{X}$
Rejection Region: $\overline{X} < c$

### Two Tailed Test 
$H_0 : \mu = \mu_0$
$H_A : \mu \neq \mu_0$
$T = \overline{X}$
Rejection Region: $|\overline{X} - \mu| > c$