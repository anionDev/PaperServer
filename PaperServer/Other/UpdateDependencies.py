from pathlib import Path
import requests
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TFCPS.TFCPS_Tools_General import TFCPS_Tools_General


def get_latest_version_number(timeout_in_seconds: int) -> str:
    url = 'https://api.papermc.io/v2/projects/paper'
    response = requests.get(url=url, timeout=timeout_in_seconds)
    data = response.json()
    version_numbers = data['versions']
    latest_version_number = version_numbers[-1]
    return latest_version_number


def get_latest_build_number(version_number: str, timeout_in_seconds: int) -> str:
    url = f'https://api.papermc.io/v2/projects/paper/versions/{version_number}/builds'
    response = requests.get(url=url, timeout=timeout_in_seconds)
    data = response.json()
    build_numbers = data['builds']
    latest_build_number = build_numbers[-1]['build']
    return str(latest_build_number)


def get_latest_paper_version() -> str:
    timeout_in_seconds = 3
    latest_version_number = get_latest_version_number(timeout_in_seconds)
    latest_build_number = get_latest_build_number(latest_version_number, timeout_in_seconds)
    return f"{latest_version_number};{latest_build_number}"

def update_dependencies():
    script_file = str(Path(__file__).absolute())
    sc = ScriptCollectionCore()
    TFCPS_Tools_General(sc).update_dependency_in_resources_folder(script_file, "Paper", get_latest_paper_version())



if __name__ == "__main__":
    update_dependencies()
