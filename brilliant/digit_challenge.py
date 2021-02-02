"""A python library to solve the following type of problem:
      A P P L E
    +   P E A R
    ___________
    C H E R R Y

Where the letters are variables that stand in for digits [0-9]:
"""

import re
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class sum_eqn:
    summands: Tuple[int, int]
    result: int
    is_mod_10: bool


def solve_digit_problem_naive(
    equation: str, solve_for: str = None, constraints: List[str] = None
):
    """A simple method to solve this kind of problem for simple arithmetic expressions

    Can't handle

    Parameters
    ----------
    problem_string : str
        A string holding a problem
    """
    expression_regex = re.compile(
        r"(?P<summand_1>[a-zA-Z ]+)\+(?P<summand_2>[a-zA-Z ]+)=(?P<sum>[a-zA-Z ]+)"
    )

    whitespace_regex = re.compile(r"\s")

    parsed_problem = expression_regex.fullmatch(equation)
    summand_1 = whitespace_regex.sub("", parsed_problem["summand_1"])
    summand_2 = whitespace_regex.sub("", parsed_problem["summand_2"])

    result = whitespace_regex.sub("", parsed_problem["sum"])

    max_len = max([len(summand_1, summand_2)])
    for i in range(max_len - 1, -1, -1):
        pass


if __name__ == "__main__":
    problem = "APPLE+PEAR=CHERRY"
    solve_digit_problem_naive(problem)
