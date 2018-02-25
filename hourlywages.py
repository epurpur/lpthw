#defines calcWeeklyWages function with 2 arguments, totalHours and hourlyWage
def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40: #checks to see if totalHours is <= 40
        totalWages = hourlyWage*totalHours #standard paycheck = wage * hours
    else:
        overtime = totalHours - 40 #if totalHours > 40, subtract 40 from that number to get hours of overtime
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime #calculates regular rate up to 40 hours, then does formula for overtime (1.5 * hourlyWage) * overtime.  Adds those 2 number together
    return totalWages #returns value totalWages

def main():
    hours = float(input('Enter hours worked: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.' #:.2f creates 2 decimal places
          .format(**locals()))

main()
