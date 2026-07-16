import random


class Dice:
    def __init__(self, num_of_dice=2, sides=6):
        self.num_of_dice = num_of_dice
        self.sides = sides

    def tossAndSum(self):
        """Rolls all N dice once and returns the sum."""
        return sum(random.randint(1, self.sides) for _ in range(self.num_of_dice))


class Bins:
    def __init__(self, min_value, max_value):
        self.bins = {value: 0 for value in range(min_value, max_value + 1)}

    def get_bin(self, value):
        return self.bins[value]

    def increment_bin(self, value):
        self.bins[value] += 1

    def get_all_bins(self):
        return self.bins


class Simulation:
    def __init__(self, num_of_dice, total_rolls):
        self.dice = Dice(num_of_dice=num_of_dice)
        self.total_rolls = total_rolls
        self.results = Bins(min_value=num_of_dice, max_value=num_of_dice * 6)

    def run_simulation(self):
        for _ in range(self.total_rolls):
            total = self.dice.tossAndSum()
            self.results.increment_bin(total)

    def print_results(self):
        print(f"Results of rolling {self.dice.num_of_dice} dice {self.total_rolls:,} times:\n")
        print(f"{'Sum':<5} {'Count':<10} {'Percentage':<10} {'Histogram':<50}")
        

        for sum_val, count in self.results.get_all_bins().items():
            percentage = (count / self.total_rolls) * 100
            stars = "*" * round(percentage)
            print(f"{sum_val:<5} {count:<10,} {percentage:>8.2f}% {stars}")


if __name__ == "__main__":
    sim = Simulation(2, 10000)
    sim.run_simulation()
    sim.print_results()


