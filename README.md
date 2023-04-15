# create_svn_url
This Python code allows you to create multiple SVN directories by passing the URLs as command-line arguments and authenticating the user with the provided credentials.


The import statements at the beginning of the code import the necessary modules to execute the script.

The create_svn_url function takes an SVN URL as input and constructs an svn mkdir command using the URL. The subprocess module is used to execute the command in the shell and pass the SVN_USERNAME and SVN_PASSWORD environment variables to authenticate the user. The function returns True if the command executed successfully, and False otherwise.

The sys.argv statement retrieves the command-line arguments passed to the script. The URLs are stored in a list called urls.

The for loop iterates through the urls list and calls the create_svn_url function for each URL. If the function returns True, a success message is printed. If the function returns False, an error message is printed.

python create_svn_url.py https://svn.example.com/repo1/new_folder/sub_folder https://svn.example.com/repo2/new_folder/another_sub_folder


To make the create_svn_urls.py file callable as csurl from the command line, you need to add an alias to your ~/.bashrc file like this:

alias csurl='python /path/to/create_svn_url.py'

Simply add this line to the bottom of your ~/.bashrc file, save the changes, and then run the source ~/.bashrc command in your terminal or open a new terminal. Now you can call the create_svn_url.py file by simply typing csurl in the command line.
