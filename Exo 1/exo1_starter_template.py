import time, sys

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
  # Constructeur
    def __init__(self, name):
        self.name = name
        #self.power = False
        #self.current_speed = 0
        #self.battery_level = 0

  # Destructeur
  #  def __del__(self): 
  #      print("je suis le destructeur")
  #      self.clear()
  
  
  ### Get/Set ###

  # Name getter function 
    @property
    def name(self): 
         #print("getter method called") 
         return self.__name
       
  # Name setter function 
    @name.setter
    def name(self, a): 
         #print("setter method called") 
         self.__name = a 

  # Power getter function 
    @property
    def power(self): 
         #print("getter method called") 
         return self.__power
       
  # Power setter function 
    @power.setter
    def power(self, a): 
         #print("setter method called") 
         self.__power = a 

  # current_speed getter function 
    @property
    def current_speed(self): 
         #print("getter method called") 
         return self.__current_speed

  # Power setter function 
    @current_speed.setter
    def current_speed(self, a): 
         #print("setter method called") 
         self.__current_speed = a 

  # battery_level getter function 
    @property
    def battery_level(self): 
         #print("getter method called") 
         return self.__battery_level    
  
  # battery_level setter function 
    @battery_level.setter 
    def battery_level(self, a): 
         #print("setter method called") 
        ## The maximum charge need to be 100% otherwise quit
         if(a > 100):
              return
         else :
              self.__battery_level = a

  # State robot getter function 
    @property
    def states(self): 
         ## If the power is off return a shutdown state
         #print("getter method called") 
         if (self.power == False):
              return self.__states[0]
         ## else If the power is on return a running state
         elif (self.power == True):
              return self.__states[1]
         
  #Méthode qui va retourner toutes les info d'un robot sous format string
    def __str__(self):
        return "Nom du robot : {}, état Allumé  : {} / Current speed: {} / Battery level : {} / état robot : {} ".format(self.name, self.power, self.current_speed, self.battery_level, self.states)

    
    def rechargement(self):
        i = 0
        while i < 100 :
          i = i+1
          self.battery_level = i
          time.sleep(0.1)
          print("La recharge de la batterrie est a : {}%".format(self.battery_level))
    
    def stop(self):
         self.current_speed = 0