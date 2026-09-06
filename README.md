
# Экономика информатизации — Решения экзаменационных задач

## О репозитории

Данный репозиторий содержит решения экзаменационных задач по курсу "Экономика информатизации". Все решения выполнены в формате Jupyter Notebook с визуализациями и экономической интерпретацией результатов.

Проект использует современный менеджер пакетов **`uv`** для управления зависимостями, что обеспечивает высокую скорость установки и воспроизводимость окружения.

---

## Структура репозитория

```
economy-of-informatization-exam/
├── .venv/                          # Виртуальное окружение (создается uv)
├── .gitignore                      # Игнорируемые файлы
├── README.md                       # Описание репозитория
├── pyproject.toml                  # Зависимости проекта (uv)
├── uv.lock                         # Блокировка версий пакетов
│
├── notebooks/                      # Jupyter Notebook с решениями задач
│   ├── task_01_attention_economy.ipynb
│   ├── task_02_cocomo_calculation.ipynb
│   ├── task_03_tco_analysis.ipynb
│   ├── task_04_roi_tei_calculation.ipynb
│   ├── task_05_unit_economics.ipynb
│   ├── task_06_token_costs.ipynb
│   ├── task_07_winner_curse.ipynb
│   ├── task_08_evpi_calculation.ipynb
│   ├── task_09_real_options.ipynb
│   ├── task_10_nmck_calculation.ipynb
│   └── task_11_budget_justification.ipynb
│
├── data/                           # Исходные данные
│   ├── reference_data.csv          # Справочные данные
│   └── tasks_config.json           # Конфигурация задач
│
├── reports/                        # Экспортированные отчеты
│   ├── task_01_report.txt
│   ├── task_01_cash_flows.png
│   └── ... (другие отчеты)
│
├── utils/                          # Вспомогательные функции
│   ├── __init__.py
│   ├── calculations.py             # Общие функции расчетов
│   └── visualization.py            # Шаблоны для графиков
│
└── docs/                           # Документация
    ├── methodology.md              # Методологические пояснения
    └── glossary.md                 # Глоссарий терминов
```

---

## Установка и запуск

### Требования
- Python 3.10 или выше
- `uv` (установка описана ниже)

### 1. Клонирование репозитория

```bash
git clone https://github.com/username/economy-of-informatization-exam.git
cd economy-of-informatization-exam
```

### 2. Установка `uv` (если не установлен)

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Перезапустите терминал после установки.

### 3. Создание виртуального окружения и установка зависимостей

```bash
# Создание виртуального окружения
uv venv

# Активация окружения
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Установка всех зависимостей из pyproject.toml
uv sync
```

### 4. Установка Jupyter ядра для работы в PyCharm

```bash
# Установка ipykernel
uv add --dev ipykernel

# Регистрация ядра
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name="economy-exam"
```

### 5. Запуск Jupyter

```bash
# Запуск Jupyter Lab
uv run --with jupyter jupyter lab

# Или Jupyter Notebook
uv run --with jupyter jupyter notebook
```

---

## Зависимости

Основные зависимости проекта (управляются через `uv`):

| Пакет | Версия | Назначение |
|-------|--------|------------|
| `pandas` | latest | Работа с данными |
| `numpy` | latest | Численные расчеты |
| `matplotlib` | latest | Построение графиков |
| `seaborn` | latest | Статистическая визуализация |
| `scipy` | latest | Научные расчеты |
| `openpyxl` | latest | Работа с Excel-файлами |
| `tabulate` | latest | Табличное представление данных |


### Добавление новых пакетов

```bash
# Добавление основного пакета
uv add package_name

# Добавление пакета для разработки
uv add --dev package_name

# Обновление всех пакетов
uv sync --upgrade
```

---

## Список задач

| № | Задача | Статус |
|---|--------|--------|
| 1 | Экономика внимания (внедрение CRM) | ✅ Выполнено |
| 2 | Расчет COCOMO | ⏳ В процессе |
| 3 | TCO анализ | ⏳ В процессе |
| 4 | ROI / TEI расчет | ⏳ В процессе |
| 5 | Юнит-экономика | ⏳ В процессе |
| 6 | Расчет затрат на токены | ⏳ В процессе |
| 7 | Проклятие победителя | ⏳ В процессе |
| 8 | EVPI расчет | ⏳ В процессе |
| 9 | Реальные опционы | ⏳ В процессе |
| 10 | Расчет НМЦК | ⏳ В процессе |
| 11 | Обоснование бюджета | ⏳ В процессе |

---

## Использование

### Запуск отдельного ноутбука

1. Откройте PyCharm и загрузите проект.
2. Выберите ядро `economy-exam` в правом верхнем углу ноутбука.
3. Выполняйте ячейки последовательно (Shift+Enter).

### Генерация отчетов

После выполнения всех расчетов в ноутбуке выполните ячейку с генерацией отчета. Отчеты сохраняются в папку `reports/` в формате `.txt`.

```python
# Пример вызова генерации отчета
from datetime import datetime
# ... код генерации отчета ...
with open('../reports/task_XX_report.txt', 'w', encoding='utf-8') as f:
    f.write(report_content)
```

### Экспорт результатов

Результаты расчетов можно экспортировать в CSV:

```python
df_results.to_csv('../reports/task_XX_results.csv', index=False)
```

---

## Особенности работы с `uv` в PyCharm

1. **Создание нового проекта:** При создании проекта в PyCharm выберите **Custom environment → Type: uv**.
2. **Активация окружения:** PyCharm автоматически активирует `.venv` при открытии терминала.
3. **Добавление пакетов:** Используйте терминал PyCharm для выполнения команд `uv add`.
4. **Выбор ядра:** Для Jupyter ноутбуков выберите зарегистрированное ядро `economy-exam`.

---

## Авторы

**Студент:** Орлова Екатерина Александровна  
**Группа:** 4-2\
**Направление:** Прикладная информатика  
**Год:** 2026

---

## Контакты

**email** : vip.okaterina@gmail.com

**tg**: itkotik1


