# Parameter Estimation
- It refers to the process of using sample data to make inferences 
or estimates about one or more unknown parameters 
that characterize a statistical population or probability distribution.
- It is a function defined on the samples taken. 

## Estimation Error 
Estimation error is the **difference between an estimated/predicted 
value and the true/actual value** in a 
statistical or modeling context. It quantifies the accuracy or 
precision of an estimation method, reflecting how closely the estimate aligns with the real-world value.

- Let $\theta$ be the parameter and $\hat{\theta}$ be the estimator.

**Error:**  $\hat{\theta}(X_1 , X_2 .... X_n) - \theta$ is a random variable.

## Bias 
Bias refers to the tendency of a statistical estimator 
to systematically overestimate or underestimate a population parameter. 

- Let $X_1 , X_2 , .... X_n \sim \text{iid } X$ , parameter $\theta$,
- The bias of the estimator $\hat{\theta}$ for a parameter $\theta$ is denoted as 

$$\text{Bias}(\hat{\theta} , \theta) = \text{E}(\hat{\theta}) - \theta = \text{Error}$$

!!! note "Unbiased Estimator"
    When Bias/Error is 0 , then the estimator $\hat{\theta}$ is said to be unbiased estimator.

## Risk (Squared Error)
Let $X_1 , X_2 , .... X_n \sim \text{iid } X$ , parameter $\theta$

The squared-error or risk of the estimator $\hat{\theta}$ for a parameter $\theta$ is denoted as

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

