# Scope Global
x = 0

def funcion1():
    # Scope Local
    x = 1
    print("Scope local: ", x)

    def funcion2():
        # Scope Enclosing
        x = 2
        print("Scope Enclosing: ", x)

    funcion2()

print("Scope global: ", x)
funcion1()
