from models.Movie import Movie
from models.Backpack import Backpack, my_backpack as backpack 
#from models.Circle import Counter
def main():
    movie = Movie("Inception", 2010, 3.0)

    # Acceso a atributos públicos
    print(movie.title) 
    print(movie.year)  

    # Acceso al atributo privado (correcto)
    print(movie.rating)

    # Modificar atributo privado
    movie.rating = 5.0
    print(movie.rating)

    # Acceso a atributos
    print("Backpack model")
    print(backpack.color)
    
    # Modificar atributo privado
    backpack.multiple_items(["water", "laptop", "book", "notebook", "pen","backpack"])
    backpack.count_my_items()

 
    backpack.show_items(True)
    print(f"Items en mi mochila: {backpack.items}")

    input("Press Enter to continue...")
    backpack.remove_item("backpack")
    print(f"Items en mi mochila: {backpack.items}")
    print(f"Tengo {backpack.count_my_items()} items en mi mochila")

    input("Press Enter to continue...")
    backpack.remove_item("water")
    print(f"Items en mi mochila: {backpack.items}")
    print(f"Tengo {backpack.count_my_items()} items en mi mochila")

    string_1 = "Hello, World!"
    string_2 = "Hello, World!"

    a = [1,2,3]
    b = a
 
    print(string_1 is string_2)
    print(f" {a.id() }")

 
if __name__ == "__main__":
    main()