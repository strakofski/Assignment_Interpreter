from abc import ABCMeta, abstractmethod


class IFileHandler:
    __metaclass__ = ABCMeta

    @abstractmethod
    def load_file(self, file): raise NotImplementedError

    @abstractmethod
    def write_file(self, file, data): raise NotImplementedError
