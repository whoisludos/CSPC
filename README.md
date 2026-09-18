# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup

Create the environment for a given lab:

```bash
conda env create -f PW<n>/Lab <X>/environment.yml
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

In this lab, I set up a Conda environment and worked on a radioactive decay simulation.

I made two versions of the simulation:

* one using a normal Python loop
* one using NumPy

The NumPy version was much faster than the normal Python version.

**Speed comparison:**

* loop: 1.835957 s
* NumPy: 0.000162 s
* speed-up: 11354.16x

I also added tests using pytest and used Git and GitHub to keep track of my work.

**Tests:** all passing? **yes**

**Conclusion:**

The main thing I learned from this lab is that NumPy can make calculations much faster than using a normal Python loop. I also learned how to use tests, Git, and a reproducible Conda environment for my project.

---

## PW1 - Lab B

In this lab, I worked with radioactive decay data. The number of observed particles went down as time increased, which is what we expect from radioactive decay.

The observed data was quite close to the analytical curve. The graph showed that both had a similar decreasing shape.

I also used Snakemake to make the process easier. It takes the CSV data, runs the Python program, and creates the graph automatically. If nothing has changed, Snakemake does not run the program again.
