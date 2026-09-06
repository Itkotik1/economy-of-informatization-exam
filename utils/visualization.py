"""
Шаблоны для графиков
"""
import matplotlib.pyplot as plt
import seaborn as sns

def setup_style():
    """Настройка единого стиля для всех графиков"""
    sns.set_theme(style='whitegrid')
    plt.rcParams['figure.figsize'] = (10, 6)