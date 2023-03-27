

class Receipt(object):
    """
    Class used to represent a Receipt
    """

    def __init__(self, id_receipt: int = 0, cost: float = 0.0, cash: float = 0, change: float = 0, product: str = "product", payment_method: str = "payment_method"):
        """ Receipt constructor object.

        :param id_receipt: id of receipt.
        :type id_receipt: int
        :param cost: cost of receipt.
        :type cost: float
        :param cash: cash of receipt.
        :type cash: float
        :param change: change of receipt.
        :type change: float
        :param product: product to deliver
        :type product: object
        :param payment_method: payment method of receipt
        :tyoe payment_method: str
        :returns: Person: object
        :rtype: Person
        """
        self._id_receipt = id_receipt
        self._cost = cost
        self._cash = cash
        self._change = change
        self._product = product
        self._payment_method = payment_method

    @property
    def id_receipt(self) -> int:
        """
        Returns id receipt of the receipt.
          :returns: id of receipt.
          :rtype: int
        """
        return self._id_receipt

    @id_receipt.setter
    def id_receipt(self, id_receipt: int):
        """
        The id of the receipt.
        :param id_receipt: id of receipt.
        :type: int
        """
        self._id_receipt = id_receipt

    @property
    def cost(self) -> float:
        """
        Returns the cost of the receipt.
          :returns: cost of receipt.
          :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost: float):
        """
        The cost of the receipt.
        :param cost: cost of receipt.
        :type: float
        """
        self._cost = cost

    @property
    def cash(self) -> float:
        """
        Returns the cash of receipt.
          :returns: cash of receipt.
          :rtype: float
        """
        return self._cash

    @cash.setter
    def cash(self, cash: float):
        """
        The cash of the receipt.
        :param cash: cash of receipt.
        :type: float
        """
        self._cash = cash

    @property
    def change(self) -> float:
      """
      Returns the change of the receipt.
        :returns: change of receipt.
        :rtype: float
      """
      return self._change

    @change.setter
    def change(self, change: float):
      """
      The change of the receipt.
      :param change: change of the receipt
      :type: float
      """
      self.change = change

    @property
    def object(self) -> str:
      """
      Returns the object of the receipt.
        :returns: object of receipt.
        :rtype: object
      """
      return self._object

    @object.setter
    def object(self, object: object):
      """
      The object of the receipt.
      :param object: object of the receipt
      :type: object
      """
      self.object = object
  
    @property
    def payment_method(self) -> str:
      """
      Returns the payment_method of the receipt.
        :returns: payment method of receipt.
        :rtype: str
      """
      return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
      """
      The payment_method of the receipt.
      :param payment method: payment method of the receipt
      :type: str
      """
      self.payment_method = payment_method

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.id_receipt, self.cost, self.cash, self.change, self.product, self.payment_method)

    if __name__ == 'Receipt':
        receipt1 = Receipt(id_receipt=1006875342, cost=100000, cash=100000, change=0, product="Silla", payment_method="Tarjeta de credito")
        receipt1.name = "Receipt1"
        print(receipt1)

        receipt2 = Receipt()
        print(receipt2)

