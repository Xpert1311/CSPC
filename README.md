# CSPC Computer Science for Physics and Chemistry Lab A Report
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW1/Lab\ A/environment.yml
conda activate cspc

## PW1
Lab A: Reproducible Foundations

**What I built:**
Set up the reproducible workspace, conda environment, Git workflow, decay simulation, and test suite.

**Speed comparison (loop vs NumPy):**
- loop: 2.71 s
- numpy: 0.0003 s
- speed-up: 9196.96x faster

**Tests:** all passing? yes

**Conclusion:** 
Successfully configured the environment and version control. The NumPy implementation showed massive performance gains over the pure-Python loop due to vectorized operations. All unit tests passed successfully.



## PW1
Lab B - Data, Plotting, and Automation

### Results & Findings
- **Data Analysis:** The observed decay dataset closely follows the exponential decay law $N_0 e^{-\lambda t}$.
- **Comparison:** When comparing the scatter plot of the observed data with the analytical curve on shared axes, the two shapes match seamlessly.
- **Snakemake Pipeline:** Snakemake automates the workflow by tracking input/output file timestamps, ensuring that `figure.png` is only rebuilt when `decay_observed.csv` or `plot.py` undergoes modifications.



## PW2
Lab A - Motion from Tracking Data

### Results & Findings
- **Mean Acceleration:** The calculated average acceleration is $-8.58 \text{ m/s}^2$, which is close to the theoretical gravity value of $-9.81 \text{ m/s}^2$.
- **Noise Magnification:** Taking numerical derivatives (`np.gradient`) twice significantly amplified the measurement noise, leading to a large standard deviation of $28.72 \text{ m/s}^2$.
- **Integration Recovery:** Integrating the noisy acceleration back up suppressed the noise and recovered the original position profile with a maximum difference of only $0.78 \text{ m}$.



## PW2
Lab B - Optimization in Chemistry

### Results & Findings
- **Part 2 (Optimization Methods):** For the convex function ($f$), all methods easily agreed on the minimum at $x=3$. However, for the harder polynomial ($g$), the starting point strongly influenced the outcome. From $x_0=0$, Gradient descent and SLSQP found the global minimum (~$-1.30$), but Newton's method landed on a local maximum (~$0.17$) because it only looks for roots of the derivative ($g'' < 0$). From $x_0=2$, GD found a local minimum (~$1.13$), while SLSQP successfully reached the global minimum.
- **Part 3 (Reaction Kinetics):** The fitted reaction rate constant for the first-order decay model was determined to be $k \approx 0.262$, which matched the data perfectly.
- **Part 4 (Chemical Equilibrium):** Both Newton and SLSQP yielded an extent of reaction $x \approx 0.664$. The final equilibrium composition was calculated as: $0.336 \text{ mol}$ of $H_2$, $0.336 \text{ mol}$ of $I_2$, and $1.328 \text{ mol}$ of $HI$.
- **Part 5 (Titration):** Using numerical differentiation, the highest slope of the pH curve indicated an equivalence point exactly at $50.0 \text{ mL}$.




## PW3 - Data, Distributions, Testing, and Causation

### Session 1: Characterising the Data
- **Distributions & Normality:** I plotted the histograms for `age`, `chol`, `trestbps`, and `thalach` and ran the Shapiro-Wilk test to evaluate normality numerically. For all four variables, the p-values were significantly less than 0.05, meaning none of them are normally distributed. Therefore, non-parametric statistical tests must be used for further analysis.

### Session 2: Drawing Conclusions
- **Heart Rate Comparison:** To determine if max heart rate (`thalach`) differs between healthy and diseased patients, I used the **Mann-Whitney U test** because the data is not normally distributed. The test yielded a p-value close to zero ($1.86 \times 10^{-13}$), confirming a statistically significant difference. Healthy patients have a higher mean maximum heart rate ($158.38 \pm 1.50$) compared to those with heart disease ($139.26 \pm 1.92$).
- **Age vs. Max Heart Rate:** There is a moderate negative correlation ($r \approx -0.39$) between `age` and `thalach`. As age increases, the maximum heart rate tends to decrease.
- **Category Predictability (Bonus):** The `target` variable is well-balanced, with about 54% of patients classified as healthy and 46% as diseased. This near 50/50 split means guessing a patient's status blindly would be highly unpredictable.

### The Chemical Mystery: Correlation vs Causation
- **Naive Analysis:** Initially, both chemicals appeared linked to malignancy, but `cadmium` showed a significantly stronger correlation ($0.88$) than `benzene` ($0.38$). At face value, Cadmium looked like the primary cause.
- **The Reality (Controlling for Confounders):** I restricted the dataset to patients with a similar `pollution_index` (between 45 and 55) to eliminate the confounding effect of general pollution. In this isolated group, the correlation between `cadmium` and `malignancy` dropped entirely to $0.0$, while the correlation for `benzene` increased to $0.65$.
- **Conclusion:** **Benzene** is the true chemical driver of malignancy. Cadmium only appeared guilty because it strongly co-occurs in highly polluted areas (the third variable), creating a false correlation with cancer rates.
