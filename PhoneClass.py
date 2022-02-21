

from re import M


class Phone:
    def  __init__ (self,manu,model,price):
       self.__manufact = manu 
       self.__model_ = model
       self.__retail_price = price
    
    def set_manufact(self, manu):
        self.__manufact = manu
   
    def set_model(self, model):
        self.__model_ = model

    def set_retail_price(self, price):
        self.__retail_price = price
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model_

    def get_retail_price(self):
        return self.__retail_price




