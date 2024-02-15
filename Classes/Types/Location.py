class Latlng:
    lat:float
    lng:float
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
    
    def get_lat(self):
        return self.lat
    
    def get_lng(self):
        return self.lng
    
    def set_lat(self, lat):
        self.lat = lat
        
    def set_lng(self, lng):
        self.lng = lng
    
        
    