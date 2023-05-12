#!/usr/bin/python3

"""
This defines the custome errors used in a File Storage
"""


class ModelNotFoundError(Exception):
    """Raised when an unknown module is passed"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class InstanceNotFoundError(Exception):
    """Raised when an unknown id  is passed"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Insatnce of {mod} with id {obj_id} does not exist!")
