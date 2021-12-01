from pathlib import Path
from typing import Any

inputs_dir = Path(__file__).parent / "inputs"


class BaseSolution:
    input_name = None

    def __init__(self) -> None:
        if self.input_name is None:
            raise ValueError("Please provide input name.")
        input_file = inputs_dir / self.input_name
        if not input_file.exists():
            raise ValueError("File doesn't exist.")
        with open(input_file) as file_stream:
            self.input = file_stream.readlines()

    def first_task(self) -> Any:
        """
        First task to solve.

        :return: Answer.
        """

    def second_task(self) -> Any:
        """
        Second task to solve.

        :return: Answer.
        """

    def pretty_print(self):
        task_name = self.__class__.__name__
        print(f" {task_name} part one ".center(50, "#"))
        print(self.first_task())
        print(f" {task_name} part two ".center(50, "#"))
        print(self.second_task())
