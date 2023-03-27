class Person(object):
    """
    Class used to represent an Person
    """

    def __init__(self, id_person: int = 0, name: str = 'Name', last_name: str = "LastName", contact: int = 0):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :param contact: person contact.
        :type contact: int
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._contact = contact

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        : param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    @property
    def contact(self) -> int:
      """ Returns the contact of the person.
        :returns: contact of person.
        :rtype: int
      """
      return self._contact

    @contact.setter
    def contact(self, contact: int):
      """ The contact of the person.
      : param contact: contact of the person
      :type: int
      """
      self.contact = contact

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3})'.format(self.id_person, self.name, self.last_name, self.contact)