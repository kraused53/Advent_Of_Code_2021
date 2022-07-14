from os.path import exists


# -----------------------------------------------------------
'''
    Description:

    Input:
        fp (string) -> path to the file 
            containing the depth measurements
    Output:
        If file exists -> 
        If file does not exist -> None
'''
def DayA(fp):
    # Does the file exist?
    if exists(fp):
        # If yes:
        return None
    else:
        # If no:
        # Display a simple error message
        print('The given file does not exist...')
        # Return None
        return None


# -----------------------------------------------------------
'''
    Description:

    Input:
        fp (string) -> path to the file 
            containing the depth measurements
    Output:
        If file exists -> 
        If file does not exist -> None
'''
def DayB(fp):
    # Does the file exist?
    if exists(fp):
        # If yes:
        return None
    else:
        # If no:
        # Display a simple error message
        print('The given file does not exist...')
        # Return None
        return None


'''
    Run this when main
'''
if __name__ == '__main__':
    # Input file path
    fp = './inputs/day1.txt'
    
    # Does the file exist?
    if exists(fp):
        print(DayA(fp))
        print(DayB(fp))
    else:
        print('File does not exist!')
