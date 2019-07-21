import pathlib
from typing import Union, List, Tuple


def remove_and_create_empty_directory(directory: pathlib.Path):
    """Remove directory if it exists, and create a new directory using specified path

    Parameters
    ----------
    directory : str
        Path of directory that you want to clear
    """

    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir()


def get_genres(directory: pathlib.Path) -> Tuple[int, List[str]]:
    genres = [dirname.stem for dirname in directory.iterdir() if dirname.stem != ".DS_Store"]
    num_files = len(genres)
    return (num_files, genres)
