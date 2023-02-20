#!/user/bin/python3
"""
    Class Base Model
"""

import uuid
from datetime import datetime


class BaseModel:
    """
        Defines all common attributes/methods for other classes

        ATTRIBUTS:
        ==============
            id : public, string assgin with uuid4 method

            create_at: date of creation

            update_at: date of modification

        METHODS:
        =============

            __str__ : [<class name>] (<self.id>) <self.__dict__>

            save(self): method to update create_at and stock in update_at

            to_dict(self): dict of all key/values

    """

    def __init__(self, *args, **kwargs):
        # generate random UUID
        self.id = str(uuid.uuid4())
        # first initialization : creates and updated time = now
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            [<class name>] (<self.id>) <self.__dict__>
                   |           |             |
                name of class  |             |
                            uniq uuid4       |
                                          instance attributs set
        """
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    def save(self):
        """
            update the public instance attribute updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            dictionary all keys/values of __dict__ of the instance
        """
        # copy dict
        copy_dict = self.__dict__.copy()
        # implement new key/value
        for key, value in copy_dict.items():
                setattr(self, key, value)
        copy_dict['__class__'] = type(self).__name__
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()
        return (copy_dict)
