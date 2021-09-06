from abc import ABC
import abc
from src.siren.config.db import session


class AbstractRepository(ABC):

    def __init__(self):
        self.session = session

    @abc.abstractmethod
    def add(self, model: object):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> object:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> object:
        raise NotImplementedError
