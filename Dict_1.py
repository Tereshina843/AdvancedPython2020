
DICT_MINSIZE = 8


class Object:
    def __init__(self, in_key=None, in_value=None):
        self.key = in_key
        self.value = in_value

        self.deleted = False

    def delete(self):
        self.deleted = True
        self.value = None


class Dictionary:
    def __init__(self, **init_data):
        self.storage = [None] * DICT_MINSIZE

        # Parameters
        self.max_size = DICT_MINSIZE
        self.used_count = 0

        for key, value in init_data.items():
            self.__setitem__(key, value)


    def __setitem__(self, key, value):
        if self.used_count / self.max_size > 0.66:  # Если заполнен, расширяем
            self.expand_dict()

        hash_key = self.get_hash(key)
        our_object = Object(key, value)
        self.storage[hash_key] = our_object

        self.used_count += 1


    def __getitem__(self, key):
        hash_key = self.get_hash(key)

        if hash_key != None:
            value = self.storage[hash_key]
            return value
        else:
            return None

    def __delitem__(self, key):
        hash_key = self.get_hash(key)
        self.storage[hash_key].delete()
        self.used_count-=1


    def __str__(self):
        output_string = "{\n"


        for obj in self.storage:
            if obj:
                if not obj.deleted:
                    output_string += "  \'" + str(obj.key) + "\' : \'" + str(obj.value) + "\',\n"

        output_string += "}"
        return output_string


    def __add__(self, other):
        if isinstance(other, dict):
            for key in other:
                self.__setitem__(key, other[key])
        elif isinstance(other, Dictionary):
            for obj in other.storage:
                if obj != None:
                    self.__setitem__(obj.key, obj.value)

        return self




    def expand_dict(self):
        self.max_size *= 4
        temp_storage = []


        for obj in self.storage:
            if obj:
                temp_storage.append(obj)


        self.used_count = 0
        self.storage = [None] * self.max_size


        for obj in temp_storage:
            self.__setitem__(obj.key, obj.value)


    def get_hash(self, key):
        key_hash = hash(key) % self.max_size
        i = 1


        while (True):
            if self.storage[key_hash] == None: break
            if self.storage[key_hash].key == key: break
            if self.storage[key_hash].deleted: break


            key_hash = (hash(key) + i) % self.max_size
            i += 1

        return key_hash


