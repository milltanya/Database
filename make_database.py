import create
import filling
import os
os.remove("Transport.db")
create.create_database()
filling.fill_route()
filling.fill_card()
filling.fill_concrete_card()
filling.fill_trip()
filling.fill_station()
filling.fill_route_station()
filling.fill_route_shift()
filling.fill_route_schedule()
filling.fill_model()
filling.fill_vehicle()
filling.fill_driver()
filling.fill_driver_shift()
filling.fill_driver_schedule()
