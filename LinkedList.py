#from _typeshed import Self
from abc import abstractmethod
from Node import Node 
class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0
    
    def agrega(self,Value):
        mnodo = Node(Value)
        if self.Size == 0 :
            self.First = mnodo
        else:
            ahora = self.First
            while ahora.Next != None:
                ahora = ahora.Next
            ahora.Next = mnodo
        
        self.Size += 1
        return mnodo

    def __len__(self):
        return self.Size

    def __str__(self):
        S = "["
        ahora = self.First
        while ahora != None:
            S += str(ahora)
            if ahora.Next != None:
             S+=", "
            ahora = ahora.Next
        S+="]"
        return S
    def limpia(self):
        self.First = None
        self.Size = 0


    """def verif(self, nombre):
        
        S = "["
        ahora = self.First
        while ahora != None:
            
            
            if str(ahora) == nombre:
                print(nombre+str(ahora))
                S += str(ahora)+", "
                ahora = ahora.Next

                while ahora != None and -1 == str(ahora).find("terreno") :
                  S += str(ahora)
                 
                  #print(int(ahora)[0]*200)
                  if ahora.Next != None:
                   S+=", "
                  ahora = ahora.Next
                S+="]"
            if ahora!= None:
             ahora = ahora.Next
        return S
    """
    def vuelve(self):
        return self.First.Next





 