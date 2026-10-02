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

## PW2 - Lab B

### Kinetics

In this part, I worked with concentration data and tried to fit it to an exponential model. The model I used was **C(t) = C0 * exp(-k*t)**.

The initial concentration was **104.082**. I used SLSQP to find the value of k that fitted the data best. The value of k was about **0.25**.

I also made a graph of the data and the fitted curve. This made it easier to see how well the model matched the data.

### Conclusion

From this part, I learned how Python can be used to fit a mathematical model to experimental data. I also learned how optimization can be used to find an unknown value such as the rate constant.

---

### Chemical Equilibrium

In this part, I worked with the reaction **H2 + I2 <-> 2HI** and used an equilibrium constant of **K = 15.6**.

I solved the problem using two different methods: Newton's method and SLSQP. The results were almost the same:

* Newton's method: **0.66384766696**
* SLSQP: **0.66384742840**

The equilibrium amounts I got were:

* **H2 = 0.336152 mol**
* **I2 = 0.336152 mol**
* **HI = 1.327695 mol**

Since both methods gave very similar answers, it shows that the calculation was consistent. I also made a graph of the equilibrium results.

### Conclusion

This part helped me understand how a chemical equilibrium problem can be solved using numerical methods. I also learned that using two different methods and comparing the results is a useful way to check the calculation.

---

### Titration — Bonus

For the bonus part, I worked with a titration dataset containing the volume of base added and the pH.

I used `np.gradient()` to calculate how quickly the pH was changing. The equivalence point is where the pH changes the fastest, so I used `np.argmax()` to find the largest slope.

The result was:

* **Equivalence point = 50.0**
* **Maximum slope = 4.0**

I also made two graphs. The first shows the pH changing as more base is added, and the second shows the slope of the curve. The largest slope occurs at **50.0**, which gives the equivalence point.

### Conclusion

This part showed me how the equivalence point can be found from titration data using Python. Instead of trying to find it just by looking at the graph, I used the numerical slope to find the point where the pH changes most quickly.

---

## AI Assistance

I used ChatGPT during the PWs to help me understand the coursework instructions, solve errors, and understand the Python, Git, and Snakemake steps. I wrote and checked the final code and report myself.
