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

## Conclusion

In this lab, I learned how radioactive decay can be analysed using data and Python. I also learned how Snakemake can automate the analysis process and avoid running steps again when the data has not changed.

---

## PW2 — Lab A

### Motion from Tracking Data

The mean acceleration I got was **-8.58 m/s²**, which is fairly close to the expected value of **-9.81 m/s²** for free fall.

The acceleration was much noisier than the position data. This is because when we differentiate the data, the small errors and noise in the measurements become bigger. Since we differentiated twice to get acceleration, the noise became even more noticeable. The standard deviation of the acceleration was **28.72 m/s²**.

After integrating the acceleration to get the velocity and then the position, the recovered position was quite close to the original position. The biggest difference was only **0.78 m**. This shows that integration helps reduce the noise that appeared during differentiation.

## Conclusion

In this lab, I learned how to calculate velocity and acceleration from noisy position data and how differentiation can increase the noise. I also learned that integrating the data back can reduce the noise and give a position close to the original one.

---

## AI Assistance

I used ChatGPT during the PWs to help me understand the coursework instructions, solve errors, and understand the Python, Git, and Snakemake steps. I wrote and checked the final code and report myself.
