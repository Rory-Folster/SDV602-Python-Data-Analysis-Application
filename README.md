# SDV602-Python-Data-Analysis-Application
Data analysis application created with Python, Tkinter, Pandas and Matplotlib. 

The login page is connected to an SQL Server hosted on my PC. The application connects remotely so any computer with this application can connect, although
I will probably close the server soon as this is only a school project.
When a user logins into the application, an update query is sent to the database to update a column named 'is_online' in the User table, this allows users
to see online users by executing a query to find 'is_online' column = 1 (0 is offline).

The plot data is host on Google Sheets, and is exported as a CSV format so that Pandas can fetch the data and I can deconstruct it to create plots.

The chat system is using socket and threading supplied from Python. A user can type '/users' to get a list of users online currently, or '/clear' to clear the 
message history.
