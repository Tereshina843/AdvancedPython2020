
class PrintParameters(Exception):
    pass

class Handler:
    def __init__(self):
        self.elements = list()
        self.value_mean = 0
        self.value_disp = 0

    def calc_mean_for_new(self, new_elem):
        return (self.value_mean * len(self.elements) + new_elem) / (len(self.elements) + 1)

    def calc_disp_for_new(self, new_elem):
        disp = 0

        for elem in self.elements:
            disp += ((elem - self.value_mean) ** 2) / (len(self.elements) + 1)
        disp += ((new_elem - self.value_mean) ** 2) / (len(self.elements) + 1)
        return disp


    def coroytine_for_update(self):
        print("Starting coroutine\n")
        try:
            while True:
                try:
                    new_elem = yield

                    self.value_mean = self.calc_mean_for_new(new_elem)
                    self.value_disp = self.calc_disp_for_new(new_elem)

                    self.elements.append(new_elem)

                except PrintParameters:
                    yield len(self.elements), self.value_mean, self.value_disp
        finally:
            print("\nStop coroutine")


# Чтобы не вводить из консоли, сделаем массив из команд, которые "пришли" от устройства
commands_imitation = [[7, 3, 2, 8, 10], "Print"]

handler = Handler()
coroytine = handler.coroytine_for_update()

next(coroytine)

for command in commands_imitation:

    if isinstance(command, list):
        for elem in command:
            coroytine.send(elem)
    else:
        params = coroytine.throw(PrintParameters)


        print("____PARAMETERS___")
        print("Quantity:\t", params[0])
        print("Mean value:\t", params[1])
        print("Mean value:\t", params[2])


coroytine.close()
