"""
Общие функции для экономических расчетов
"""
import pandas as pd
import numpy as np

def load_reference_data():
    """Загрузка справочных данных"""
    # пока просто заглушка
    return pd.read_csv('data/reference_data.csv')

def calculate_cocomo(sloc, mode='organic'):
    """
    Расчет COCOMO (пример)
    """
    # Позже заполним реальной логикой
    pass