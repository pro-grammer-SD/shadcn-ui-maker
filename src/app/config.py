from subprocess import run, CalledProcessError
from os import remove
from os.path import exists
from pathlib import Path
import webbrowser
import multiprocessing
import socket
import time

class Maker:
    def __init__(self, project_dir: str):
        self.make_command = "npx shadcn@latest init"
        self.start_command = "npm run dev"
        self.project_dir = Path(project_dir)

    def make(self):
        try:
            run(self.make_command, check=True, shell=True)
            print(f"[Maker] Project '{self.project_dir}' initialized successfully.")
        except CalledProcessError as e:
            print(f"[Maker] Init failed: {e}")

    def rmv(self):
        if exists(self.project_dir):
            try:
                remove(self.project_dir)
                print(f"[Maker] Project '{self.project_dir}' removed successfully.")
            except Exception as e:
                print(f"[Maker] Failed to remove project '{self.project_dir}': {e}")
        else:
            print(f"[Maker] Project '{self.project_dir}' not found.")

    def _run_server(self):
        run("npm run dev", check=True, shell=True, cwd=self.project_dir)

    def _wait_for_server(self, host="localhost", port=3000, timeout=60):
        start = time.time()
        while time.time() - start < timeout:
            try:
                with socket.create_connection((host, port), timeout=2):
                    return True
            except OSError:
                time.sleep(0.5)
        return False

    def start(self):
        try:
            p = multiprocessing.Process(target=self._run_server)
            p.start()
            if self._wait_for_server():
                print("[Maker] Server started successfully.")
                webbrowser.open("http://localhost:3000")
            else:
                print("[Maker] Server did not start in time.")
        except CalledProcessError as e:
            print(f"[Maker] Failed to start the server: {e}")   
        
class ComponentManager:
    def __init__(self, component_name: str, app_name: str):
        self.a_name = app_name
        self.c_name = component_name.lower()
        self.c_file = Path(app_name) / "components" / "ui" / f"{self.c_name}.tsx"
        self.add_command = f"npx shadcn@latest add {self.c_name}"
        
    def add(self):
        try:
            run(self.add_command, check=True, shell=True, cwd=self.a_name)
            print(f"[Component] Component '{self.c_name}' added successfully.")
            print(f"[Component] For Docs, please visit: https://ui.shadcn.com/docs/components/{self.c_name}")
        except CalledProcessError as e:
            print(f"[Component] Failed to add '{self.c_name}': {e}")

    def rmv(self):
        if exists(self.c_file):
            try:
                remove(self.c_file)
                print(f"[Component] Removed: {self.c_file}")
            except Exception as e:
                print(f"[Component] Failed to remove '{self.c_file}': {e}")
        else:
            print(f"[Component] File not found: {self.c_file}")

if __name__ == "__main__":
    Maker("my-app").start()
