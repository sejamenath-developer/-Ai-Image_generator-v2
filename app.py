import subprocess

# Install pygit2 with the specified version
subprocess.run(['pip', 'install', 'pygit2==1.12.2'])

# Change to the desired directory
subprocess.run(['cd', '/content'])

# Clone the repository from GitHub
subprocess.run(['git', 'clone', 'https://github.com/lllyasviel/Fooocus.git'])

# Change to the cloned repository directory
subprocess.run(['cd', '/content/Fooocus'])

# Run the Python script with the --share argument
subprocess.run(['python', 'entry_with_update.py', '--share'])
