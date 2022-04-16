from sklearn.neural_network import MLPClassifier


# coding=utf-8
# TheGodEye = MLPClassifier()
def OneMix():
    import random

    import matplotlib.pyplot as plt
    import numpy as np
    from deap import algorithms, base, creator, tools

    ONE_MAX_LENGHT = 100
    POPULATION_SIZE = 300
    MAX_GENERATIONS = 50
    P_CROSSOVER = 0.9
    P_MUTATION = 0.1

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    def oneMaxFitnes(individual):
        return (sum(individual),)  # кортеж

    toolbox = base.Toolbox()
    toolbox.register("zeroOrOne", random.randint, 0, 1)
    toolbox.register(
        "IndividualCreator",
        tools.initRepeat,
        creator.Individual,
        toolbox.zeroOrOne,
        ONE_MAX_LENGHT,
    )
    toolbox.register(
        "populationCreator", tools.initRepeat, list, toolbox.IndividualCreator
    )

    population = toolbox.populationCreator(n=POPULATION_SIZE)

    toolbox.register("evaluate", oneMaxFitnes)
    toolbox.register("select", tools.selTournament, tournsize=5)
    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=1.0 / ONE_MAX_LENGHT)

    stats = tools.Statistics(lambda x: x.fitness.values)
    stats.register("max", np.max)
    stats.register("avg", np.mean)

    population, logbook = algorithms.eaSimple(
        population,
        toolbox,
        cxpb=P_CROSSOVER,
        mutpb=P_MUTATION,
        ngen=MAX_GENERATIONS,
        stats=stats,
        verbose=True,
    )

    MaxPopVal, MeanPopVal = logbook.select("max", "avg")
    print(MaxPopVal)
    plt.plot(MaxPopVal, color="red")
    plt.plot(MeanPopVal, color="blue")
    plt.xlabel("Поколения")
    plt.ylabel("Макс/ср")
    plt.show()


def gen_population():
    import random

    import matplotlib.pyplot as plt
    import numpy as np
    from deap import algorithms, base, creator, tools

    ONE_MAX_LENGHT = 100
    POPULATION_SIZE = 300
    MAX_GENERATIONS = 50
    P_CROSSOVER = 0.9
    P_MUTATION = 0.1


GodEye = MLPClassifier(
    hidden_layer_sizes=(3, 30, 1), solver="lbfgs", activation="logistic"
)
GodEye.coefs_ = OneMix()


OneMix()
