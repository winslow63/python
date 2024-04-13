import pandas as pd

import matplotlib.pyplot as plt

def filter_by_date_range(df, start_date, end_date):
    df['Дата'] = pd.to_datetime(df['Дата'])
    filtered_df = df[(df['Дата'] >= start_date) & (df['Дата'] <= end_date)]

    return filtered_df
def filter_by_mean_deviation(df, deviation_value):
    filtered_df = df[df['среднее'] >= deviation_value]
    return filtered_df

def filter_by_month(df):
    df['Дата'] = pd.to_datetime(df['Дата'])
    monthly_mean = df.groupby(df['Дата'].dt.to_period('M')).mean().drop(columns=['Дата'])
    return monthly_mean


def plot_currency_monthly_stats(dataframe, month):
    dataframe['Дата'] = pd.to_datetime(dataframe['Дата'])
    monthly_data = dataframe[(dataframe['Дата'].dt.month == month) & (dataframe['Дата'].dt.year == 2024)]


    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['Дата'], monthly_data['Информация'], marker='o', linestyle='-')
    plt.title(f'Изменение курса за {month}-й месяц')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data['Дата'], monthly_data['Информация'], marker='o', linestyle='-', label='Изменение курса')
    plt.axhline(y=monthly_data['Информация'].median(), color='r', linestyle='--', label='Медиана')
    plt.axhline(y=monthly_data['Информация'].mean(), color='g', linestyle='--', label='Среднее значение')
    plt.title(f'Статистика курса за {month}-й месяц')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def course_change(dataframe):
    dataframe['Дата'] = pd.to_datetime(dataframe['Дата'])
    # Построить график изменения курса
    plt.figure(figsize=(10, 6))  # Задать размер графика
    plt.plot(dataframe['Дата'], dataframe['Информация'], marker='o', linestyle='-')  # Построить график
    plt.title('Изменение курса за весь период')  # Заголовок графика
    plt.xlabel('Дата')  # Подпись оси x
    plt.ylabel('Курс')  # Подпись оси y
    plt.grid(True)  # Включить сетку на графике
    plt.xticks(rotation=45)  # Повернуть подписи по оси x для лучшей читаемости
    plt.tight_layout()  # Улучшить компоновку графика
    plt.show()  # Показать график

if __name__ == '__main__':
    '''1'''
    df = pd.read_csv("course.csv",encoding='cp1251', delimiter=';')
    print(df.head())
    '''3'''
    invalid_values = df.isna().any()
    print("Колонки с невалидными значениями:")
    print(invalid_values)
    '''4'''
    df['Информация'] = df['Информация'].str.replace(',', '.').astype(float)
    median_rate = df['Информация'].median()
    mean_rate = df['Информация'].mean()
    print(median_rate)
    print(mean_rate)
    df['медиана'] = df['Информация'] - median_rate
    df['среднее'] = df['Информация'] - mean_rate

    '''5'''
    rate_stats = df['Информация'].describe()
    median_deviation_stats = df['медиана'].describe()
    mean_deviation_stats = df['среднее'].describe()
    print("Статистическая информация о курсе:")
    print(rate_stats)
    print("\nСтатистическая информация об отклонении от медианы:")
    print(median_deviation_stats)
    print("\nСтатистическая информация об отклонении от среднего:")
    print(mean_deviation_stats)


    '''6'''
    deviation_value = 0.3# значение отклонения от среднего значения курса
    filtered_df = filter_by_mean_deviation(df, deviation_value)
    print(filtered_df)

    '''7'''
    start_date = '2022-02-01'
    end_date = '2022-03-01'
    data_df = filter_by_date_range(df, start_date, end_date)
    print(data_df)

    '''8'''
    month=filter_by_month(df)
    print(month)
    '''9'''
    course_change(df)
    '''10'''
    plot_currency_monthly_stats(df, 4)

