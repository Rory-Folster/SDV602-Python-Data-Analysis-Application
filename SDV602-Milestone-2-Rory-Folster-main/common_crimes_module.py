"""
DES to plot the most common crimes in Atlanta DES.
"""

from tkinter import END, ACTIVE, DISABLED, filedialog, messagebox
import tkinter as tk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import highest_crime_module
import total_crimes_module
import global_functions

def most_common_crimes():
    """
    Most Common Crimes DES.
    """
    data_frame = pd.read_csv("https://docs.google.com/spreadsheets/d/18CMql-YKfH3Pw8eVHFtXUjefVIl6P40bIbirCCEwFo0/export?format=csv#gid=1590555330")
    pie_data = data_frame["count"].iloc[0:6].sort_values(ascending=False)
    label_data = data_frame["crime"].iloc[0:6]


    def data_input_func():
        data_input.delete(0, END)

    def reset_view():
        most_common_crimes_window.destroy()
        most_common_crimes()

    def upload_file():
        file = filedialog.askopenfilename(
            filetypes=[("CSV Files", ".csv")], defaultextension=".csv"
        )
        if file:
            most_common_crimes_window.geometry("1600x700+100+100")
            imported_file = pd.read_csv(file)
            new_pie_data = (
                imported_file["count"].iloc[0:6].sort_values(
                    ascending=False)
            )
            new_label_data = imported_file["crime"].iloc[0:6]

            new_fig = Figure()
            new_ax = new_fig.add_subplot(111)
            new_ax.pie(
                new_pie_data,
                radius=1,
                autopct="%0.2f%%",
                shadow=True,
                startangle=140,
                counterclock=False,
            )
            new_ax.legend(
                new_label_data,
                title="imported data",
                loc="upper left",
                bbox_to_anchor=(0.9, 1.05),
                prop={"size": 7},
            )
            reset_btn.config(state=ACTIVE)
            new_frame_charts_lt = tk.Frame(most_common_crimes_window)
            new_frame_charts_lt.grid(row=1, column=4)
            new_pie = FigureCanvasTkAgg(new_fig, new_frame_charts_lt)
            new_chart = new_pie.get_tk_widget()
            new_chart.grid(row=1, column=4)
        else:
            most_common_crimes_window.geometry("970x700+100+100")
            messagebox.showinfo(
                "CSV File can not be read.", "CSV File can not be read."
            )

    def show_main():
        most_common_crimes_window.destroy()
        highest_crime_module.highest_crime_areas()

    def show_total_crimes_window():
        most_common_crimes_window.destroy()
        total_crimes_module.total_crimes()

    most_common_crimes_window = tk.Toplevel()
    most_common_crimes_window.title("Data Analysis Program")
    most_common_crimes_window.geometry("970x700+100+100")
    heading = tk.Label(most_common_crimes_window,
                       text="Most common crimes in Atlanta")
    heading.grid(row=0, column=0)
    frame_charts_lt = tk.Frame(most_common_crimes_window)
    frame_charts_lt.grid(row=1, column=0)
    input_data_label = tk.Label(
        most_common_crimes_window, text="Enter additional data specifications here"
    )
    input_data_label.grid(row=2, column=0)
    show_highest_crimes = tk.Button(
        most_common_crimes_window, text="Highest crime areas", command=show_main)
    show_highest_crimes.grid(row=0, column=2, pady=20)
    show_total_crimes = tk.Button(
        most_common_crimes_window, text="Total crimes", command=show_total_crimes_window)
    show_total_crimes.grid(row=0, column=3, pady=20)
    data_input = tk.Entry(most_common_crimes_window, width=15)
    data_input.grid(row=3, column=0, ipady=30, ipadx=270)
    download_data = tk.Button(
        most_common_crimes_window, text="Upload File", command=upload_file
    )
    download_data.grid(row=1, column=2)
    data_input_btn = tk.Button(
        most_common_crimes_window, text="Submit", command=data_input_func
    )
    data_input_btn.grid(row=3, column=1)
    reset_btn = tk.Button(
        most_common_crimes_window,
        text="Remove import",
        command=reset_view,
        state=DISABLED,
    )
    reset_btn.grid(row=2, column=2)
    quit_btn = tk.Button(
        most_common_crimes_window, text="Exit", height=1, width=12, command=global_functions.on_closing
    )
    quit_btn.grid(row=3, column=2)

    fig = Figure()
    plot_axes = fig.add_subplot(111)
    plot_axes.pie(
        pie_data,
        radius=1,
        autopct="%0.2f%%",
        shadow=True,
        startangle=140,
        counterclock=False,
    )
    plot_axes.legend(
        label_data,
        title="Crimes",
        loc="upper left",
        bbox_to_anchor=(0.9, 1.00),
        prop={"size": 7},
    )
    chart = FigureCanvasTkAgg(fig, frame_charts_lt)
    toolbar = NavigationToolbar2Tk(chart)
    toolbar.grid(row=2, column=0)
    chart.get_tk_widget().grid(row=1, column=0)

    most_common_crimes_window.protocol("WM_DELETE_WINDOW", global_functions.on_closing)