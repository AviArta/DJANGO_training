from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def get_omlet(request):
    servings = request.GET.get('servings', 1)
    context = {'recipe': {
        'яйца, шт': 2 * int(servings),
        'молоко, л': 0.1 * int(servings),
        'соль, ч.л.': 0.5 * int(servings)},
        'servings': servings}
    return render(request, 'calculator/index.html', context)

def get_pasta(request):
    servings = request.GET.get('servings', 1)
    context = {'recipe': {
        'макароны, г': 0.3 * int(servings),
        'сыр, г': 0.05 * int(servings)},
        'servings': servings}
    return render(request, 'calculator/index.html', context)

# реализовала через указание персон через параметр URL:
def get_buter(request, counter):
    context = {'recipe': {
        'хлеб, ломтик': 1 * counter,
        'колбаса, ломтик': 1 * counter,
        'сыр, ломтик': 1 * counter,
        'помидор, ломтик': 1 * counter,
    },
        'counter': counter}
    return render(request, 'calculator/buter.html', context)