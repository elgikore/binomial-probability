import numpy as np
import math
import pandas as pd # for table

# for graphs
import seaborn as sns
from matplotlib import pyplot as plt 

class BinomialDist:
    """
        This class deals with the binomial distribution, its calculation and graphs.

        Attributes
        ----------
        n: int
            Number of trials.
        pi: float or int
            Probability of success/target of interest.
        probability_table: np.array
            A 2D array (table) containing the x's and its probabilities.
    """

    def __init__(self, n: int, pi: float | int):
        """
            Initializes the values of n and pi.

            Parameters
            ----------
            n: int
                Number of trials.
            pi: float or int
                Probability of success/target of interest
        """
        print()
        self.__n = n
        self.__pi = np.longdouble(pi)

        # Probability array generation
        self.__probability_table = self.__generate_table()
    


    # Table Generation
    def __generate_table(self) -> np.array:
        """Generates a probability table as an `np.array` for decimal precision."""
        probability_table = np.zeros(shape=(self.__n + 1, 2))
        
        for i in range(len(probability_table)):
            probability_table[i] = np.array([i, self.__success_probability(i)])
        
        return probability_table
    
    def __success_probability(self, small_x: int) -> np.longdouble:
        """
            Basically the binomial distribution formula.

            Parameters
            ----------
            small_x: int
                The x value to calculate the probability with.
            
            Returns
            -------
            Probability of x (`small_x`), i.e. Pr(X = x).
        """
        # Combination formula
        nCr = math.factorial(self.__n) / (math.factorial(small_x) * math.factorial(self.__n - small_x))

        return np.longdouble(nCr * (self.__pi ** small_x) * ((1 - self.pi) ** (self.__n - small_x)))



    # Getters and Setters
    @property
    def n(self) -> int:
        """Retrieves the n value."""
        return self.__n
    
    @n.setter
    def n(self, new_n: int) -> None:
        """
            Modifies the n value.
            
            Parameters
            ----------
            new_n: int
                New n value.
        """
        self.__n = new_n
        self.__probability_table = self.__generate_table() # Remake table
    
    @property
    def pi(self) -> np.longdouble:
        """Retrieves the pi value."""
        return self.__pi
    
    @pi.setter
    def pi(self, new_pi: float) -> None:
        """
            Modifies the pi value.

            Parameters
            ----------
            new_pi: float
                New pi value.
        """
        self.__pi = np.longdouble(new_pi)
        self.__probability_table = self.__generate_table()

    @property
    def probability_table(self) -> pd.DataFrame:
        """
            Returns the calculated probability table as a dataframe.

            Returns
            -------
            A dataframe of probabilities (`pd.Dataframe`)
        """
        return pd.DataFrame({
            '(small) x': self.__probability_table[:, 0].astype(int),
            'Probability': self.__probability_table[:, 1]
        })
    


    # Graph
    def show_graph(self, graph_type: str) -> None:
        """
            Graph with specified type.

            Parameters
            ----------
            graph_type: str
                The type of graph specified, either:
                * `'bar'` for bar graph.
                * `'line'` for line graph.
                * `'scatter'` for scatter graph.
                * `'linepoint'` for line graph with visible data points.
                * `'linebar'` for line and bar graph.
            
            Returns
            -------
            `None`

            Throws
            ------
            `ValueError` if `graph_type` isn't one of the valid graph types.
        """
        sns.set_style("whitegrid")

        match graph_type.lower():
            case 'bar':
                ax = sns.barplot(self.probability_table, x='(small) x', y='Probability', color='#3A1078')
            case 'line':
                ax = sns.lineplot(self.probability_table, x='(small) x', y='Probability', c='#4E31AA', markers=True, dashes=False)
            case 'scatter':
                ax = sns.scatterplot(self.probability_table, x='(small) x', y='Probability', c='#3795BD')
            case 'linepoint':
                ax = sns.scatterplot(self.probability_table, x='(small) x', y='Probability', c='#3795BD')
                sns.lineplot(self.probability_table, x='(small) x', y='Probability', c='#4E31AA', markers=True, dashes=False)
            case 'linebar':
                ax = sns.barplot(self.probability_table, x='(small) x', y='Probability', color='#3A1078')
                sns.lineplot(self.probability_table, x='(small) x', y='Probability', c='#3795BD', markers=True, dashes=False)
            case _:
                raise ValueError(f'Invalid input! "{graph_type}" is not a valid graph type.')
        
        plt.suptitle("Probability Distribution", x = 0.125, y = 0.94, ha="left", fontweight="bold", size="xx-large")
        plt.title(f"n = {self.__n}, $\\pi$ = {self.__pi}", x = 1, ha="right", fontweight="light", style="italic", size="small", c="#808080")
        
        ax.set(xlabel='Possible Values (X)', ylabel='Probability of X')
        plt.show()
    


    # Probabiltiy Operations. small_x is basically x in this context, to distunguish it from capital X.
    def less_or_equal(self, small_x: int) -> np.longdouble:
        """
            Equivalent to Pr(X <= x).

            Parameters
            ----------
            target: int
                `small_x` (x) in Pr(X <= x).

            Returns
            -------
            small_x: np.longdouble
                Pr(X <= x) i.e. sum of all probabilities from Pr(X = 0) to Pr(X = x).
        """
        return np.longdouble(np.sum(self.__probability_table[:(small_x + 1), 1]))
    
    def greater_or_equal(self, small_x: int) -> np.longdouble:
        """
            Equivalent to Pr(X >= x).

            Parameters
            ----------
            target: int
                `small_x` (x) in Pr(X >= x).

            Returns
            -------
            small_x: np.longdouble
                Pr(X >= x) i.e. sum of all probabilities from Pr(X = 0) to Pr(X = x) and getting 
                its complement.
        """
        return 1 - self.less_or_equal(small_x)
    
    def lesser_than(self, small_x: int) -> np.longdouble:
        """
            Equivalent to Pr(X < x).

            Parameters
            ----------
            target: int
                `small_x` (x) in Pr(X < x).

            Returns
            -------
            small_x: np.longdouble
                Pr(X < x) i.e. sum of all probabilities from Pr(X = 0) to Pr(X = (x - 1)).
        """
        return np.longdouble(np.sum(self.__probability_table[:small_x, 1]))
    
    def greater_than(self, small_x: int) -> np.longdouble:
        """
            Equivalent to Pr(X > x).

            Parameters
            ----------
            target: int
                `small_x` (x) in Pr(X > x).

            Returns
            -------
            small_x: np.longdouble
                Pr(X > x) i.e. sum of all probabilities from Pr(X = 0) to Pr(X = (x - 1)) and getting 
                its complement. 
        """
        return 1 - self.lesser_than(small_x)
    
    def small_x_value(self, target: int) -> np.longdouble:
        """
            Equivalent to Pr(X = x).

            Parameters
            ----------
            target: int
                `small_x` (x) in Pr(X = x).

            Returns
            -------
            small_x: np.longdouble
                Pr(X = x).
            
            Throws
            ------
            `IndexError` if the `x` value exceeds n
        """
        if target > (len(self.__probability_table) - 1): 
            raise IndexError(f"Outside of range 0 to {len(self.__probability_table) - 1}.")

        return np.longdouble(self.__probability_table[target, 1])
    


    # Mean, variance, and standard deviation
    def binom_mean(self) -> np.longdouble:
        """
            Mean of the binomial distribution.

            Returns
            -------
            `np.longdouble`
        """
        return self.__n * self.__pi
    
    def binom_var(self) -> np.longdouble:
        """
            Variance of the binomial distribution.

            Returns
            -------
            `np.longdouble`
        """
        return self.binom_mean() * (1 - self.__pi)
    
    def binom_sdev(self) -> np.longdouble:
        """
            Standard deviation of the binomial distribution.

            Returns
            -------
            `np.longdouble`
        """
        return np.sqrt(self.binom_var()) 
    

    
    def __str__(self) -> str:
        """
            Displays the attribute values, as well as the mean, variance,
            and standard deviation.
        """
        
        return f'n\t\t{self.__n}\n' \
                f'pi\t\t{self.__pi}\n' \
                f'Mean\t\t{self.binom_mean()}\n' \
                f'Variance\t{self.binom_var()}\n' \
                f'Std. dev.\t{self.binom_sdev()}'