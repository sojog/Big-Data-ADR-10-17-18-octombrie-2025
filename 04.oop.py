""" Aceasta este o documentatie a modului
"""

## Definitia unei clasei - CONVENTIE (incepe cu litera mare)
class Student:
    """ Aici este o documentatie -
    trebuie pusa pe prima linie a clasei
    """
    ## constructor (initializator)
    ## FUNCTIILE cu "__" sunt functii magice 
    def __init__(self, var):
        self.varsta =  var

    def __str__(self):
        return f"Studentul are varsta de {self.varsta} ani"

    ## O functie in clasa - metoda
    ## self - echivalent cu this din alte limbaj
    def este_adult(self):
        """ Aceasta este o documentatie a metodie(functie)
        """
        if vasta > 18:
            return True
        else:
            return False


obiect = Student(33)
print(obiect)
print(Student.__doc__) ## __doc__ -> documentatie