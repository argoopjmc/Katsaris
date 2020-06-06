#Defining a custom class which can be adopted later if needed
class CustomClass:
  
  # specify attributes to prevent dynamic creation
  __slots__ = ['field1','field2','field3']

  
  def __init__(self,field1,field2,field3) -> None:
    self.field1 = field1
    self.field2 = field2
    self.field3 = field3
    

  def __getter__(self):
    return(self.field1,self.field2,self.field3)
