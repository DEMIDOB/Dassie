import os, platform

def setup_dassie():
    os_name = platform.system()
    def_python_command = "python" if os_name == "Windows" else "python3"

    os.system(f"{def_python_command} -m venv dassie")
    os.system("source dassie/bin/activate")

    python_command = "dassie/bin/python3"
    os.system(f"{python_command} -m pip install -r requirements.txt")
    os.system(f"{python_command} -m pip freeze")

    import colorama
    colorama.init()
    print()
    print(colorama.Back.GREEN + "All the requirements are satisfied." + colorama.Back.BLACK)
    print()
    print(colorama.Fore.GREEN + f"To start your work with Dassie run '{def_python_command} dassie.py'")


if __name__ == '__main__':
    setup_dassie()
