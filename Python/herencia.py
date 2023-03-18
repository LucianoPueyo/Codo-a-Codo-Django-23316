class Empleado:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property # Getter de nombre
    def nombre(self):
        return self.__nombre

    @nombre.setter # Setter de nombre
    def nombre(self, valor):
        self.__nombre = valor

    @property # Getter de apellido
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def nombre_completo(self):
        return f"Hola, mi nombre es {self.__nombre} {self.__apellido}"

class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario

    @property    
    def salario(self):
        return self.__salario
    

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * self.__valor_hora * 21


e1 = EmpleadoFullTime("Maria", "Gonzalez", 80000)
e2 = EmpleadoPorHora("Pedro", "Del Monte", 9, 3000)

print(e1.nombre_completo)
print(e2.nombre_completo)

print(e1.salario)
print(e2.salario)