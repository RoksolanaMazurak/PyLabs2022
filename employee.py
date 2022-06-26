import dbList


class Employee:

    def __init__(self, name: str, surname: str, education: str, speciality: str,
                 experience: int, birth_year: int) -> None:
        self.__surname = surname
        self.__name = name
        self.__education = education
        self.__speciality = speciality
        self.__experience = experience
        self.__birth_year = birth_year

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        self.__experience = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    def __str__(self):
        return f"Name: {self.__name}, surname: {self.__surname}, education: {self.__education}, speciality: {self.__speciality}, " \
               f"experience: {self.__experience}, year of birth: {self.__birth_year}."