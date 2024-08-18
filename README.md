# A calculator for Binomial Probability-related problems
Inspired by my STATs class, I randomly decided to make a command-line application that has binomial probability-related things in it.

# What is binomial probability
<p float="left">
  <img src="https://th.bing.com/th/id/OIP.1HQFaDGys_wVvYfYMeBOiwAAAA?rs=1&pid=ImgDetMain" alt="Binomial Probability Graph" width="300"/>
  <img src="https://github.com/user-attachments/assets/15a437b0-5218-4dd9-8745-72921c09c2aa" alt="Picture of the app" width="550"/>
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

# How to install
