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