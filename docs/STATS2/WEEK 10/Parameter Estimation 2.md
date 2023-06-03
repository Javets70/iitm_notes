## Bayesian Estimation 
$$X_1 , X_2 .... X_n \sim , \text{parameter } \Uptheta$$
- Prior distribution of $\Uptheta$ : $\Uptheta \sim f(\Uptheta)$
- Bayes' rule : posterior $\propto$ likelihood $\times$ prior 

$$P(\Uptheta = \theta | S) = \frac{P(S|\Uptheta = \theta) \times f_{\Uptheta}(\theta)}{P(S)}$$
![[Pasted image 20230410153658.png]]

## Choice of Priors
### Types of Priors 
- **Flat , uninformative:** 
	- Nearly flat over the interval in which the parameter takes value 
	- This usually reduces to something close to maximum likelihood.

- **Conjugate Priors:** 
	- Pick a prior so that the posterior is in the same class as the prior.

- **Informative Priors**: 
	- This needs some justification from the domain of the problem.
	- Parameterize the prior so that its flatness can be controlled.


### Examples 
#### Bernoulli Distribution 
$$X_1 , X_2 .... X_n \sim \text{iid } \text{Bernoulli}(\mathbf{p})$$
- Prior $\mathbf{p} \sim \text{Uniform}[0,1]$ , continuous distribution 
- Samples: $x_1 , x_2 , x_3 ..... x_n$
- $w = x_1 + x_2 + ... + x_n$ 
- Posterior density: $\text{Beta}(w + 1 , n -w + 1)$
	- Posterior Mean: $\frac{w+ 1}{(w+1) + (n-w+1)} = \frac{w+1}{n+2} =\frac{x_1 + x_2 + ... +x_n + 1}{n+2}$

#### Bernoulli Distribution with beta prior 
$$X_1 , X_2 .... X_n \sim \text{iid } \text{Bernoulli}(\mathbf{p})$$
- Prior $\mathbf{p} \sim \text{Beta}(\alpha,\beta)$ , continuous distribution 
- $w = x_1 + x_2 + ... + x_n$ 
- Posterior Density: $\text{Beta}(w + \alpha , n - w + \beta)$
	- Posterior Mean: $\frac{w + \alpha}{(w + \alpha) + (n - w + \beta)} = \frac{w + \alpha}{n + \alpha + \beta}$

### Observations for Beta Prior 
- Prior : $\text{Beta}(\alpha , \beta)$
	- $\alpha , \beta \geq 0$
	- PDF $\propto p^{\alpha - 1}(1-p)^{\beta -1} , 0 < p < 1$
- $\alpha = \beta = 1$
	- Flat prior 
	- Estimate close to but not equal to maximum -likelihood 
- $\alpha = \beta = 0$
	- Estimate coincides with Maximum-likelihood.
- $\alpha = \beta$
	- Symmetric Prior 

### Normal sample with known mean and known variance 
$$X_1 , X_2 .... X_n \text{iid Normal}(M ,\sigma^2)$$
Prior $M \sim Normal(\mu_{0} , \sigma_{0}^{2})$ , continuous distribution 
$f_M(\mu) = \frac{1}{\sqrt{2 \pi}\sigma_0} \text{exp}(- \frac{(\mu - \mu_0)^2}{2 \sigma_{0}^{2}})$

- Posterior Density : Normal 
- Posterior Mean = $\overline{x}\frac{n \sigma_{0}^{2}}{n \sigma_{0}^{2} + \sigma^2} + \mu_0 \frac{\sigma^2}{n \sigma_{0}^{2} + \sigma^2}$


