import datetime

class Apex_Categories:
    def __init__(self, tier1, tier2, tier3):
        """
        :param tier1: main group
        :param tier2: sub group
        :param tier3: base group
        """
        self.tier1 = tier1
        self.tier2 = tier2
        self.tier3 = tier3

class Apex_Codes:
    code_count = 0  # this counts the number of different types of objects you have created


    def __init__(self, stock_code, description, brand, tiers):
        """
        :param stock_code: identifier for the product
        :param description: description of the product
        :param brand: manufacturer of the product
        :param tiers: groups into which the products are in
        """
        self.stock_code = stock_code
        self.description = description
        self.brand = brand
        self.tiers = tiers
        self.total_stock = 0
        self.batches = []  # I have created batches as a list, you'll understand in a second
        self.batch_history = []

        Apex_Codes.code_count += 1  # Each time you create a new object I keep track of the count


    def add_batch(self, batch_code, quantity, date_added=datetime.datetime.today()):
        """
        :param batch_code: batch code as a string or integer
        :param quantity: quantity of the batch as an integer
        :param date_added: year-month-day date the batch was added
        :return: no return
        """
        if type(date_added)==str:
            date_added = datetime.datetime.strptime(date_added, "%Y-%m-%d").date()
        if batch_code not in [i[0] for i in self.batches] and batch_code not in [i[0] for i in self.batch_history]:
            # above, check if the batch is already rung through or is already there
            self.batches.append(batch_code, quantity, date_added) # i made this a tuple to simplify
            self.total_stock += quantity
            if datetime.datetime.today() != date_added:
                self.batches.sort(key=lambda i: i[-1])
        else:
            print("batch already exists, or was used up. Don't cook the books")


    def consume_stock(self, quantity, batch_code = -1):
        """
        :param quantity: the amount that is being consumed
        :param batch_code: what batch is it being consumed from, if you skip this param, then it is consumed from the oldest batch
        :return: remaining quantity in batch
        """
        consumed = False
        if batch_code.is_integer() and batch_code == -1:
            while not consumed:
                self.batches[0] = self.batches[0][0], self.batches[0][1] - quantity, self.batches[0][2]
                if self.batches[0][1] <= 0:
                    quantity = 0 - self.batches[0][1]
                    self.batch_history.append((self.batches[0][0], self.batches[0][2], datetime.datetime.today()))
                    # above i am saving this batch and when it was consumed and emptied
                    self.batches.pop(0)  # deletes the empty batch
                else:
                    consumed = True
        else:
            # add error handling is batch does not exist
            if batch_code not in [i[0] for i in self.batches]:
                self.consume_stock(quantity)
                return
            loc_batch = [i[0] for i in self.batches].index(batch_code)
            # above, find the location of the requested batch
            self.batches[loc_batch] = (self.batches[loc_batch][0],
                                       self.batches[loc_batch][1] - quantity,
                                       self.batches[loc_batch][2])
            if self.batches[loc_batch][1] <= 0:
                quantity = 0 - self.batches[loc_batch][1]
                self.batch_history.append((self.batches[loc_batch][0], self.batches[loc_batch][2],  datetime.datetime.today()))
                self.batches.pop(loc_batch)
                self.consume_stock(quantity)
                return

energade = Apex_Codes(stock_code="AP19368",
                      description="Energade - Blueberry 24x500ml",
                      brand="Energade",
                      tiers=Apex_Categories(tier1="Sports & Energy",
                                            tier2="Cold Beverages",
                                            tier3="Beverages"))
