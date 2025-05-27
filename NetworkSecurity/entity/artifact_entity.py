from dataclasses import dataclass

@dataclass
class DataInjestionArtifact:
    trained_file_path:str
    test_file_path:str