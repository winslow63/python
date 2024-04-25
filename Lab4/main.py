import argparse
import datetime
import logging
import matplotlib.pyplot as plt
import pandas as pd


def filter_by_date_range(df:pd.DataFrame, start_date:str, end_date:str)-> pd.DataFrame:
    """
    DataFram отфильтрованный по датам DataFram
    :param df: начальный датьфреейм
    :type df: pd.DataFrame
    :param start_date: начальная дата
    :type start_date: str
    :param end_date: конечная дата
    :type end_date: str
    :return: датафрейм отфильтрованный по датам
    :rtype:pd.DataFrame
    """
    df['Дата'] = pd.to_datetime(df['Дата'])
    filtered_df = df[(df['Дата'] >= start_date) & (df['Дата'] <= end_date)]
    return filtered_df


def filter_by_mean_deviation(df:pd.DataFrame, deviation_value:float)-> pd.DataFrame:
    """
    DataFrame отфильтрованный по значению отклонения от среднего значения курса
    :param df: начальный датьфреейм
    :type df: pd.DataFrame
    :param deviation_value: отклонение
    :type deviation_value: float
    :return: датафрейм отфильтрованный поотклонениям
    :rtype:pd.DataFrame
    """
    filtered_df = df[df['среднее'] >= deviation_value]
    return filtered_df


def filter_by_month(df:pd.DataFrame)->pd.DataFrame:
    """
    Групировка по месяцу
    :param df: начальный датьфреейм
    :type df: pd.DataFrame
    :return: сгрупированный датафрейм
    :rtype:pd.DataFrame
    """
    df['Дата'] = pd.to_datetime(df['Дата'])
    monthly_mean = df.groupby(df['Дата'].dt.to_period('M')).mean().drop(columns=['Дата'])
    return monthly_mean


def plot_currency_monthly_stats(dataframe:pd.DataFrame, month:int)->None:
    """"
    графики изменения курса, а также медиану и среднее значение за указанный месяц
    :param dataframe: начальный датьфреейм
    :type dataframe: pd.DataFrame
    :param month: месяц
    :type month: int
    """
    dataframe['Дата'] = pd.to_datetime(dataframe['Дата'])
    monthly_data = dataframe[(dataframe['Дата'].dt.month == month) & (dataframe['Дата'].dt.year == datetime.now().year)]
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


def course_change(dataframe:pd.DataFrame)->None:
    """
    график изменения курса за весь период
    :param dataframe: начальный датьфреейм
    :type dataframe: pd.DataFrame
    """
    dataframe['Дата'] = pd.to_datetime(dataframe['Дата'])
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['Дата'], dataframe['Информация'], marker='o', linestyle='-')
    plt.title('Изменение курса за весь период')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    console_logger = logging.getLogger('console_logger')
    console_logger.addHandler(console_handler)

    parser = argparse.ArgumentParser(description="получение статистики")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--option1", action="store_true", help="Фильтрация по отклонению от среднего значения курса")
    group.add_argument("--option2", action="store_true", help="Фильтрация по дате")
    group.add_argument("--option3", action="store_true", help="Фильтрация по месяцу")
    group.add_argument("--option4", action="store_true", help="Построение графика для всего периода")
    group.add_argument("--option5", action="store_true", help="Построение графика для определенного месяца")
    parser.add_argument("--deviation_value",type=float, default=0.3)
    parser.add_argument("--start_date",type=str, default="2022-02-01")
    parser.add_argument("--end_date",type=str, default="2022-03-01")
    args = parser.parse_args()


    df = pd.read_csv("course.csv",encoding='cp1251', delimiter=';')
    console_logger.info(f"{df.head()}")
    invalid_values = df.isna().any()
    console_logger.info(f"Колонки с невалидными значениями:{invalid_values}")
    df['Информация'] = df['Информация'].str.replace(',', '.').astype(float)
    median_rate = df['Информация'].median()
    mean_rate = df['Информация'].mean()
    console_logger.info(f"Медиана:{median_rate}")
    console_logger.info(f"Среднее:{mean_rate}")
    df['медиана'] = df['Информация'] - median_rate
    df['среднее'] = df['Информация'] - mean_rate

    rate_stats = df['Информация'].describe()
    median_deviation_stats = df['медиана'].describe()
    mean_deviation_stats = df['среднее'].describe()

    console_logger.info(f"Статистическая информация о курсе:{rate_stats}")
    console_logger.info(f"\nСтатистическая информация об отклонении от медианы:{median_deviation_stats}")
    console_logger.info(f"\nСтатистическая информация об отклонении от среднего:{mean_deviation_stats}")

    if args.option1:
        filtered_df = filter_by_mean_deviation(df, args.deviation_value)
        console_logger.info(f"{filtered_df}")
    elif args.option2:
        data_df = filter_by_date_range(df, args.start_date, args.end_date)
        console_logger.info(f"{data_df}")
    elif args.option3:
        month = filter_by_month(df)
        console_logger.info(f"{month}")
    elif args.option4:
        course_change(df)
    elif args.option5:
        plot_currency_monthly_stats(df, 4)
    else:
        console_logger.info(f"Выбран неправильный номер")

