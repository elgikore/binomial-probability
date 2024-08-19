import sys
import os
from BinomialDistribution import BinomialDist
from typing import Callable
from tabulate import tabulate

binomial = None

def clear() -> None:
    # Works well in VSCode; from: https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
    # The Console.Clear() equivalent in Python
    print("\033[H\033[J", end='')

    # In case escape codes aren't supported
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_continue() -> None:
    input("Press ENTER to continue. ")
    clear()

def not_in_selection() -> None:
    print("Not in selection!", end=' ')
    clear_continue() 

def end_screen() -> None:
    print('See you soon! Press ENTER to quit. ', end=' ')
    input()
    sys.exit(0)

def header(title_name: str, symbol: str = '=', equals_length: int = 80) -> None:
    print(f"{symbol * equals_length}")
    print(f"{title_name.center(equals_length)}")
    print(f"{symbol * equals_length}")

def title() -> None:
    header("Binomial Distribution Calculator")
    print("             / n \\      x         n - x")
    print("Pr(X = x) = |     | (pi)  (1 - pi)")
    print("             \\ x /")
    print("\nWhere:")
    print("\t- n = Total number of independent trials")
    print("\t- pi = Probability of success/target outcome")
    print("\t- x = Probability of x successes (i.e. the little x in P(X = x))")
    print("Conditions:")
    print("\t- Event can be summarized to two outcomes (i.e. pi and its complement)")
    print("\t- Trials (n) must be independent")
    print("\t- Trials (n) must be fixed prior to data collection")
    print("\t- Probability of success/target outcome (pi) must stay constant\n")

def n_and_pi(header_screen: Callable) -> tuple[int, float]:
    while True:
        header_screen()

        print("NOTE: Type Q/q to quit.\n")

        try:
            n = input("What is the value of n? (Must be a whole number): ")
            if (n.lower() == 'q'): end_screen()
            n = int(n)

            pi = input("What is the value of pi?: ")
            if (pi.lower() == 'q'): end_screen()
            pi = float(pi)
        except ValueError as val_err:
            print(f"Invalid input! ({val_err})", end=' ')
            clear_continue()
            continue
        else:
            return (n, pi)


def selection(header_screen: Callable, selection_list: tuple) -> int:
    selection_list_len = len(selection_list)
    
    while True:
        header_screen()
        print("What do you want to do?")
        for num, selection in enumerate(selection_list):
            print(f"({num + 1}) {selection}")
        print("(0) Quit")

        try:
            selection = int(input(f"\nPlease enter a number between 0 and {selection_list_len}: "))
            
            if (selection < 0 or selection > selection_list_len): not_in_selection()
        except ValueError as val_err:
            print(f"Invalid input! ({val_err})", end=' ')
            clear_continue()
            continue
        else:
            return selection

def graph_selection(header_screen: Callable, graph_selections: tuple) -> None:
    while True:
        match selection(header_screen, graph_selections):
            case 0: 
                clear_continue()
                break
            case 1: 
                binomial.show_graph('bar')
                clear_continue()
            case 2: 
                binomial.show_graph('line')
                clear_continue()
            case 3: 
                binomial.show_graph('scatter')
                clear_continue()
            case 4:
                binomial.show_graph('linepoint')
                clear_continue()
            case 5:
                binomial.show_graph('linebar')
                clear_continue()
            case _: 
                continue

def probability_operations(header_screen: Callable, pr_selections: tuple) -> None:
    while True:
        match selection(header_screen, pr_selections):
            case 0: 
                clear_continue()
                break
            case 1:
                clear()
                x = set_x_value(pr_selections[0])
                print(f"Pr(X <= {x}) = {binomial.less_or_equal(x)}\n")
                clear_continue()
            case 2:
                clear()
                x = set_x_value(pr_selections[1])
                print(f"Pr(X >= {x}) = {binomial.greater_or_equal(x)}\n")
                clear_continue()
            case 3:
                clear()
                x = set_x_value(pr_selections[2])
                print(f"Pr(X < {x}) = {binomial.lesser_than(x)}\n")
                clear_continue()
            case 4:
                clear()
                x = set_x_value(pr_selections[3])
                print(f"Pr(X > {x}) = {binomial.greater_than(x)}\n")
                clear_continue()
            case 5:
                clear()
                x = set_x_value(pr_selections[4])
                print(f"Pr(X = {x}) = {binomial.small_x_value(x)}\n")
                clear_continue()
            case _:
                continue

def set_x_value(header_title: str) -> int:
    total_x_instances = len(binomial.probability_table) - 1

    while True:
        header(header_title, '-')
        print("NOTE: Type Q/q to quit.\n")

        try:
            x = input(f"What is the value of x (i.e small x)? Must be between 0 and {total_x_instances}: ")
            if (x.lower() == 'q'): 
                clear_continue()
                break

            x = int(x)
            
            if (x < 0 or x > total_x_instances): 
                not_in_selection()
                continue
        except ValueError as val_err:
            print(f"Invalid input! ({val_err})", end=' ')
            clear_continue()
            continue
        else:
            return x

if __name__ == "__main__":
    MAIN_MENU_SELECTIONS = ("Operations on Pr(X = x)", "Graph", "Summary", "Change x and pi")
    GRAPH_SELECTIONS = ("Bar Graph", "Line Graph", "Scatterplot", "Line Graph with Points", "Line and Bar Graph")
    PR_SELECTIONS = ("Pr(X <= x)", "Pr(X >= x)", "Pr(X < x)", "Pr(X > x)", "Pr(X = x)")
    
    # Title Screen
    n_pi = n_and_pi(title)
    binomial = BinomialDist(n_pi[0], n_pi[1])
    clear()
    
    # Main menu
    while True:
        match selection(lambda: header("Main Menu"), MAIN_MENU_SELECTIONS):
            case 0: end_screen()
            case 1:
                clear()
                probability_operations(lambda: header(MAIN_MENU_SELECTIONS[0], '*'), PR_SELECTIONS)
            case 2:
                clear()
                graph_selection(lambda: header(MAIN_MENU_SELECTIONS[1], '*'), GRAPH_SELECTIONS)
            case 3:
                clear()
                header(MAIN_MENU_SELECTIONS[2], '*')
                print(tabulate(binomial.probability_table, headers="keys", showindex=False, tablefmt="double_grid"), '\n')
                print(binomial, '\n')
                clear_continue()
            case 4:
                clear()
                n_pi = n_and_pi(lambda: header(MAIN_MENU_SELECTIONS[3], '*'))
                binomial = BinomialDist(n_pi[0], n_pi[1])
                clear_continue()
            case _:
                continue
