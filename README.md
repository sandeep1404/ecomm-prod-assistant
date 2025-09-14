These are all the commands that you need to run on your command prompt

1. Write Python in your terminal
2. If you have Python, then no need to install it
3. uv --version
If you are not able to get the version
4. Pip install uv
5. import shutil
   print(shutil.which("uv"))
 
6. Uv init <my-project-name>
7. uv pip list
 
8. uv python list
9. uv venv env --python cpython-3.10.18-windows-x86_64-none
10. uv venv <your-env-namne> --python <your-python-version>
Note: Please use either 3.10, 3.11, or 3.12
11. Command Prompt (CMD)  .\<your-env-nanme>\Scripts\activate.bat
12. Git Bash ya WSL terminal, or MAC Terminal:
13. source <your-env-nanme>/Scripts/activate


If your git is asking for a login to publish the repo, execute the command below
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
UV add <package_name>
Uv add -r requirements.txt
Streamlit run <give your streamlit python filename>
Install the live server extension in VS Code for testing the HTML

For accessing the DataStax, here is a link: https://accounts.datastax.com/session-service/v1/login

Vectordb Comparison: https://superlinked.com/vector-db-comparison

