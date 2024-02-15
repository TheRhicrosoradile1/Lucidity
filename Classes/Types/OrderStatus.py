from enum import Enum

class OrderStatus(Enum):
    PENDING = 0
    RECIEVED = 1
    PREPARED = 2
    PICKED = 3
    DELIVERED = 4
    REJECTED = 5
    