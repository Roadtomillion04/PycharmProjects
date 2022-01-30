class Bill(object):
    """
    Object that contains data about bill,
    that is amount and period(mm/yyyy)
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate(object):
    """
    Stores a flatmate details and calculates
    the share of the bill
    """

    def __init__(self, name, day_in_house):
        self.name = name
        self.day_in_house = day_in_house

    def pays(self, bill: Bill, flatmates: list):
        days_stayed = []
        for flatmate in flatmates: # appends given flatmates day_in_house
            days_stayed.append(flatmate.day_in_house)

        '''formula - value / sum all values'''
        weight = self.day_in_house / (self.day_in_house + sum(days_stayed))
        to_pay = weight * bill.amount
        return to_pay