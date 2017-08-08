from abc import ABCMeta, abstractmethod


class IView:
    @abstractmethod
    def say(self, message): raise NotImplementedError
