import json
import logging
from pathlib import Path
import requests
from typing import Union, List

from .SDTLResult import SDTLResult


class SDTLClient:

    def __init__(self, endpoint_url: str, input_file: Union[Path, str], converter_type: str):
        """
        Create the SDTL client. It needs to know which endpoint to use, so pass it in. This endpoint
        will be different for SASS and R.

        :param endpoint_url: The SDTL API endpoint
        :param input_file: The script being sent to the converter
        :param converter_type: The type of SDTL converter (sas, python, etc)
        """
        logging.debug("Creating SDTLClient with args: {} , {}".format(endpoint_url, input_file))
        # The endpoint for the client to use
        self.endpoint_url: str = endpoint_url
        # Holds the results from the conversion
        self.results: List[SDTLResult] = []
        # A list of path objects representing files that will be converted
        self.input_files: List[Path] = []
        # A list of path objects representing directories of files that will be converted
        self.input_directories: List[Path] = []
        self.converter_type: str = converter_type
        # Add files or directories
        self.add_file(input_file)

    def add_file(self, file_path: Union[str, Path]) -> None:
        """
        Adds a file to the client.

        :param file_path: The path to the file
        :return: None
        """
        logging.debug("Adding file: {} to the client".format(str(file_path)))
        if isinstance(file_path, str):
            file_path = Path(file_path)
        self.input_files.append(file_path)

    def add_artifact(self, artifact: Union[str, Path, List[Path], List[str]]) -> None:
        """
        Adds a file or folder to the client. It can also be a list of filenames.
        """
        logging.debug("Adding filesystem artifacts to the client")
        # Check to see if it's iterable
        try:
            iter(artifact)
        except TypeError:
            artifact_path = Path(artifact)
            if artifact.is_dir():
                self.add_directory(artifact_path)
            elif artifact_path.is_file():
                self.add_file(artifact_path)
            return

        for file_artifact in artifact:
            artifact_path = Path(file_artifact)
            if artifact_path.is_file():
                self.add_file(artifact_path)
            elif artifact_path.is_dir():
                self.add_directory(artifact_path)

    def add_directory(self, directory_path: Union[str, Path]) -> None:
        """
        Adds a directory of files to the client.

        :param directory_path: The Path object representing a directory
        :return: None
        """
        logging.debug("Adding directory: {} to the client".format(str(directory_path)))
        if isinstance(directory_path, str):
            directory_path = Path(directory_path)
        self.input_directories.append(directory_path)

    def transform_files(self) -> None:
        """
        Takes the files and directories in the client and converts them into SDTL. The
        results are saved into Result objects.
        :return: None
        """
        #for directory in self.input_directories:
        #    for file in directory.glob('**/*'):
        #        sdtl = self.get_sdtl(file)
        #        if sdtl is not None:
        #            self.add_result(SDTLResult(sdtl, file.name))
        #for file in self.input_files:
        sdtl = self.get_sdtl(self.input_files[1])
        if sdtl is not None:
            self.add_result(sdtl, "sdtl_output.json")

    def get_sdtl(self, code: Union[str, Path]) -> Union[dict, None]:
        """
        Gets the SDTL representation of a file or string

        :param code: The string of code being converted
        :return: dict, None
        """
        if isinstance(code, Path):
            with open(code, "r") as python_source:
                code = python_source.read()
        data = {
            "parameters": {
                f"{self.converter_type}": code
            }
        }
        logging.info("Retrieving SDTL for script")
        response = requests.post(url=self.endpoint_url,
                                 data=json.dumps(data))
        return response.json()

    def add_result(self, sdtl, filename) -> None:
        """
        Adds a result from a parser to the client
        :param sdtl: The SDTL from the cliennt
        :param filename:
        :return:
        """
        logging.debug("Adding result for {}.".format(filename))
        result = SDTLResult(sdtl, filename)
        self.results.append(result)

    def save(self, directory_path: Union[Path, str] = None) -> None:
        logging.debug("Saving the client client.")
        for run in self.results:
            run.save(directory_path)
