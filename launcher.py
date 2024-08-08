import subprocess
import os
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command, shell=False):
    logging.info(f"Running command: {command}")
    result = subprocess.run(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging.info(f"STDOUT: {result.stdout.decode()}")
    logging.error(f"STDERR: {result.stderr.decode()}")
    if result.returncode != 0:
        raise RuntimeError(f"Command failed with exit code {result.returncode}")

def get_python_executable():
    python_executable_path = os.path.join(os.getcwd(), 'Python312', 'python.exe')
    if not os.path.exists(python_executable_path):
        raise FileNotFoundError(f"Python executable not found at {python_executable_path}")
    return python_executable_path

def create_venv(python_exe):
    venv_dir = "./env"
    run_command([python_exe, "-m", "venv", venv_dir])

def install_dependencies():
    venv_python = os.path.join('env', 'Scripts', 'python.exe')
    venv_pip = os.path.join('env', 'Scripts', 'pip.exe')
    run_command([venv_python, '-m', 'pip', 'install', '--upgrade', 'pip'])
    run_command([venv_pip, 'install', '-r', 'requirements.txt'])

def run_app():
    python_exe = os.path.join("env", "Scripts", "python.exe")
    run_command([python_exe, '-m', 'streamlit', 'run', 'app.py'])

def main():
    python_exe = get_python_executable()
    create_venv(python_exe)
    install_dependencies()
    run_app()

if __name__ == "__main__":
    main()
