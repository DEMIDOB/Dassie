import os, platform


def setup_dassie():
    os_name = platform.system()

    im_on_windows = os_name == "Windows"

    def_python_command = "python" if im_on_windows else "python3"

    venv_name = "venv"

    os.system(f"{def_python_command} -m venv {venv_name}")
    # os.system(f"source {venv_name}/bin/activate")

    python_command = f"{venv_name}\\Scripts\\python" if im_on_windows else f"{venv_name}/bin/python3"

    os.system(f"{python_command} -m pip install -r requirements.txt")
    print()
    os.system(f"{python_command} -m pip freeze")

    import colorama
    colorama.init()
    print()
    print(colorama.Fore.GREEN + "All the requirements are satisfied.")
    print()
    print(colorama.Fore.GREEN + f"To start your work with Dassie run '{def_python_command} dassie.py'")


if __name__ == '__main__':
    setup_dassie()
