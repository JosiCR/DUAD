Variable_global = 14

def cambiar_variable():
    global Variable_global
    Variable_global = 28
    


cambiar_variable()
print(Variable_global)