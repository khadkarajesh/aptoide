from dataclasses import dataclass


@dataclass
class AppInformation:
    name: str = ''
    version: str = ''
    download: str = ''
    release_date: str = ''
    description: str = ''
