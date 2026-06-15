from address import Address
from mailing import Mailing

from_address = Address("445621", "Барнаул", "Ленина", "10", "1")
to_address = Address("124500", "Санкт-Петербург", "Невский", "20", "2")

my_mailing = Mailing(to_address, from_address, 650, '666666')

print(my_mailing)
