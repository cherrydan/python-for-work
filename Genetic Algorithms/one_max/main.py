#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt
import seaborn as sns

from one_max import *
from one_max.one_max_fitness import one_max_fitness

"""
Выше мы видели, что одним из основных компонентов каркаса DEAP
является класс Toolbox, который позволяет регистрировать новые функ-
ции (или операторы), настраивая поведение существующих функций.
В данном случае мы воспользуемся им, чтобы определить оператор
zeroOrOne путем специализации функции random.randomint(a, b).

"""

toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)

"""

Далее следует создать класс Fitness. Поскольку у нас всего одна цель –
сумма цифр, а наша задача – максимизировать ее, то выбираем страте-
гию FitnessMax, задав в кортеже weights всего один положительный вес:

"""

creator.create("FitnessMax", base.Fitness, weights=[1.0,])

"""

По соглашению, в DEAP для представления индивидуумов использу-
ется класс с именем Individual, для создания которого применяется
модуль creator. В нашем случае базовым классом является list, т. е.
хромосома представляется списком. Дополнительно в класс добавля-
ется атрибут fitness, инициализируемый экземпляром определенного
ранее класса FitnessMax

"""
creator.create("Individual", list, fitness=creator.FitnessMax)

"""

Следующий номер нашей программы – регистрация оператора indi-
vidualCreator, который создает экземпляр класса Individual, заполнен-
ный случайными значениями 0 или 1. Для этого мы настроим ранее
определенный оператор zeroOrOne. В качестве базового класса исполь-
зуется вышеупомянутый оператор initRepeat, специализированный
следующими аргументами:

"""
toolbox.register("individualCreator", tools.initRepeat,
                 creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)

"""

Наконец, регистрируем оператор populationCreator, создающий список
индивидуумов. В его определении также используется оператор initRe-
peat со следующими аргументами:

"""
toolbox.register("populationCreator", tools.initRepeat,
                 list, toolbox.individualCreator)
"""
Теперь определим оператор evaluate – псевдоним только что опреде-
ленной функции one_max_fitness
"""
toolbox.register("evaluate", one_max_fitness)

"""
В предыдущем разделе мы говорили, что генетические операторы
обычно создаются как псевдонимы существующих функций из мо-
дуля tools с конкретными значениями аргументов. В данном случае
аргументы будут такими:
* турнирный отбор с размером турнира 3;
* одноточечное скрещивание;
* мутация инвертированием бита.
"""
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0 / ONE_MAX_LENGTH)


def main():
    # Создаем начальную популяцию оператором populationCreator, задавая
    # размер популяции POPULATION_SIZE

    population = toolbox.populationCreator(n=POPULATION_SIZE)
    generation_counter = 0

    # Для вычисления приспособленности каждого индивидуума в началь-
    # ной популяции воспользуемся функцией Python map(), которая при-
    # меняет оператор evaluate к каждому элементу популяции
    fitness_values = list(map(toolbox.evaluate, population))

    # Поскольку элементы списка fitnessValues взаимно однозначно со-
    # ответствуют элементам популяции (представляющей собой список
    # индивидуумов), мы можем воспользоваться функцией zip(), чтобы
    # объединить их попарно, сопоставив каждому индивидууму его при-
    # способленность
    for individual, fitness_value in zip(population, fitness_values):
        individual.fitness.values = fitness_value

    # Далее, так как в нашем случае имеет место приспособляемость всего
    # с одной целью, то извлекаем первое значение из каждого кортежа при-
    # способленности для сбора статистики:
    fitness_values = [individual.fitness.values[0] for individual in population]

    # В качестве статистики мы собираем максимальное и среднее значение
    # приспособленности в каждом поколении. Для этого нам понадобятся
    # два списка, создадим их
    max_fitness_values = []
    mean_fitness_values = []

    # Теперь мы готовы написать главный цикл алгоритма. В самом начале
    # цикла проверяются условия остановки. Одно из них – ограничение на
    # количество поколений, второе – проверка на лучшее возможное реше-
    # ние (двоичная строка из одних единиц)
    while max(fitness_values) < ONE_MAX_LENGTH and generation_counter < MAX_GENERATIONS:
        generation_counter += 1

        # Сердце алгоритма – генетические операторы, которые применяются на
        # следующем шаге. Сначала – оператор отбора toolbox.select, который
        # мы выше определили как турнирный отбор. Поскольку размер турни-
        # ра был задан в определении оператора, сейчас нам осталось передать
        # только популяцию и ее размер
        offspring = toolbox.select(population, len(population))

        # Далее отобранные индивидуумы, которые находятся в списке off-
        # spring, клонируются, чтобы можно было применить к ним следующие
        # генетические операторы, не затрагивая исходную популяцию
        offspring = list(map(toolbox.clone, offspring))

        # Следующий генетический оператор – скрещивание. Ранее мы опре-
        # делили его в атрибуте toolbox.mate как псевдоним одноточечного
        # скрещивания. Мы воспользуемся встроенной в Python операцией
        # среза, чтобы объединить в пары каждый элемент списка offspring
        # с четным индексом со следующим за ним элементом с нечетным
        # индексом. Затем с по­м ощью функции random() мы «подбросим моне-
        # ту» с вероятностью, заданной константой P_CROSSOVER, и тем самым
        # решим, применять к паре индивидуумов скрещивание или оставить
        # их как есть. И наконец, удалим значения приспособленности потом-
        # ков, потому что они были модифицированы и старые значения уже
        # не актуальны:
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < P_CROSSOVER:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        # Последний генетический оператор – мутация, ранее мы определили
        # его в атрибуте toolbox.mutate как псевдоним инвертирования бита. Мы
        # должны обойти всех потомков и применить оператор мутации с веро-
        # ятностью P_MUTATION.
        for mutant in offspring:
            if random.random() < P_MUTATION:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # Те индивидуумы, к которым не применялось ни скрещивание, ни му-
        # тация, остались неизменными, поэтому их приспособленности, вы-
        # численные в предыдущем поколении, не нужно заново пересчитывать.
        # В остальных индивидуумах значение приспособленности будет пус­
        # тым. Мы находим этих индивидуумов, проверяя свойство valid класса
        # Fitness, после чего вычисляем новое значение приспособленности так
        # же, как делали это ранее
        fresh_individuals = [ind for ind in offspring if not ind.fitness.valid]
        fresh_fitness_values = list(map(toolbox.evaluate, fresh_individuals))
        for individual, fitness_value in zip(fresh_individuals, fresh_fitness_values):
            individual.fitness.values = fitness_value
        # После того как все генетические операторы применены, нужно заме-
        # нить старую популяцию новой:
        population[:] = offspring

        # Прежде чем переходить к следующей итерации, учтем в статистике
        # текущие значения приспособленности. Поскольку приспособленность
        # представлена кортежем (из одного элемента), необходимо указать ин-
        # декс [0]
        fitness_values = [ind.fitness.values[0] for ind in population]

        # Далее мы вычисляем максимальное и среднее значения, помещаем их
        # в накопители и печатаем сводную информацию
        max_fitness = max(fitness_values)
        mean_fitness = sum(fitness_values) / len(population)
        max_fitness_values.append(max_fitness)
        mean_fitness_values.append(mean_fitness)
        print('-Поколение {}: Макс. приспособ. = {}, Сред. приспособ. = {}'.format(
            generation_counter, max_fitness, mean_fitness
        ))
        # Дополнительно мы находим индекс (первого) лучшего индивиду
        # ума, пользуясь только что найденным значением приспособленности,
        # и распечатываем этого индивидуума
        best_ind = fitness_values.index(max(fitness_values))
        print('Лучший индивидуум  = ', *population[best_ind], '\n')

    # выводим графики на экран
    sns.set_style('whitegrid')
    plt.plot(max_fitness_values, color='red')
    plt.plot(mean_fitness_values, color='green')
    plt.xlabel('Поколение')
    plt.ylabel('Макс/сред. приспособляемость')
    plt.title('Зависимость макс.и сред. приспособляемости от поколения')

    plt.savefig('one_max_graph.png', dpi=600)

    plt.show()


if __name__ == '__main__':
    main()
