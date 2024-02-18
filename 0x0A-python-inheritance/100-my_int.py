#!/usr/bin/python3
"""contains a custom int class"""


class MyInt(int):
    """defines a rebellious int"""

    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        return not super().__ne__(__value)
