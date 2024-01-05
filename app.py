import subprocess

# Install pygit2 with the specified version
install_pygit2 = subprocess.run(['pip', 'install', 'pygit2==1.12.2'], capture_output=True, text=True)

# Change to the desired directory
change_directory = subprocess.run(['cd', '/content'], shell=True, capture_output=True, text=True)

# Clone the repository from GitHub
clone_repository = subprocess.run(['git', 'clone', 'https://github.com/lllyasviel/Fooocus.git'], capture_output=True, text=True)

# Change to the cloned repository directory
change_to_cloned_dir = subprocess.run(['cd', '/content/Fooocus'], shell=True, capture_output=True, text=True)

# Run the Python script with the --share argument
run_script = subprocess.run(['python', 'entry_with_update.py', '--share'], capture_output=True, text=True)

# Print the deployment link or output from the script
print(run_script.stdout)
