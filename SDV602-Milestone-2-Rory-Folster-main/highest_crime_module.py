"""
DES to plot the areas with the most crime.
"""

from tkinter import END, ACTIVE, DISABLED, filedialog, messagebox
import tkinter as tk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import total_crimes_module
import common_crimes_module
import global_functions


def show_total_crimes_window():
    """
    Closes root window, and opens the total crimes window using the total crimes module's function.
    """

    root.withdraw()
    total_crimes_module.total_crimes()


def show_most_common_window():
    """
    Closes root window, and opens the common crimes
    window using the common crimes module's function.
    """

    root.withdraw()
    common_crimes_module.most_common_crimes()


def highest_crime_areas():
    """
    Highest crime areas DES.
    """

    global root
    root = tk.Toplevel()
    root.title("Data Anlysis Program")
    root.geometry(
        "970x700+100+100"
    )  # Setting display size (Width x Height) and displaying the window in specific place,
    # important to keep smaller screens in mind as im coding this on a pc monitor.

    data_frame = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/1Ky8WytW2l7IaOBpdwiOmKPIPU5CM2ECLdTmTe1eABMA/export?format=csv#gid=993873974")  # reading csv file
    pie_data = (
        data_frame["count"].iloc[0:5].sort_values(ascending=False)
    )  # getting count column as i need it for the plot
    label_data = data_frame["neighborhood"].iloc[
        0:5
    ]  # getting the neighbourhoods for the label aspect of the plot.

    def data_input_func():
        data_input.delete(0, END)

    def upload_file():
        """
        Creating upload file function. This will involve using Tkinter's 'askopenfilename'
        to get the directory. Pandas will then be used to deconstruct the data and plot an
        additional MatPlotLib plot.
        """

        # this opens a window explorer that will allow a user to select a CSV file
        file = filedialog.askopenfilename(
            # Setting the required file to be a CSV file\
            # to help the user know which file is required.
            filetypes=[("CSV Files", ".csv")],
            defaultextension=".csv",
        )
        # If the user returns a directory, run the following code.
        if file:
            # Increase the size of the window to allow the new plot to fit.
            root.geometry("1600x700+100+100")
            # Adding the dataframe into a variable so i can deconstruct it
            imported_file = pd.read_csv(file)
            # Grabbing the first column
            new_pie_data = imported_file["count"].iloc[0:6].sort_values(
                ascending=False)
            # Grabbing the second column
            new_label_data = imported_file["crime"].iloc[0:6]

            # creating the new figure needed for the new plot
            new_fig = Figure()
            # Adding the pie sub-plot number, 111.
            new_ax = new_fig.add_subplot(111)
            # Adding the count column into the pie function.
            # Also changing the style so it fits and looks nice.
            new_ax.pie(
                new_pie_data,
                radius=1,
                autopct="%0.2f%%",
                shadow=True,
                startangle=140,
                counterclock=False,
            )
            # Adding a legend so the user knows what the data represents.
            new_ax.legend(
                new_label_data,
                title="imported data",
                loc="upper left",
                bbox_to_anchor=(0.9, 1.05),
                # Changing the size of the legend so it fits in the Figure.
                prop={"size": 7},
            )
            # Allowing the reset view button to be used.
            reset_btn.config(state=ACTIVE)
            # creating global variable so that it can be removed as the
            # root window can not be closed and reopened without restarting the app.
            global NEW_FRAME_CHARTS_LT
            # creating new frame
            NEW_FRAME_CHARTS_LT = tk.Frame(root)
            NEW_FRAME_CHARTS_LT.grid(row=1, column=4)
            # adding the figure into the frame and placing the frame on the window.
            new_pie = FigureCanvasTkAgg(new_fig, NEW_FRAME_CHARTS_LT)
            new_chart = new_pie.get_tk_widget()
            new_chart.grid(row=1, column=4)
        else:
            root.geometry("970x700+100+100")
            messagebox.showinfo(
                "CSV File can not be read.", "CSV File can not be read."
            )

    def reset_view():
        """
        Destroys the new frame used for uploading files.
        """
        NEW_FRAME_CHARTS_LT.destroy()  # destorys the current imported plot
        root.geometry(
            "970x700+100+100"
        )  # resets the window size back to the regular size.
        reset_btn.config(state=DISABLED)  # Disables the button once again.

    heading = tk.Label(root, text="Highest Crime Areas in Atlanta")
    heading.grid(row=0, column=0)
    input_data_label = tk.Label(
        root, text="Enter additional data specifications here")
    input_data_label.grid(row=2, column=0)
    show_highest_crimes = tk.Button(
        root, text="Show total crimes", command=show_total_crimes_window)
    show_highest_crimes.grid(row=0, column=2, pady=20)
    show_total_crimes = tk.Button(
        root, text="Show most common crimes", command=show_most_common_window)
    show_total_crimes.grid(row=0, column=3, pady=20)
    frame_charts_lt = tk.Frame(root)
    frame_charts_lt.grid(row=1, column=0)
    data_input = tk.Entry(root, width=15)
    data_input.grid(row=3, column=0, ipady=30, ipadx=270)
    download_data = tk.Button(root, text="Upload File", command=upload_file)
    download_data.grid(row=1, column=2)
    data_input_btn = tk.Button(root, text="Submit", command=data_input_func)
    data_input_btn.grid(row=3, column=1)
    reset_btn = tk.Button(
        root,
        text="Remove import",
        command=reset_view,
        # Setting the state so that the button can only be pressed when a file is imported.
        state=DISABLED,
    )
    reset_btn.grid(row=2, column=2)
    quit_btn = tk.Button(
        root, text="Exit", command=global_functions.on_closing, height=1, width=12)
    quit_btn.grid(row=3, column=2)
    show_chat_btn = tk.Button(
        root, text="Open Chat", command=global_functions.open_chat, height=1, width=12)
    show_chat_btn.grid(row=4, column=2)

    # Creating figure and adding pie plot to it.
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
        label_data, title="Neighborhoods", loc="upper left", bbox_to_anchor=(0.9, 1.05)
    )
    chart = FigureCanvasTkAgg(fig, frame_charts_lt)
    toolbar = NavigationToolbar2Tk(chart)
    toolbar.grid(row=2, column=0)
    chart.get_tk_widget().grid(row=1, column=0)

    root.protocol("WM_DELETE_WINDOW", global_functions.on_closing)
