from collections import defaultdict as dd
from typing import Callable, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class defaultdict(dd, Generic[K, V]):
    """
    defaultdict provides typings for collections.defaultdict, as well as a few quality of life improvements.

    - Supports nested defaultdicts, e.g. defaultdict(defaultdict(int))
    - Reverts __str__ and __repr__ to the builtin dict representation
    """

    def __init__(self, default_factory: Callable[[], V], *args, **kwargs):
        super().__init__(default_factory, *args, **kwargs)

    def __getitem__(self, key: K) -> V:
        return super().__getitem__(key)

    def __setitem__(self, key: K, value: V):
        super().__setitem__(key, value)

    def __call__(self) -> "defaultdict":
        return self.__class__(self.default_factory)

    def __str__(self):
        return str(dict(self))

    def __repr__(self):
        return str(self)
