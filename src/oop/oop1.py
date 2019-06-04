# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
# 
# Put a comment noting which class is the base class

#ask to explaine base class


#Vehicle
class Vehicle:
  pass

#Vehicle
class FlightVehicle(Vehicle):
  pass

#Flight Vehicle
class Starship(FlightVehicle):
  pass

#Vechile
class GroundVehicle(Vehicle):
    pass

#GroundVehicle
class Car(GroundVehicle):
  pass
#GroundVehicle
class Motorcycle(GroundVehicle):
  pass
#FlightVehicle
class Airplane(FlightVehicle):
  pass

