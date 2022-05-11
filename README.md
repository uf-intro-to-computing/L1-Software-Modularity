### Python Virtual Environment Setup
A python virtual environment allows you to create an isolated folder with a well-defined python interpreter version and set of dependencies. This minimizes conflicts between python projects that might arise due to library or interpreter version differences. You can easily delete the virtual environment by removing the folder from your computer.

To create the virtual environment for this project, run the following command in your shell:
`python -m venv .venv`

Activate the virtual environment on Windows PowerShell by typing `.\.venv\Scripts\Activate.ps1` or on bash by typing `source .venv/bin/activate.sh`.

After activating the virtual environment, install the dependencies by typing
`pip install -r requirements.txt`

Run the program by typing `python gui.py`