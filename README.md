# A calculator for Binomial Probability-related problems
Inspired by my STATs class, I randomly decided to make a command-line application that has binomial probability-related things in it. 
<br><br>
It can:
* Solve $Pr(X = x)$ questions, including $\leq$, $\geq$, $<$, and $>$.
* Produce a binomial probability table with essential statistics like mean, variance, and standard deviation
* Produce a binomial probability distribution with different graph styles such as line graphs, bar graphs, and scatterplots.
<br><br>

# What is Binomial Probability
<p float="left">
  <img src="https://th.bing.com/th/id/OIP.1HQFaDGys_wVvYfYMeBOiwAAAA?rs=1&pid=ImgDetMain" alt="Binomial Probability Graph" width="33%"/>
  <img src="https://github.com/user-attachments/assets/15a437b0-5218-4dd9-8745-72921c09c2aa" alt="Picture of the app" width="66%"/>
</p>

Binomial probability is used to calculate the success ($\pi$)/failure ($1 - \pi$) in an event, or more generally the probability of something happening and not happpening.
<br><br>
There are certain conditions for an experiment/event to be binomial:
* Event can be summarized to two outcomes (i.e. $\pi$ and its complement)
* Trials ($n$) must be independent
* Trials ($n$) must be fixed prior to data collection
* Probability of success/target outcome ($\pi$) must stay constant

The formula used is:<br>
```math
Pr(X=x)=\binom{n}{x}(\pi^x)(1-\pi)^{n-x}
```
Where:
* $n$ = Total number of independent trials
* $pi$ = Probability of success/target outcome
* $x$ = Probability of x successes (i.e. the little x in $P(X = x)$)
* $\binom{n}{x}$ = Combination formula
<br><br>

# How to install
1. Make sure you installed [Python 3.10](https://www.python.org/downloads/) or higher (since it uses the new `match` case and type annotations).
2. Make sure these libraries are installed:
   ```
   pip install typing
   pip install tabulate
   pip install numpy
   pip install pandas
   pip install matplotlib
   pip install seaborn
   ```
3. Click the green code button and download as a ZIP (or you can clone it).
4. Run BinomialApp.py on your Python terminal or any Python IDE
5. Enjoy!
