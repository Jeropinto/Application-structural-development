class Package(object):
    """
    Class used to represent an Package
    """

    def __init__(self, id_package: int = 0, weight: float = 0.1, description: str = "description", cost: float = 0, w_gr_100: float = 1.0):
        """ package constructor object.

        :param id_package: id of package.
        :type id_package: int
        :param weight: weight of package.
        :type weight: float
        :param description: description of package.
        :type description: str
        :param cost: cost of package.
        :type cost: float
        :param w_gr_100: gr limit of package 
        :type w_gr_100: float
        :returns: Package object
        :rtype: object
        """
        if (weight < w_gr_100):
          Standar_package(self, id_package, weight, description, cost, w_gr_100)
        else:
          Overweight_package
        self._id_package = id_package
        if (weight < 0):
          self._weight = 1.0
        self._weight = weight
        self._description = description
        self._cost = cost
        self._w_gr_100 = w_gr_100
        

    @property
    def id_package(self) -> int:
        """ Returns id package of the package.
          :returns: id of package.
          :rtype: int
        """
        return self._id_package

    @id_package.setter
    def id_package(self, id_package: int):
        """ The id of the package.
        :param id_package: id of package.
        :type: int
        """
        self._id_package = id_package

    @property
    def weight(self) -> float:
        """ Returns the weight of the package.
          :returns: weight of package.
          :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """ The weight of the package.
        :param name: weight of package.
        :type: float
        """
        self._weight = weight

    @property
    def description(self) -> str:
        """ Returns the description of the package.
          :returns: desciption of package.
          :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """ The description of the package.
        : param description: description of package.
        :type: str
        """
        self._description = description

    @property
    def cost(self) -> float:
      """ Returns the cost of the package.
        :returns: cost of package.
        :rtype: float
      """
      return self._cost

    @cost.setter
    def cost(self, cost: float):
      """ The cost of the package.
      : param cost: cost of the package
      :type: float
      """
      self.cost = cost

    @property
    def w_gr_100(self) -> float:
      """ Returns the w_gr_100 of the package.
        :returns: w_gr_100 of package.
        :rtype: float
      """
      return self._w_gr_100

    @w_gr_100.setter
    def w_gr_100(self, w_gr_100: float):
      """ The w_gr_100 of the package.
      : param cost: w_gr_100 of the package
      :type: float
      """
      self.w_gr_100 = w_gr_100 

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_package, self.weight, self.description, self.cost, self.w_gr_100)

class Standar_package(Package):
  def __init__(self, id_package: int = 0, weight: float = 0.1, description: str = "description", cost: float = 0, w_gr_100: float = 1.0):
    Package.__init__(self, id_package, weight, description, cost, w_gr_100)

class Overwight_package(Package):
  def __init__(self, id_package: int = 0, weight: float = 0.1, description: str = "description", cost: float = 0, w_gr_100: float = 1.0, overweight: float = 0.0):
    super().__init__(self, id_package, weight, description, cost, w_gr_100)
    if (overweight < 0):
      overweight = 0.1
    self.overweight = overweight
    