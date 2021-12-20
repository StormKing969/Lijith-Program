# Welcoming Message
print("Real Estate Analyzer")

# Creating a list for property
sPropertyList = []


# Takes the list and return the medium
def getMedium(current):
    # sorts the list in ascending order
    current.sort(key=float)
    # get the length of the list
    lengthList = len(current)

    # Check if the list is even
    if lengthList % 2 == 0:
        # Looks for the middle indexed value when the list is even
        val1 = float(current[int((lengthList / 2))])
        # Gets the value that indexed before the middle
        val2 = float(current[int((lengthList / 2 - 1))])
        # Calculates the medium
        middleVal = (val1 + val2) / 2
        return "{:.2f}".format(float(middleVal))
    # When the list is odd
    else:
        # Get the medium
        middleVal = current[int((lengthList / 2))]
        return "{:.2f}".format(float(middleVal))


def getFloatInput(val):
    # User input
    propertyValue = input("Enter the property Value: $ ")

    # Loops if the userInput contains letter or is zero
    while propertyValue.isalpha() or propertyValue == "0":
        print("Input a number that is greater than 0")
        propertyValue = input("Enter the property Value: $ ")

    # Checks if the userInput is less or equal to zero
    if float(propertyValue) <= 0:
        print("Input a number that is greater than 0")
        getFloatInput("Enter property sales value: $ ")
    else:
        # Returns the value if all the conditions pass
        return "{:.2f}".format(float(propertyValue))


# Returns the total Value of the properties
def totalAmount(values):
    x = 0.0
    for i in values:
        x += float(i)
    return "{:.2f}".format(float(x))


# Returns the Average
def AvgAmount(numbers, total):
    avg = float(total) / numbers
    return "{:.2f}".format(float(avg))


if __name__ == '__main__':
    sPropertyList.append(getFloatInput("Enter the property Value: $ "))

    # Checking if user wants to add more property
    sCondition = input("Do you want to add another property Y or N: ").upper()

    # Loop that makes sure that only "Y" or "N" are entered
    while sCondition != "N" or sCondition != "Y":
        sCondition = input("Do you want to add another property Y or N: ").upper()
        if sCondition == "Y":
            break

    while sCondition != "N":
        sPropertyList.append(getFloatInput("Enter the property Value: $ "))
        sCondition = input("Do you want to add another property Y or N: ").upper()

    # Sorts the list in order
    sPropertyList.sort(key=float)

    # Used to print all the properties listed
    counter = 0
    print()
    for i in sPropertyList:
        counter += 1
        print(f"Property {counter} $ {'{:,.2f}'.format(float(i))}")
    print()

    minValue = sPropertyList[0]
    maxValue = sPropertyList[-1]
    totalValue = totalAmount(sPropertyList)
    averageValue = AvgAmount(len(sPropertyList), totalAmount(sPropertyList))
    medianValue = getMedium(sPropertyList)
    commissionValue = (float(totalAmount(sPropertyList)) * 0.03)

    # Used f-string and format to produce a "$123,000.00" output
    print(f"Minimum Value: $ {'{:,.2f}'.format(float(minValue))}")
    print(f"Maximum Value: $ {'{:,.2f}'.format(float(maxValue))}")
    print(f"Total Value: $ {'{:,.2f}'.format(float(totalValue))}")
    print(f"Average: S {'{:,.2f}'.format(float(averageValue))}")
    print(f"Median: $ {'{:,.2f}'.format(float(medianValue))}")
    print(f"Commission: $ {'{:,.2f}'.format(commissionValue)}")
