"""
Write a program to calculate tax if Salary and Tax Brackets are given as list in the form 
[ [10000, .3],[20000, .2], [30000, .1], [None, .1]]. You don’t know in the beginning how many tax brackets are there. 
You have to test for all of them
"""

"""

public static void main (String[] args) {

	List<List<Double>> levels = new ArrayList<>();

    levels.add( Arrays.asList(10000.0, 0.3) );

    levels.add( Arrays.asList(20000.0, 0.2) );

    levels.add( Arrays.asList(30000.0, 0.1) );

    levels.add( Arrays.asList(null, 0.1) );

    double tax = calculateTax(levels,45000);

    System.out.println(tax);

}

public static double calculateTax(List<List<Double>> levels, double salary ){


}

1. Compute tax for each level until levels exhaust or max salary bracket is reached
2. At each level, reduce salary by taxable income for next level

TC: O(n)
SC: O(1)
"""

def calculateTax(levels, salary):
    tax = 0.0
    remSalary = salary
    i = 0
    while levels[i][0] and remSalary > 0:
        level, taxpct = levels[i]
        tax += taxpct * min(level, remSalary)
        remSalary -= level
        i += 1
    
    if remSalary > 0:
        tax += remSalary * levels[i][1]

    return tax


if __name__ == "__main__":
    salary = 100000
    levels = []
    levels.append((10000.0, 0.3))
    levels.append((20000.0, 0.2))
    levels.append((30000.0, 0.1))
    levels.append((None, 0.1))
    tax = calculateTax(levels, salary)
    print(tax)
