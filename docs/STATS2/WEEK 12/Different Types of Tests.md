## Normal Samples and Statistics 
$$X_1 , X_2 , X_3 ..... X_n \sim iid \text{ Normal}(\mu , \sigma^2)$$
- Sample Mean $\overline{X} = \frac{1}{n}(X_1 + X_2 + X_3 .... + X_n)$
- Sample Variance $S^2 = \frac{1}{n-1}((X_1 - \overline{X})^2 + (X_2 - \overline{X})^2 + ...... + (X_n - \overline{X})^2)$
$$\overline{X} \sim \text{ Normal}(\mu , \frac{\sigma^2}{n})$$
$$\frac{(n-1)}{\sigma^2}S^2 \sim \chi^{2}_{n-1}$$
$$\frac{\overline{X} - \mu}{S / \sqrt{n}} \sim t_{n-1}$$


## T-Test for Mean (unknown variance)
$$X_1 , X_2 ,  ...... ,X_n \sim \text{ Normal}(\mu , \sigma^2)$$
- Null $H_0 : \mu = \mu_0, \text{ Alternative } H_A : \mu > \mu_0$
- $T = \overline{X}$ , Test : Reject $H_0 \text{ if } T > c$

**Computing Significance Level**
- Sample Variance $S^2 = \frac{1}{n-1}\sum^{n}_{i=1}(X_i - \overline{X})^2$
- Given , $H_0 ,\frac{T - \mu_0}{S /  \sqrt{n}} \sim t_{n-1}$
$$\alpha = P(T > c | \mu = \mu_0) = P(t_{n-1} > \frac{c - \mu_0}{S / \sqrt{n}}) = 1 - F_{t_{n-1}}(\frac{c- \mu_0}{S/ \sqrt{n}})$$
## $\mathbf{\chi^2}$ test for variance 
$$X_1 , X_2 , ..... iid \text{ Normal}(\mu , \sigma^2)$$
- Null $H_0 : \sigma = \sigma_0$ , Alternative $H_A : \sigma > \sigma_0$
- $S^2 = \frac{1}{n-1}\sum^{n}_{i=1}(X - \overline{X})^2$ ,  Test: Reject $H_0$ if $S >c$

**Computing Significance Level**
- Given $H_0$ , $\frac{n-1}{\sigma_0^2}S^2 \sim \chi^{2}_{n-1}$
- $\alpha = P(S > c | H_0) = P(\frac{n-1}{\sigma_0^2})S^2 > \frac{n-1}{\sigma_0^2})c^2 = 1 - F_{\chi^{2} _{n-1}}(\frac{n-1}{\sigma_0^2}c^2)$


## Two Samples from Normal Distribution 
$$X_1 , X_2 , X_3 , ...... X_n \sim \text{iid Normal}(\mu_1 , \sigma^2_1 )$$
$$Y_1 , Y_2 , Y_3 , ...... Y_n \sim \text{iid Normal}(\mu_2 , \sigma^2_2 )$$
- $\overline{X} \sim \text{ Normal}(\mu_1 , \sigma_1^2 / n_1)$ , $\overline{Y} \sim \text{ Normal}(\mu_2 , \sigma_2^2 / n_2)$
- $(\frac{n_1-1}{\sigma^2_1})S^2_X \sim \chi^2_{n_1 - 1}$ , $(\frac{n_2-1}{\sigma^2_2})S^2_Y \sim \chi^2_{n_2 - 1}$
- $\overline{X} - \overline{Y} \sim \text{Normal}(\mu_1 - \mu_2 , \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2})$
- If $\sigma_1 = \sigma_2$
	- $\frac{S^2_X}{S^2_Y} \sim F(n_1 -1 , n_2 - 1)$

## Two Samples Z-test 
$$X_1 , X_2 , X_3 , ...... X_n \sim \text{iid Normal}(\mu_1 , \sigma^2_1 )$$
$$Y_1 , Y_2 , Y_3 , ...... Y_n \sim \text{iid Normal}(\mu_2 , \sigma^2_2 )$$
- Null $H_0 : \mu = \mu_0, \text{ Alternative } H_A : \mu \neq \mu_0$
- $T = \overline{Y} - \overline{X}$ , Test : Reject $H_0 \text{ if } |T| > c$

**Computing Significance Level**
Given $H_0$ , $T \sim \text{Normal}(0 , \sigma_{T}^{2})$ , where $\sigma_T^2 = \frac{\sigma_1^2}{n_1} + \frac{\sigma^2_2}{n_2}$
$$\alpha = P(|T| > c | H_0) = P(|\text{Normal}(0,1)| > \frac{c}{\sigma_{T}})$$
## Two Sample F-test 
$$X_1 , X_2 , X_3 , ...... X_n \sim \text{iid Normal}(\mu_1 , \sigma^2_1 )$$
$$Y_1 , Y_2 , Y_3 , ...... Y_n \sim \text{iid Normal}(\mu_2 , \sigma^2_2 )$$
- Null $H_0 : \sigma_1 = \sigma_2$ , Alternative $H_A : \sigma_1 \neq \sigma_2$
- T = $\frac{S_X^2}{S_Y^2}$ , Test : Reject $H_0$ if $T > 1 + c_R$ or $T < 1 - c_L$
- Given $H_0$ , $T \sim F(n_1 -1 , n_2 -1)$
- $\alpha / 2 = P(T < 1 - c_L | H_0) = P(T > 1 + c_R | H_0)$
	