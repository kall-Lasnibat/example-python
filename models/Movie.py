class Movie:
    
    def __init__(self, title, year, rating):
        # Atributos públicos
        self.title = title
        self.year = year
        # Atributo privado (name mangling)
        self.__rating = rating

    @property  
    def rating(self):
        print("Getting rating")
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 0 <= new_rating <= 5.0:
            self.__rating = new_rating
        else:
            print("Rating debe estar entre 0 y 5.0")