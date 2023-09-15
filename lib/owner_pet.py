class Pet:
    #defining a class variable of all pet types
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    #all class variable to keep track of every pet instance of Pet class
    all = []

    def __init__(self, name, pet_type, owner= None):
        self.name = name
        Pet.all.append(self) #every time an instance is created it gets added to all
        #class variable
        self.pet_type = pet_type
        self.owner = owner
    
    @property 
    def pet_type(self): #gets the pet_type of self
        return self._pet_type
    
    @pet_type.setter # setting pet type
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES: #checks if passed pet_type is not one of the accepted pet types
            raise Exception("Not a vaid pet type.") #raises an exception for their input
        self._pet_type = pet_type #if it is one of the pet types then it sets the objs pet type to pet_type
    
    @property
    def owner(self): #gets the owner of self
        return self._owner
    
    @owner.setter #sets owner
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner): #checks if owner is not an instance of Owner class
            raise Exception("Input is not a valid Owner type") #raised exception for their input
        self._owner = owner # if it is sets the owner of that object to the passed in owner
        


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self): #method to return the pet if its an instance stored in Pet class all list
        return [pet for pet in Pet.all if pet.owner == self] #returns the pet if the owner is self
    
    def add_pet(self, pet): #method to add pet
        if isinstance(pet, Pet): #checks if pet is an instance of Pet
            pet.owner = self   #if it is then sets the owner to self
        else:
            raise Exception("Input is not a valid Pet type") #raise exceptiong if not
       
    
    def get_sorted_pets(self): # method to return list of pets sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)
    # sorting our owners (self) pets from pets() with  a specific key of pet 
    #lambda creates an inline function that returns pet.name as the key