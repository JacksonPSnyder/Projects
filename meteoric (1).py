"""
    Module for displaying information about meteor data from the NASA Meteorite Landings dataset:
    https://data.nasa.gov/widgets/gh4g-9sfh

    Created by: <Jackson Snyder, Alex Grommesh>
""" 
import sys
import csv
import math


def load_data():
    """Load meteorite data into a "list of lists".
    Each element in the list corresponds to a single line in the CSV file.
    Each line has 9 elements: name,id,nametype,recclass,mass (g),fall,year,reclat,reclong

    Returns:
        list: a list of lists, where each inner list contains the data for one meteor
    """
    with open('meteorite_landings.csv', encoding='utf-8', newline='') as csvfile:
        next(csvfile)  # skip the header row
        return list(csv.reader(csvfile))
    

def get_year(meteors, year):
    """ This function recieves the validated year input by the user
    and the list of lists of meteor's attributes it then returns every 
    meteor and its attributes discovered in the year entered in the form 
    of a list of lists.

    Args:
        meteors (List): list of lists of meteors with each index being a different attribute
        year (str): the year by which the user would like to see every meteor discovered in that year.

    Returns:
        list: list of lists which contains every meteor discovered in the year entered by the user
        along with all of its attributes
    """
    new_list = []
    for i in meteors:
        if str(i[2]) == str(year):
            new_list.append(i)
    return new_list


def get_geopoint(meteors, geopoint):
    """This function receives the validated geopoint input by the user
    and the list of lists of meteor's attributes. It then uses a python 
    implementation of the haversine formula found on geeksforgeeks.org,
    created by ChitraNayal, to create a list of distances. I slightly modified 
    the formula based off of another implementation on stackoverflow. It then returns
    the meteor(s) with the smallest distance. 

    geeksforgeeks link: https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/#
    stackoverflow link: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    

    Args:
        meteors (List): List of lists of meteors with each index being a different attribute.
        geopoint (float): comma separated latitude and longitude coordinates. 
    """
    reclat1, reclong1 = map(float, geopoint.split(',')) # use of map was seen on stackoverflow
    RECLAT1_RADIANS = math.radians(reclat1)
    EARTH_RADIUS = 6371

    closest_meteors = []
    minimum_distance = float('inf')
    
    for meteor in meteors:
        # Try block will catch any invalid formatting of the latitude and longitude
        #  from the meteorrite_landing.cvs file. 
        try:
            reclat2 = float(meteor[3])
            reclong2 = float(meteor[4])
        except ValueError:
            continue
        except IndexError:
            continue

        # Distance between latitudes and longitudes in radians
        distance_between_lat = math.radians(reclat2 - reclat1)
        distance_between_long = math.radians(reclong2 - reclong1)

        # Convert reclat2 to radians
        reclat2_radians = math.radians(reclat2)

        # Haversine formula
        a = (math.sin(distance_between_lat / 2) ** 2 + 
             math.sin(distance_between_long / 2) ** 2 * 
             math.cos(RECLAT1_RADIANS) * math.cos(reclat2_radians))
        c = 2 * math.asin(math.sqrt(a))
        
        # Multiply by Earth's radius to get distance in kilometers
        distance = EARTH_RADIUS * c

        # Checks if the meteor is closer than the current closest meteor. 
        # If the distance is the same, it will store both meteors data. 
        if distance < minimum_distance:
            minimum_distance = distance
            closest_meteors = [meteor]
        elif distance == minimum_distance:
            closest_meteors.append(meteor)
    
    return closest_meteors, minimum_distance


def is_valid_arg(command, arg):
    """ This function is used to verify that the arguments associated with the command are valid.

    Args:
        command (str): The 'year' or 'geopoint' function the user specifies.
        arg (int, float): argument the user provided. Should be an integer for the year function, and either an integer or float for geopoint.

    Raises:
        ValueError: Coordinates are not numeric.
        ValueError: Either 1, or 3+ coordinates were received.
        ValueError: latitude is out of range: [-90,90]
        ValueError: Longitude os out of range: [-180,180]
        ValueError: The year is not properly formatted. It either contains letters or decimal values. 
        ValueError: The year was entered as a negative number.

    Returns:
        bool: Returns True if all conditions are passed. Returns False otherwise.
    """
    if command == 'geopoint':
        try:
            coordinates = []
            # need to use the .split() to separate the lat and long as a str, then convert to a float.
            for element in arg.split(','):
                coordinates.append(float(element))
        except ValueError:
            raise ValueError ("Error: Coordinates must be numeric.")

        # Validates that there are only 2 coordinates
        if len(coordinates) != 2:
            raise ValueError ("Error: Only 1 latitude and 1 longitude can be excepted.")

        # Validates that the coordinates are in range
        if (coordinates[0] < -90) or (coordinates[0] > 90):
            raise ValueError ("Error: The latitude must be within the range [-90, 90].")
        elif (coordinates[1] < -180) or (coordinates[1] > 180):
            raise ValueError ("Error: The longitude must be within the range [-180, 180]")

    elif command == "year":
        try:
            year = int(arg)
        except ValueError:
            raise ValueError("Error: The year must be an integer.")
        
        if year < 0:
            raise ValueError("Error: The year must be positive.")

    else:
        return False
    return True

def is_valid_command(command):
    """This function is used to check if the command the user inputted is acceptable.

    Args:
        command (str): The first input the user types into the consol.

    Returns:
        bool: Returns True if the command is within the VALID_COMMANDS list. Returns False otherwise. 
    """
    command = command.lower()
    VALID_COMMANDS = ["year", "geopoint"]
    for i in VALID_COMMANDS:
        if i == command:
            return True
    return False


def main():
    """The main function that provides the console interface for the application.
    """
    # attempt to get the command and argument from the CLI or the input() console.
    if len(sys.argv) == 3:
        command = sys.argv[1]
        arg = sys.argv[2]
    else:
        print("Give a command. Options are: year or geopoint")
        try:
            command, arg = input("Enter a command: ").split(' ')
        except ValueError:
            print("Expected a command and data but only received 1")
            return
    # Read the CSV file data into a list.
    meteors = load_data()

    # Add code here to validate command & arg, and then call the functions to process the data.
    if not is_valid_command(command.lower()):
        print("Invalid command entered. Please re-enter the command.")
        return
    
    try:
        if command.lower() == "year":
            if is_valid_arg(command, arg):
                list_of_years = get_year(meteors, arg)
                if len(list_of_years) == 0:
                    print("No meteor found in that year.")
                for i in list_of_years:
                    print(f"Meteor {i[0]} with an id of {i[1]} was discovered in {i[2]}.")


        if command.lower() == "geopoint":
            if is_valid_arg(command, arg):
                closest_meteor = get_geopoint(meteors, arg)
                print(f"The closest meteorite landings from your given coordinates is {closest_meteor[1]:.2f} kilometers away. The following are the meteors:")
                for meteoric_data in closest_meteor[0]:
                    print(f"Meteorite ID. {meteoric_data[1]}: {meteoric_data[0]}. The meteor landed in {meteoric_data[2]} at latitude {meteoric_data[3]}, longitude {meteoric_data[4]}.")

    except ValueError as err:
        print(f"\n{err} \nExample of valid format: year 1999 | geopoint 70,-25.000\n")

if __name__ == "__main__":
    main()