

class Searching_module:
    #search_counter = 0
    API_KEY = 'insert_api_key_here'

    def __init__(self, current_location = None):
        self.m_object_list = []
        if current_location:
            self.m_object_list[0] = current_location
    
    def convert_miles_to_meters (miles):
        pass

    def get_m_object_list(self):
        return self.m_object_list
        
    def set_m_object_list(self,list):
        self.m_object_list = list

    def remove_old_objects(self):
        self.m_object_list = []

    #def start_searching_module(self, input_location = None, input_radius = None):
    #    map_client = googlemaps.Client(API_KEY)
    #   if -90 > input_location[0] > 90 or 180 < input_location[1] < -180:
    #        return -1
    #    if input_location:
    #        response = map_client.places_nearby (location = input_location, radius = input_radius)
    #    else:
    #        return -2

    def search_the_area(coordinates, radius, category, subcategory):
        pass
    def prepare_search_result (self, params):
        pass
