class Classroom:
    '''
    Class for classroom representation.
    '''

    def __init__(self, number, capacity, equipment):
        '''
        (Classroom, str, int, list) -> Nontype
        Initializes a classroom with such papameters:
        number, capacity, equipment.
        '''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        '''
        Returns certain text (str).
        '''
        equip_str = ', '.join(self.equipment)
        return f'Classroom {self.number} has a capacity of {self.capacity} \
persons and has the following equipment: {equip_str}.'

    def is_larger(self, other):
        '''
        (Classroom, Classroom) -> (bool)
        Returns True if first room's capacity is larger than
        the second room's and False otherwise.
        '''
        return self.capacity > other.capacity

    def equipment_differences(self, other):
        '''
        (Classroom, Classroom) -> (bool)
        Returns the equipment of the first room that
        is not present in the seond room.
        '''
        return set(self.equipment).difference(set(other.equipment))

    def __repr__(self):
        '''
        Returns certain text (str).
        '''
        return f"Classroom('{self.number}', {self.capacity}, {self.equipment})"


class AcademicBuilding:
    '''
    Class that represents academic buildings.
    '''

    def __init__(self, address, classrooms):
        '''
        (Building, str, list(Classroom)) -> Nontype
        Initializes an academic building with such
        parameters: address, classroom.
        '''
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        '''
        (Building) -> (list)
        Returns a list of all equipment that is stored
        in each classroom of the building combined.
        '''
        all_equipment = []
        for room in self.classrooms:
            all_equipment += room.equipment
        total_equipment = []
        for elem in all_equipment:
            if (elem, all_equipment.count(elem)) not in total_equipment:
                total_equipment.append((elem, all_equipment.count(elem)))
        return total_equipment

    def __str__(self):
        '''
        Returns certain text (str).
        '''
        class_info = ''
        for room in self.classrooms:
            class_info += room.__str__() + '\n'
        return f'{self.address}\n{class_info[:-2]}'
