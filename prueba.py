from pyomo.environ import *

# Crear el modelo
model = ConcreteModel()

# Definir las variables
model.manzana = Var(within=NonNegativeReals)  
model.pino = Var(within=NonNegativeReals)  

# Definir la función objetivo
model.obj = Objective(expr=1 * model.manzana + 1.2 * model.pino, sense=maximize)

# Definir las restricciones
model.constr1 = Constraint(expr=0.3 * model.manzana + 0.5 * model.pino <= 20) 
model.constr2 = Constraint(expr=0.7 * model.manzana + 0.5 * model.pino <= 28) 
model.constr3 = Constraint(expr=model.manzana <= 30)  

# Crear el solver especificando la ruta del ejecutable
solver = SolverFactory('glpk',executable='C:/Users/usuario/Downloads/winglpk-4.65/glpk-4.65/w64/glpsol.exe')

# Resolver el modelo
results = solver.solve(model)

# Imprimir los resultados
print(f"Litros de Verde Manzana a producir: {model.manzana.value}")
print(f"Litros de Verde Pino a producir: {model.pino.value}")
print(f"Beneficio máximo: {model.obj()} €")