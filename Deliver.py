from Person import Person
from Address import Address
from Package import Package
from Receipt import Receipt


class Deliver(object):
    """
    Class used to represent an Deliver
    """

    def __init__(self, id_deliver: int = 0, date_d: int = 0, date_m: int = 0, date_y: int = 0, time: float = 0.0, sender: Person = Person.__init__(), receiver: Person = Person.__init__(), sender_add: Address = Address.__init__(), receiver_add: Address = Address.__init__(), contact: Person = Person.__init__(), items: Package = Package.__init__(), receipt: Receipt = Receipt.__init__()):
        """ Deliver constructor object.

        :param id_deliver: id of Deliver.
        :type id_deliver: int
        :param date_d: number of day.
        :type date_d: int
        :param date_m: number of month.
        :type date_m: int
        :param date_y: number of year.
        :type date_y: int
        :param time: time passed since deliver.
        :type time: float
        :param sender: Person that sending deliver.
        :type sender: object
        :param receiver: Person that receives deliver.
        :type receiver: object
        :param sender_add: adress of sender.
        :type sender_add: object
        :param receiver_add: address of receiver.
        :type receiver_add: object
        :param contact: contact of person.
        :type contact: int
        :param items: items carried of package.
        :type items: object
        :param receipt: receipt of the deliver.
        :tpye receipt: object
        :returns: Deliver object
        :rtype: object
        """
        self._id_deliver = id_deliver
        self._date_d = date_d
        self._date_m = date_m
        self._date_y = date_y
        self._time = time
        self._sender = sender
        self._receiver = receiver
        self._sender_add = sender_add
        self._receiver_add = receiver_add
        self._contact = contact
        self._receipt = receipt

    @property
    def id_deliver(self) -> int:
        """ Returns id deliver of the deliver.
          :returns: id of deliver.
          :rtype: int
        """
        return self._id_deliver

    @id_deliver.setter
    def id_deliver(self, id_deliver: int):
        """ The id of the deliver.
        :param id_deliver: id of deliver.
        :type: int
        """
        self._id_deliver = id_deliver

    @property
    def date_d(self) -> int:
        """ Returns the day of the deliver.
          :returns: day of deliver.
          :rtype: int
        """
        return self._date_d

    @date_d.setter
    def date_d(self, date_d: int):
        """ The day of the deliver.
        :param date_d: day of deliver.
        :type: int
        """
        self._date_d = date_d

    @property
    def date_m(self) -> int:
      """ Returns the month of the deliver.
        :returns: month of deliver.
        :rtyoe: int
      """
      return self.date_m
      
    @date_m.setter
    def date_m(self, date_m: int):
      """ The month of the deliver.
        :param date_m: month of deliver.
        :type: int
      """
      self._date_m = date_m

    @property
    def date_y(self) -> int:
      """ Returns the year of the deliver.
        :returns: year of deliver.
        :rtyoe: int
      """
      return self.date_y
      
    @date_y.setter
    def date_y(self, date_y: int):
      """ The year of the deliver.
        :param date_y: year of deliver.
        :type: int
      """
      self._date_y = date_y
      
    @property
    def time(self) -> float:
        """ Returns the time of the deliver.
          :returns: time of deliver.
          :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time: float):
        """ The time of the deliver.
        : param time: time of deliver.
        :type: float
        """
        self._time = time

    @property
    def sender(self) -> object:
        """ Returns the sender of the deliver.
          :returns: sender of deliver.
          :rtype: object
        """
        return self._sender

    @sender.setter
    def sender(self, sender: object):
        """ The sender of the receiver.
        :param sender: sender of receiver.
        :type: object
        """
        self._sender = sender

    @property
    def receiver(self) -> object:
        """ Returns the receiver of the receiver.
          :returns: receiver of deliver.
          :rtype: object
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: object):
        """ The receiver of the deliver.
        :param receiver: receiver of deliver.
        :type: object
        """
        self._receiver = receiver

    @property
    def sender_add(self) -> object:
        """ Returns the sender address of the deliver.
          :returns: sender address of deliver.
          :rtype: object
        """
        return self._sender_add

    @sender_add.setter
    def sender_add(self, sender_add: object):
        """ The sender address of the deliver.
        : param sender_add: sender address of deliver.
        :type: object
        """
        self._sender_add = sender_add

    @property
    def receiver_add(self) -> object:
        """ Returns the receiver address of the deliver.
          :returns: receiver address of deliver.
          :rtype: object
        """
        return self._receiver_add

    @receiver_add.setter
    def sender_add(self, receiver_add: object):
        """ The receiver address of the deliver.
        : param receiver_add: receiver address of deliver.
        :type: object
        """
        self._receiver_add = receiver_add

    @property
    def contact(self) -> int:
        """ Returns the contact of the person.
          :returns: contact address of person.
          :rtype: int
        """
        return self._contact 

    @contact.setter
    def contact(self, contact: int):
        """ The contact of the person.
        : param contact: contact of person.
        :type: int
        """
        self._contact = contact

    @property
    def package(self) -> object:
        """ Returns the package of the deliver.
          :returns: package of deliver.
          :rtype: object
        """
        return self._package

    @package.setter
    def paclkage(self, package: object):
        """ The package of the deliver.
        :param package: 'package' of deliver.
        :type: object
        """
        self._package = package
  
    @property
    def receipt(self) -> object:
        """ Returns the receipt of the deliver.
          :returns: receipt of deliver.
          :rtype: object
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt: object):
        """ The receipt of the deliver.
        :param receipt: receipt of deliver.
        :type: object
        """
        self._receipt = receipt
  
    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
      
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8} ,{9}, {10}, {11})'.format(self.id_deliver, self.date_d, self.date_m, self.date_y, self.time, self.sender, self.receiver, self.sender_add, self.receiver_add, self.contact, self.package, self.receipt)