def main():
    print("RUN main.py")

# A function to get an input file
# Uncomment the commented line to take the input from the user. Meanwhile, comment the line below it.


def file_input():
    dirLocation = "../data/input/XSM Extracted Light Curve"
    # inputFile = str(input("Enter date: "))
    inputFile = str(20200406)

    file = dirLocation + "/ch2_xsm_" + inputFile + "_v1_level2.lc"
    return (file, inputFile)

# A function to convert the input file to a pandas dataframe


def dataFrameReturner():
    from astropy.table import Table
    import pandas as pd

    temp = Table.read(str(file_input()[0]), format="fits")
    df = temp.to_pandas()

    return df


if __name__ == "__main__":
    main()

else:
    file_input()
