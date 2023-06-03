 It is a function defined on the samples taken. 

## Estimation Error 
Let $\theta$ be the parameter and $\hat{\theta}$ be the estimator
**Error:**  $\hat{\theta}(X_1 , X_2 .... X_n) - \theta$ is a random variable.

## Bias 
Let $X_1 , X_2 , .... X_n \sim \text{iid} X$ , parameter $\theta$
The bias of the estimator $\hat{\theta}$ for a parameter $\theta$ , denoted as 
$$\text{Bias}(\hat{\theta} , \theta) = \text{E}(\hat{\theta}) - \theta = \text{Error}$$
```ad-note 
title:Unbiased Estimator 
When Bias/Error is 0 , then the estimator $\hat{\theta}$ is said to be unbiased estimator.
```

## Risk (Squared Error)
Let $X_1 , X_2 , .... X_n \sim \text{iid} X$ , parameter $\theta$
The squared-error or risk of the estimator $\hat{\theta}$ for a parameter $\theta$ , denoted 
$$\text{Risk}(\hat{\theta}, \theta) = {E[(\hat{\theta} - \theta)^2]}$$
- Since $\text{Error} = \hat{\theta} -\theta$ , risk is the expected value of **squared error** and is also called the **mean squared error** (MSE).
- Squared-error risk is the second moment of Error 

## Variance 
Let $X_1 , X_2 , .... X_n \sim \text{iid} X$ , parameter $\theta$
**Variance of Estimator:**
$$Var(\hat{\theta}) = E[(\hat{\theta} - E[\hat{\theta}])^2]$$
also variance of error is equal to variance of estimator i.e. $Var(\hat{\theta}) = Var(Error)$

## Bias Variance Tradeoff 
Let $X_1 , X_2 , .... X_n \sim \text{iid} X$ , parameter $\theta$
$$\text{Risk}(\hat{\theta} , \theta) = \text{Bias}(\hat{\theta} , \theta)^2 + Var(\hat{\theta})$$
$$\text{Risk} = \text{E}[\text{Error}]^2 = \text{Mean}[\text{Error}]^2 + \text{Var}[\text{Error}]$$

## Sample Moments 
$$X_1 , X_2 , ... X_n \sim \text{iid} \ X$$
**Sample Moments:**
$$M_k(X_1 , X_2 ...., X_n) = \frac{1}{n}\sum^{n}_{i=1}X_{i}^{k}$$

