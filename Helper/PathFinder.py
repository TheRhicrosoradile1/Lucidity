from typing import List
from sys import maxsize 
from itertools import permutations
from  math import radians, sin, cos, sqrt, atan2,ceil
from Classes.User import Rider,Customer,Restaurant
from Classes.Types.Order import Order
from Classes.Types.Location import Latlng


class PathFinder:
    
    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        radius_earth_km = 6371  # Radius of the Earth in kilometers
        distance = radius_earth_km * c

        return distance
    
    @staticmethod
    def dynamic_program_path(orders:List[Order],rider:Rider):
        pass
        
    def branch_and_bound(orders:List[Order],rider:Rider):
        restaurant_list =set()
        customer_list = []
        restaurant_to_customer = {}
        timer = 0

        for order in orders:
            customer_list.append(order.placed_by)
            restaurant_list.add(order.placed_at)
            restaurant_to_customer.setdefault(order.get_placed_at().get_name(), []).append(order.get_placed_by())

        if len(restaurant_list)==0:
            print("no resturant selected")
            return [],0
        if len(customer_list)==0:
            print("no customer selected")
            return [],0
            
        # for key,value in restaurant_to_customer.items():
        #     print("resturant : ",key)
        #     for v in value:
        #         print("        ",v.get_name())
        # print("")

        path = []
        curr_min = float('inf')

        next_node = None
        print(f"resturant length : {len(restaurant_list)}")
        restaurant_list = list(restaurant_list)
        for restaurant in restaurant_list:
            curr = PathFinder.haversine(rider.current_location.lat,rider.current_location.lng,restaurant.get_location().lat,restaurant.get_location().lng)/25
            curr = curr*3600
            if curr<curr_min:
                print(f"restaurant {restaurant.get_name()} time - {curr}")
                curr_min = curr
                next_node = restaurant
        timer+=curr_min
        restaurant_list.remove(next_node)
        
        path.append(next_node.name)
        path.append(timer)
        
        
        rider.current_location = next_node.location
        rider.deliveries.extend(restaurant_to_customer[next_node.get_name()])
        

        while len(restaurant_list) or len(rider.deliveries):
            ## find nearest resturant
            print(f"resturant left : {len(restaurant_list)}")
            print(f"deliver left : {len(rider.deliveries)}")
            curr_min = float('inf')
            next_node = None
               
            for restaurant in restaurant_list:
                curr = PathFinder.haversine(rider.current_location.lat,rider.current_location.lng,restaurant.get_location().lat,restaurant.get_location().lng)/25
                curr = curr*3600
                print(f"restaurant {restaurant.get_name()} time - {curr}")
                if curr<curr_min:
                    curr_min = curr
                    next_node = restaurant
            
            ## find nearest customer if have picked order
            for delivery in rider.deliveries:
                curr = PathFinder.haversine(rider.current_location.lat,rider.current_location.lng,delivery.get_location().lat,delivery.get_location().lng)/25
                curr = curr*3600
                print(f"customer {delivery.get_name()} time - {curr}")
                if curr<curr_min:
                    curr_min = curr
                    next_node = delivery
            
            path.append(next_node.name)
            timer+=curr_min
            path.append(timer)
            rider.current_location = next_node.location
            
            if isinstance(next_node, Restaurant):
                restaurant_list.remove(next_node)
                rider.deliveries.extend(restaurant_to_customer[next_node.get_name()])
            else :
                rider.deliveries.remove(next_node)
            print()
        return path,timer