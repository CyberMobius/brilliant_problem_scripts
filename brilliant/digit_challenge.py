"""A python library to solve the following type of problem:
      A P P L E
    +   P E A R
    ___________
    C H E R R Y

Where the letters are variables that stand in for digits [0-9]:
"""

from enum import Enum
import re
from dataclasses import dataclass
from typing import Dict, List, Tuple
from itertools import zip_longest


class QuotientTen(Enum):
    zero = 0
    one = 1
    unknown = -1


@dataclass
class SumEqn:
    summands: List[int, int]
    result: int
    quotient_ten: QuotientTen


def problem_parser(
    equation: str, solve_for: str, constraints: Dict[int, int]
) -> List[SumEqn]:
    expression_regex = re.compile(
        r"(?P<summand_1>[a-zA-Z ]+)\+(?P<summand_2>[a-zA-Z ]+)=(?P<sum>[a-zA-Z ]+)"
    )

    whitespace_regex = re.compile(r"\s")

    parsed_problem = expression_regex.fullmatch(equation)
    summand_1 = whitespace_regex.sub("", parsed_problem["summand_1"])[::-1]
    summand_2 = whitespace_regex.sub("", parsed_problem["summand_2"])[::-1]

    result = whitespace_regex.sub("", parsed_problem["sum"])[::-1]

    equations = zip_longest(summand_1, summand_2, result, fillvalue=0)

    equations = [
        SumEqn([eq[0], eq[1]], eq[2], QuotientTen.unknown) for eq in equations
    ] + [SumEqn([0, 0], 0, QuotientTen.zero)]

    return equations


def solve_digit_problem_naive(
    equation: str, solve_for: str = None, constraints: Dict[str, int] = None
):
    """A simple method to solve this kind of problem for simple arithmetic expressions

    Can't handle

    Parameters
    ----------
    problem_string : str
        A string holding a problem
    """
    if constraints is not None:
        solved = constraints.copy()
    else:
        solved = {}

    equations = problem_parser(equation, solve_for, constraints)

    progress = True
    while progress:
        progress = False
        for i, eq in enumerate(equations):
            # Apply hand crafted rules
            a, b = sorted(eq.summands)
            r = eq.result

            if a == b == 0:
                if r == 0:
                    ...
                elif r == 1:
                    ...
                else:
                    ...

        for eq in equations:
            summands = eq.summands

            if summands[0] in solved:
                summands[0] = solved[summands[0]]

            if summands[1] in solved:
                summands[1] = solved[summands[1]]

            if eq.result in solved:
                eq.result = solved[eq.result]

            if type(eq.result) == int:
                if type(summands[0]) == int and summands[0] > eq.result:
                    eq.quotient_ten = QuotientTen.one

                if type(summands[1]) == int and summands[1] > eq.result:
                    eq.quotient_ten = QuotientTen.one

            # if eq.summands[0]


if __name__ == "__main__":
    problem = "APPLE+PEAR=CHERRY"
    solve_digit_problem_naive(problem)
