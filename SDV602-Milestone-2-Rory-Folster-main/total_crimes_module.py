"""
DES to plot the total amount of crimes per year in Atlanta.
"""

from tkinter import END, ACTIVE, DISABLED, filedialog, messagebox
import tkinter as tk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import highest_crime_module
import common_crimes_module
import global_functions

def total_crimes():
    """
    Total Crimes DES.
    """

    data_frame = pd.read_csv("https://docs.google.com/spreadsheets/d/1LsAkkGQjYag7OumMM-FWMZxHRTUItBv0i-3iKoqlUJw/export?format=csv#gid=1577085985")  # Reading csv file
    y_data = data_frame["date"].iloc[
        0:8
    ]  # Splitting each column into seperate variables to be used with the bar graph.
    x_data = (
        data_frame["count"].sort_values(ascending=False).iloc[0:8]
    )  # Selecting only 0-8 entries as the final entry (2017) does not have a full year of entries.

    def reset_view():
        total_crimes_window.destroy()
        total_crimes()

    def data_input_func():  # placeholder function until I start making the data filtering.
        data_input.delete(0, END)

    def upload_file():  # This function has been explained below.
        file = filedialog.askopenfilename(
            filetypes=[("CSV Files", ".csv")], defaultextension=".csv"
        )
        if file:
            total_crimes_window.geometry("1600x700+100+100")
            imported_file = pd.read_csv(file)
            new_y_data = (
                imported_file["neighborhood"].iloc[0:8].sort_values(
                    ascending=False)
            )
            new_x_data = imported_file["count"].iloc[0:8]
            reset_btn.config(state=ACTIVE)
            new_fig = Figure()
            new_ax = new_fig.add_subplot()
            new_ax.bar(new_y_data, new_x_data)
            new_ax.set_xticks(new_y_data)
            new_frame_charts_lt = tk.Frame(total_crimes_window)
            new_frame_charts_lt.grid(row=1, column=4)
            new_bar = FigureCanvasTkAgg(new_fig, new_frame_charts_lt)
            new_chart = new_bar.get_tk_widget()
            new_chart.grid(row=1, column=4)
        else:
            total_crimes_window.geometry("850x700+100+100")
            messagebox.showinfo(
                "CSV File can not be read.", "CSV File can not be read."
            )

    def show_main():
        total_crimes_window.destroy()
        highest_crime_module.highest_crime_areas()

    def show_common_crimes_window():
        total_crimes_window.destroy()
        common_crimes_module.most_common_crimes()

    total_crimes_window = (
        tk.Toplevel()
    )  # creating top level instance of tkinter as you can only have one root window
    total_crimes_window.title("Data Anlysis Program")  # Setting the title
    # Setting the size of the gui
    total_crimes_window.geometry("970x700+100+100")
    heading = tk.Label(
        total_crimes_window, text="Total amount of crimes per year in Atlanta"
    )  # Creating a heading so the user knows which window they're on
    heading.grid(
        row=0, column=0
    )  # Using grid() instead of pack() so i can adjust where the widgets sit on the page.
    input_data_label = tk.Label(
        total_crimes_window, text="Enter additional data specifications here"
    )
    input_data_label.grid(row=2, column=0)
    frame_charts_lt = tk.Frame(
        total_crimes_window
    )  # Creating a frame from tkinter so I can add the plot onto it
    frame_charts_lt.grid(row=1, column=0)
    data_input = tk.Entry(total_crimes_window, width=15)
    data_input.grid(row=3, column=0, ipady=30, ipadx=270)
    data_input_btn = tk.Button(
        total_crimes_window, text="Submit", command=data_input_func
    )
    data_input_btn.grid(row=3, column=1)
    show_highest_crimes = tk.Button(
        total_crimes_window, text="Highest crime areas", command=show_main)
    show_highest_crimes.grid(row=0, column=2, pady=20)
    show_total_crimes = tk.Button(
        total_crimes_window, text="Common crimes", command=show_common_crimes_window)
    show_total_crimes.grid(row=0, column=3, pady=20)
    download_data = tk.Button(
        total_crimes_window, text="Upload File", command=upload_file
    )
    reset_btn = tk.Button(
        total_crimes_window,
        text="Remove import",
        command=reset_view,
        state=DISABLED,
    )
    reset_btn.grid(row=2, column=2)
    download_data.grid(row=1, column=2)
    quit_btn = tk.Button(
        total_crimes_window, text="Exit", height=1, width=12, command=global_functions.on_closing
    )  # Creating an exit button
    quit_btn.grid(row=3, column=2)

    fig = Figure()  # Creating new figure from matplotlib
    plot_axes = fig.add_subplot(111)  # Adding an axes to Figure
    plot_axes.bar(
        y_data, x_data
    )  # Creating a bar graph and adding the two columns of data from the edited csv
    plot_axes.set_xticks(
        y_data
    )  # Allowing the graph to display all years instead of skipping some.
    chart = FigureCanvasTkAgg(
        fig, frame_charts_lt
    )  # Adding the Figure and plot together using the FigureCanvasTkAgg interface
    toolbar = NavigationToolbar2Tk(chart)
    toolbar.grid(row=2, column=0)
    chart.get_tk_widget().grid(row=1, column=0)

    total_crimes_window.protocol("WM_DELETE_WINDOW", global_functions.on_closing)