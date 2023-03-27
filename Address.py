class Address(object):
    """
    Class used to represent an Address
    """

    def __init__(self, house_number: int = 0, street: str = 'street' , city: str ='city', state: str = 'state', country: str = 'country'):
        """ Address constructor object.

        :param house_number: number of house.
        :type house_number: int
        :param street: name of street.
        :type street: str
        :param city: last name of city.
        :type city: str
        :param state: name of state.
        :type state: str
        :param country: name of the country.
        :type country: str
        :returns: Address object
        :rtype: object
        """
        self._house_number = house_number
        self._street = street
        self._city = city
        self._state = state
        self._country = country

    @property
    def house_number(self) -> int:
        """ Returns house number of the address.
          :returns: house number of address.
          :rtype: int
        """
        return self._house_number

    @house_number.setter
    def house_number(self, house_number: int):
        """ The house numer of the address.
        :param house number: house number of the address.
        :type: int
        """
        self._house_number = house_number

    @property
    def street(self) -> str:
        """ Returns the street of the address.
          :returns: street of address.
          :rtype: str
        """
        return self._street

    @street.setter
    def name(self, street: str):
        """ The street of the address.
        :param street: name of address.
        :type: str
        """
        self._street = street

    @property
    def city(self) -> str:
        """ Returns the city of the address.
          :returns: last city of address.
          :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """ The city of the address.
        : param city: city of address.
        :type: str
        """
        self._city = city

    @property
    def state(self) -> str:
      """ Returns the state of the address.
        :returns: state of address.
        :rtype: str
      """
      return self._state

    @state.setter
    def state(self, state: str):
      """ The state of the address.
      : param state: state of the address
      :type: str
      """
      self.state = state

    @property
    def country(self) -> str:
      """ Returns the country of the address.
        :returns: country of address.
        :rtype: str
      """
      return self._country

    @country.setter
    def country(self, country: str):
      """ The country of the address.
      : param conutry: country of the address
      :type: str
      """
      self.country = country
      
    def __str__(self):
        """ Returns str of address.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.house_number, self.street, self.city, self.state, self.country)