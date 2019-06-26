from util.singleton import Singleton
from random import choice
from pathlib import Path

class PhotoRepository(metaclass=Singleton):

    def __init__(self):
        self.photos = [path for path in Path(Path(__file__).parent.parent.joinpath("teeth")).iterdir() if path.is_file()]

    def get_random_photo(self) -> str:
        return str(choice(self.photos))