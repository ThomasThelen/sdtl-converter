import json
from pathlib import Path
from typing import Union


class SDTLResult:
    """
    Class that holds the SDTL for a particular file.
    """

    def __init__(self, sdtl: dict, filename: str) -> None:
        """
        Create an SDTL result.
        :param sdtl:
        :param filename:
        """
        self.sdtl: json = sdtl
        self.filename: str = filename

    def save(self, directory_path: Union[Path, str] = None) -> None:
        """
        Saves the SDTL to disk. It's named 'filename-sdtl.json'. The default location
        is ./sdtl.

        :param directory_path: The directory where the output should be saved
        :return: None
        """
        if directory_path is None:
            directory_path = Path("./")
        full_path = Path(directory_path, self.filename).with_suffix(".json")
        with open(full_path, "w") as outfile:
            json.dump(self.sdtl, outfile, indent=4)
