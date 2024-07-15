
from plot_functions.date_month_covid import plot_data


def main():
    # Read data
    filename = "data/Autauga_Covid.csv"

    # Plot data
    plot_data(filename)

if __name__ == "__main__":
    main()