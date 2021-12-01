from adventofcode2021.base_solution import BaseSolution


class SonarSweep(BaseSolution):
    """
    Sonar sweep solution:

    https://adventofcode.com/2021/day/1
    """
    input_name = "1.txt"

    def first_task(self) -> int:
        increased_lines = 0
        previous = None
        for line in self.input:
            current = int(line)
            if previous is not None and previous < current:
                increased_lines += 1
            previous = current
        return increased_lines
            
    def second_task(self) -> int:
        first_window = []
        second_window = []
        increased = 0
        for line in self.input:
            if len(first_window) == 3:
                second_window = [first_window[1], first_window[2]]
            else:
                first_window.append(int(line))
                continue
            second_window.append(int(line))
            if sum(first_window) < sum(second_window):
                increased += 1
            first_window, second_window = second_window, []
        return increased
            
    
solution = SonarSweep()
solution.pretty_print()