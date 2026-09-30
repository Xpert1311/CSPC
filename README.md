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
