"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    pass
    # def __init__(self, message):
    #     self.message = message
    # def __str__(self):
    #     return str(self.message)

    # def __str__(self):
    #     print('Calling str')
    #     if self.message:
    #         return 'LowFuelError,{0} '.format(self.message)
    #     else:
    #         return  'LowFuelError has been raised'


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
