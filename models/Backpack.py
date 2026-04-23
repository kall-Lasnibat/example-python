class Backpack:

    def __init__(self,color = "black"):
        self._items = []
        self.color = color

    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Items debe ser una lista")

    @items.deleter
    def items(self):
        self._items = []
        print("Items eliminados")

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Item debe ser una cadena de texto")

    def multiple_items(self, items):
        for item in items:
            count = 0
            len_items = len(items)
            if isinstance(item, str):
                count = +1
                self.add_item(item)
                if len_items == count:
                    print(f"Item {item} agregado a mi mochila")
            else:
                print("Item debe ser una cadena de texto")

    def remove_item(self, item):
        if isinstance(item, str) and item in self._items:
            self._items.remove(item)
            print(f"Item {item} eliminado de mi mochila")
        else:
            print("Item debe ser una cadena de texto y debe existir en la mochila")

    def has_item(self, item):
        if isinstance(item, str) and item in self._items:
            return 1
        else:
            return 0

    def show_items(self, sort = False):
        if sort:
            self._items.sort()
            print(self._items)
            return self._items
        else:
            return self._items

    def count_my_items(self):
        count = len(self._items) #len() es una función que devuelve el número de elementos en una lista
        print(f"Tengo {count} items en mi mochila")
        return count

my_backpack = Backpack()

 