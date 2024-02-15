from typing import List

from Classes.User import Customer,Restaurant,Rider
from Helper.Scheduler import Scheduler
from Classes.Types.Order import Order
from Classes.Types.Location import Latlng
from Helper.PathFinder import PathFinder

def main():
            # .with_orders([ order2])\


    # Example usage for creating a Restaurant
    r1 = Restaurant.Builder(name="Pizza Place", type="restaurant")\
        .with_id(1)\
        .with_location(Latlng(lat=51.7749, lng=31.4194))\
        .build()
        
    r2 = Restaurant.Builder(name="Momo Place", type="restaurant")\
        .with_id(2)\
        .with_location(Latlng(lat=55.7749, lng=35.4194))\
        .build()

    # Example usage for creating a Customer
    c1 = Customer.Builder(name="Jack Doe", type="customer")\
        .with_id(1)\
        .with_location(Latlng(lat=72.7749, lng=71.4194))\
        .build()
    
    c2 = Customer.Builder(name="Jane Doe", type="customer")\
        .with_id(2)\
        .with_location(Latlng(lat=74.7749, lng=70.4194))\
        .build()
    
    orders = []
    order1 = Order.Builder(id=1).with_placed_at(r1)\
    .with_placed_by(c1)\
    .build()

    order2 = Order.Builder(1)\
    .with_placed_at(r2)\
    .with_placed_by(c2)\
    .build()
        
    orders.append(order1)
    orders.append(order2)
    
    rider_aman = Rider.Builder(name="Rider Aman", type="rider")\
    .with_id(1)\
    .with_current_location(Latlng(lat=37.7749, lng=38.4194))\
    .build()
    # .with_deliveries([order1, order2])\
    
    scheduler  = Scheduler()
    scheduler.get_scheduler(PathFinder.branch_and_bound)
    scheduler.get_optimal_path(orders=orders,rider=rider_aman)
    scheduler.display_path()
    
    
        

if __name__ == "__main__":
    main()