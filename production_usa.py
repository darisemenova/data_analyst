import pandas
data = pandas.read_csv('crops_usa.csv')

# преобразуем столбцы датасета в списки
acres = list(data['Acres'])
production = list(data['Production'])
years = list(data['Year'])

acres_usa = [] # общая площадь посевов за каждый год
production_usa = []  # общий объём урожая за каждый год

for year in range(1980, 2020):
    acres_one_year = []
    production_one_year = []
    for index in range(len(data)):
        if years[index] == year:
            acres_one_year.append(acres[index])
            production_one_year.append(production[index])
    acres_usa.append(sum(acres_one_year))
    production_usa.append(sum(production_one_year))

yield_usa = [] # общая урожайность за каждый год
for index in range(len(production_usa)):
    yield_usa.append(production_usa[index] / acres_usa[index])
years_numbers = list(range(1980, 2020))

error_acres = [] # ошибки первой модели, предсказана площадь посевов
for index in range(1, len(production_usa)):
    error_acres.append(production_usa[index] - acres_usa[index] * yield_usa[index - 1])
    
error_yield = [] # ошибки второй модели, предсказана урожайность
for index in range(1, len(production_usa)):
    error_yield.append(production_usa[index] - acres_usa[index - 1] * yield_usa[index])

error_abs_acres = [] # модули ошибок первой модели
for value in error_acres:
    error_abs_acres.append(abs(value))
    
print(sum(error_abs_acres) / len(error_abs_acres)) # MAE первой модели

error_abs_yield = []
for value in error_yield:
    error_abs_yield.append(abs(value))
    
print(sum(error_abs_yield) / len(error_abs_yield))