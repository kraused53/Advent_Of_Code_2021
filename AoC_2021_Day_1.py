from os.path import exists


# -----------------------------------------------------------
'''
    Description:
        Given a set of depth measurments, count
            the number of times that the current
            depth is deeper than the old depth.

    Input:
        fp (string) -> path to the file 
            containing the depth measurements
    Output:
        If file exists -> (int) Number of times
            the current depth was larger than 
            the old depth
        If file does not exist -> None
'''
def DayA(fp):
    # Does the file exist?
    if exists(fp):
        # If yes:
        # Create a counting variable
        count = 0

        # Open the file
        with open(fp, 'r') as f:
            # Create a list containing the line-by-line
            #   contents of the file
            depths = f.readlines()
        
        # Store the value of the first depth
        old_depth = int(depths[0])

        # Cylce through the remainder of the depth values
        for i in range(1, len(depths)):
            # Store value of next depth
            new_depth = int(depths[i])

            # Is it biger than the last depth?
            if new_depth > old_depth:
                # If yes, increase count by 1
                count = count + 1
            
            # Move new depth into old depth for the
            #   next comparison
            old_depth = new_depth
        # Return the answer
        return count
    else:
        # If no:
        # Display a simple error message
        print('The given file does not exist...')
        # Return None
        return None


# -----------------------------------------------------------
'''
    Description:
        Given a set of depth measurments, count
            the number of times that the current
            depth is deeper than the old depth
            using a basic averaging algorithm
            to weed out noise.

    Input:
        fp (string) -> path to the file 
            containing the depth measurements
    Output:
        If file exists -> (int) Number of times
            the current depth was larger than 
            the old depth
        If file does not exist -> None
'''
def DayB(fp):
    # Does the file exist?
    if exists(fp):
        # If yes:
        # Create a counting variable
        count = 0

        # Open the file
        with open(fp, 'r') as f:
            # Create a list containing the line-by-line
            #   contents of the file
            depths = f.readlines()
        
        # Store the value of the first depth
        old_depth = int(depths[0]) + int(depths[1]) + int(depths[2])

        # Cylce through the remainder of the depth values
        for i in range(3, len(depths)):
            # Store value of next depth
            new_depth = int(depths[i-2]) + int(depths[i-1]) + int(depths[i])

            # Is it biger than the last depth?
            if new_depth > old_depth:
                # If yes, increase count by 1
                count = count + 1
            
            # Move new depth into old depth for the
            #   next comparison
            old_depth = new_depth
        # Return the answer
        return count
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
