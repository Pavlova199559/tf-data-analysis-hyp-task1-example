import pandas as pd
import numpy as np
from scipy.stats import norm
!pip install google.colab
from google.colab import files
import pandas as pd
chat_id = 789271490  # Ваш chat ID, не меняйте название переменной

# Откроется диалоговое окно для загрузки файла
uploaded = files.upload()

# Извлечение имени загруженного файла
file_name = list(uploaded.keys())[0]

# Загрузка файла в DataFrame
data = pd.read_csv(file_name)

# Допустим, четные и нечетные `ID` определяют разные группы.
data['group'] = data['ID'] % 2  # Четные в одной группе, нечетные в другой

# Разделяем данные по группам
group_0 = data[data['group'] == 0]  # Группа 0
group_1 = data[data['group'] == 1]  # Группа 1

# Извлекаем данные для успешных и общих попыток
x_success = group_0['Флаг продажи'].sum()  # Успехи в группе 0
x_cnt = group_0['Флаг дозвона'].count()   # Общее количество в группе 0

y_success = group_1['Флаг продажи'].sum()  # Успехи в группе 1
y_cnt = group_1['Флаг дозвона'].count()   # Общее количество в группе 1

# Определение z-теста для пропорций
def solution(x_success, x_cnt, y_success, y_cnt):
    # Пропорции успеха для каждой группы
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    # Объединенная пропорция успеха
    pooled_p = (x_success + y_success) / (x_cnt + y_cnt)

    # Стандартная ошибка разницы пропорций
    se = np.sqrt(pooled_p * (1 - pooled_p) * (1 / x_cnt + 1 / y_cnt))

    # z-статистика
    z = (p1 - p2) / se

    # Критическое значение z для уровня значимости 5% (двусторонний тест)
    z_crit = norm.ppf(1 - 0.05 / 2)

    # Возвращаем `True`, если z-статистика показывает статистически значимую разницу
    return abs(z) >= z_crit

# Проверка на статистически значимую разницу между группами
result = solution(x_success, x_cnt, y_success, y_cnt)

print("Статистически значимая разница:", result)
