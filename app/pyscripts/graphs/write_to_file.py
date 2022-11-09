from __init__ import csv

def writePointsToFile(pointsList, filename):
    # method to write data to file
    # used by 1D and 2D page modules 
    with open(f"app/pyscripts/graphs/data_points_csv/{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])
        writer.writerows(pointsList)