class CountFromBy:

    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i
    def increase(self) -> None:
        self.val += self.incr
    def __repr__(self) -> None:
        return str(self.val)