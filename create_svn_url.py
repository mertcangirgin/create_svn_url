import subprocess
import sys

# Function to create SVN URL directories
def create_svn_url(url):
    # Construct SVN mkdir command using the provided URL
    cmd = f"svn mkdir -p {url}"
    # Use subprocess to execute the SVN mkdir command in the shell
    # and pass the SVN_USERNAME and SVN_PASSWORD environment variables to authenticate the user
    result = subprocess.run(cmd, shell=True, env={"SVN_USERNAME": "username", "SVN_PASSWORD": "password"}, capture_output=True)
    # Check if the command executed successfully
    if result.returncode == 0:
        # If successful, return True
        return True
    else:
        # If unsuccessful, return False
        return False

# Get the list of SVN URLs from the command line arguments
urls = sys.argv[1:]

# Loop through the list of URLs and create each one
for url in urls:
    # Call the create_svn_url function for each URL
    if create_svn_url(url):
        # If the URL was created successfully, print a success message
        print(f"{url} was created successfully.")
    else:
        # If the URL could not be created, print an error message
        print(f"{url} could not be created.")
