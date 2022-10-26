# Module 7 - Inheritance & polymorphism
# Author: Amber Wonnenberg
# Date compiled: October 11, 2022


"""
A program that will analyze the number of chromosomes supplied by the
user and determine the sex of the individual, determine if the individual
has down syndrome, and if they have Turners Syndrome.
"""

'''
I am using encapsulation bc of the medical aspect of the assignment. I want to conceal an object class's 
attributes from other classes so that methods in other classes don't accidentally modify data. I am also, using
inheritance so that the subclasses have access to protected data from the parent class.
'''


# Parent class
class Chromosome:

    def __init__(self, chrom_count):
        # Protected variable which is accessible within the class and also to its subclasses.
        self._chrom_count = chrom_count


# child class
class Sex(Chromosome):
    def __init__(self, chrom_count):
        Chromosome.__init__(self, chrom_count)
        self.sex = " "

    # determine male or female base on number of chromosomes
    def determine_sex(self):
        # accessing the protected variable
        if self._chrom_count == 44:
            self.sex = "female"
        elif self._chrom_count == 46:
            self.sex = "male"
        else:
            self.sex = "unknown. Additional testing required."

        return self.sex


class DownSyndrome(Chromosome):
    def __init__(self, chrom_count):
        Chromosome.__init__(self, chrom_count)
        self.down = " "

    # determine if individual hase downs syndrome based on chromosome count
    def determine_downs(self):
        # accessing protected variable
        if self._chrom_count == 47:
            self.down = "may have"
        else:
            self.down = "does not have"

        return self.down


class TurnerSyndrome(Chromosome):
    def __init__(self, chrom_count):
        Chromosome.__init__(self, chrom_count)
        self.turner = " "

    # determine if individual has Turners Syndrome based on chromosome count
    def determine_turner(self):
        # accessing protected variable
        if self._chrom_count == 45:
            self.turner = "has"
        else:
            self.turner = "does not have"

        return self.turner


print('''
----------------------------------------------------------
               Chromosome Count Analysis
----------------------------------------------------------               
''')

user_chrom_count = int(input("Enter in the number of chromosomes and press ENTER: "))

sex = Sex(user_chrom_count)
down = DownSyndrome(user_chrom_count)
turners = TurnerSyndrome(user_chrom_count)

print(f"\nThis individual sex is {sex.determine_sex()}")
print(f"This individual {down.determine_downs()} Down Syndrome")
print(f"This individual {turners.determine_turner()} Turners Syndrome")
