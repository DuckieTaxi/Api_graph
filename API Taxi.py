class Cars():
    car_id = 0 # это поле, но если необходимо его можно заменить методом генерации и присваивания метода
    # def car_id(self, parameter_list):
    #     pass
    def car_status(self, car_id):
        pass


class Orders():
                    #поля состояния заказа
    status_InProcess = 0
    status_end = 0
    status_start = 0
    staus_paused = 0
                    #маршрут поездки
    path_start = 0
    path_end = 0
                    #я не понял, что именно надо сделать, я бы реализовал по другому. А так в общем и целом я не уверен, что это то что хотела Татьяна
    def order_manager(self, parameter_car_id, status_InProcess, status_end, status_start, staus_paused):
        pass

class RoadPlan():
    def car_find(self, parameter_graphtop): #parameter_graphtop это аргумент в который передается вершина для которой надо найти авто
        pass
    def car_dierectionPath(self, parameter_path): #нпередаем ему путь
        pass
    def car_send(self, parameter_car_id): #передаем ему id машины
        pass
        
    def order_process(self, parameter_list_of_cars): #здесь мы передаем список всех машин, по идее надо его генерировать, но про метод генерации автомобилей и их списка ничего не было, так что я хз, тип его всегда можно написать вместе с генерацией id автомобиля
        pass
    def order_eventJamProcess(self, parameter_car_postion): #car_position нам возвращает метод car_getPistion класса Graph
        pass
    def path_get(self, parameter_shortest_path): #shortest_path нам возвращает метод shortest_path класса Graph
        pass
    def get_newPath(self, parameter_shortest_path): #shortest_path нам возвращает метод shortest_path класса Graph
        pass
    def path_process(self, parameter_shortest_path): #shortest_path нам возвращает метод shortest_path класса Graph
        pass

class Graph():
    def path_getAll(self, parameter_start, parameter_end): # end и start это вершины начала и конца пути
        pass
    def path_shortest(self, parameter_list_of_paths): #list_of_paths это аргумент, который нам возвращает метод getAll
        pass

    def car_getPosition(self, parameter_car_id): #car_id id авто, но тут есть загвоздка, реализация тут завязана не только на id, по идее нам надо будет обратиться к менджеру заказов и к ядру, чтоб точно понять на каком она пути, но для этого нужен ток id
        pass

class Core():
    def core_getPath(self, parameter_top): #top аргумент который нам возвращает метод car_directionPath  в классе Roadplan
        pass
    def core_pathEnd(self, parameter_end_top): #end_top мы уже задавали, это конец вершины, но на самом деле я не до конца понимаю смысл этого метода, но если Татьяна сказала, что нужен, пусть будет
        pass