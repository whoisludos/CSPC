# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup

Create the environment for a given lab:

```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**

* Created a reproducible Conda environment for the practical work.
* Implemented a radioactive decay simulation using both a pure-Python loop and a vectorised NumPy version.
* Added automated tests with pytest and managed the project using Git and GitHub.

**Speed comparison (loop vs NumPy):**

* loop: 1.835957 s
* numpy: 0.000162 s
* speed-up: 11354.16x faster

**Tests:** all passing? **yes**

**Conclusion:**

The NumPy implementation is much faster than the pure-Python loop for this simulation. In this test, NumPy was approximately 11,354 times faster. The project also has automated tests and a reproducible environment, making the work easier to run and verify.
