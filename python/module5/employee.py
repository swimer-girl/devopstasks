class Employee:
    """Базовый класс для сотрудников"""
    emp_count = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = self.first_name.lower() + '_' + self.last_name.lower() + '@example.com'
        self.salary = int(salary)
        Employee.emp_count += 1

    @property
    def full_name(self):
        return '{}, {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name):
        first_name, last_name = full_name.split(", ")
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    @classmethod
    def from_str(cls, arg):
        first_name, last_name, salary = arg.split(',')
        return cls(first_name, last_name, salary)


class DevOps(Employee):
    """Класс наследование DevOps от базового класса"""
    def __init__(self, first_name, last_name, salary, skills=[]):
        super(DevOps, self).__init__(first_name, last_name, salary)
        self.skills = [skill.title() for skill in skills]

    """Добавление/удаление навыков"""
    def add_skill(self, skill):
        if skill.title() not in self.skills:
            self.skills.append(skill.title())

    def remove_skill(self, skill):
        try:
            return self.skills.remove(skill.title())
        except Exception as e:
            pass


class Manager(Employee):
    """Класс наследование Manager от базового класса"""
    def __init__(self, first_name, last_name, salary, subordinates=[]):
        super(Manager, self).__init__(first_name, last_name, salary)
        self.subordinates = subordinates

    """Добавление/удаление подчиненных"""
    def add_subordinate(self, subordinate):
        if subordinate not in self.subordinates:
            self.subordinates.append(subordinate)

    def remove_subordinate(self, del_subordinate):
        if del_subordinate in self.subordinates:
            return self.subordinates.remove(del_subordinate)
        else:
            try:
                for i in self.subordinates:
                    if del_subordinate == i.email:
                        return self.subordinates.remove(i)
            except Exception as e:
                pass