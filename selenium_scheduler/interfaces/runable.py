from abc import abstractmethod


class Runable:
    @abstractmethod
    def run(self) -> None:
        pass
