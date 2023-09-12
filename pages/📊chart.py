# import streamlit as st
# import pandas as pd
# import plotly.express as px

# def main():
#     st.title("Segments for analysis")
    
#     # Загрузка данных для круговой диаграммы
#     df_pie = pd.read_csv("data/age.csv", sep=";")
#     # Загрузка данных для столбчатой диаграммы
#     df_bar = pd.read_csv("data/bar_chat.csv")

#     # Выбор типа графика (круговая диаграмма или столбчатая)
#     chart_type = st.sidebar.selectbox("Select Chart Type:", ["Pie Chart", "Bar Chart"])
    
#     if chart_type == "Pie Chart":
#         # Создание круговой диаграммы
#         fig_pie = px.pie(df_pie, values='count', names='age', title='Age percentage distribution')
#         fig_pie.update_traces(marker=dict(colors=['yellow', 'purple', 'orange']), pull=[0.1, 0.1, 0.1])
        
#         # Добавление интерактивности круговой диаграмме (выделение сегмента при клике)
#         fig_pie.update_traces(textinfo='percent+label', hoverinfo='label+percent', hovertemplate='%{label}: %{percent:.1%}')
#         fig_pie.update_layout(clickmode='event+select')
        

#         st.plotly_chart(fig_pie)
#     else:
#         # Создание столбчатой диаграммы
#         fig_bar = px.bar(df_bar, x='adress', y='Record Count', title="Income levels of target audience")
#         fig_bar.update_traces(marker=dict(color=df_bar['Record Count'], colorbar=dict(title='count')))
        
#         # Добавление интерактивности столбчатой диаграмме
#         fig_bar.update_xaxes(type='category')
#         fig_bar.update_traces(hovertemplate='location: %{x}<br>Count: %{y}')
#           # Добавление интерактивности с помощью clickmode (переключение на инструмент выбора)
#         fig_bar.update_layout(clickmode='event+select')
#         st.plotly_chart(fig_bar)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import numpy as np



# def main():
#     st.title("Segments for analysis")
    
#     # Загрузка данных для круговой диаграммы
#     df_pie = pd.read_csv("data/age.csv", sep=";")
#     # Загрузка данных для столбчатой диаграммы
#     df_bar = pd.read_csv("data/bar_chat.csv")

#     # Выбор типа графика (круговая диаграмма или столбчатая)
#     chart_type = st.sidebar.selectbox("Select Chart Type:", ["Pie Chart", "Bar Chart"])
    
#     if chart_type == "Pie Chart":
#         # Создание круговой диаграммы
#         fig_pie = px.pie(df_pie, values='count', names='age', title='Age percentage distribution',
#                          color_discrete_sequence=['orange', 'yellow', 'Crimson'])  # Задайте цвета здесь
#         fig_pie.update_traces(pull=[0.1, 0.1, 0.1])
        
#         # Добавление интерактивности круговой диаграмме (выделение сегмента при клике)
#         fig_pie.update_traces(textinfo='percent+label', hoverinfo='label+percent', hovertemplate='%{label}: %{percent:.1%}')
#         fig_pie.update_layout(clickmode='event+select')

#         st.plotly_chart(fig_pie)
#     else:
#         # Создание столбчатой диаграммы
#         fig_bar = px.bar(df_bar, x='adress', y='Record Count', title="Income levels of target audience",
#                          color='Record Count', color_continuous_scale='solar')  # Задайте цвета здесь
#         fig_bar.update_coloraxes(colorbar_title='Count')
        
        
#         # Добавление интерактивности столбчатой диаграмме
#         fig_bar.update_xaxes(type='category')
#         fig_bar.update_traces(hovertemplate='location: %{x}<br>Count: %{y}')
#         # Добавление интерактивности с помощью clickmode (переключение на инструмент выбора)
#         fig_bar.update_layout(clickmode='event+select')
        
#         st.plotly_chart(fig_bar)

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def main():
    st.title("Segments for analysis")

    # Загрузка данных для круговой диаграммы
    df_pie = pd.read_csv("data/age.csv", sep=";")

    # Выбор типа графика (круговая диаграмма или столбчатая)
    chart_type = st.sidebar.selectbox("Select Chart Type:", ["Pie Chart", "Bar Chart"])

    if chart_type == "Pie Chart":
        # Создание круговой диаграммы
        fig_pie = px.pie(df_pie, values='count', names='age', title='Age percentage distribution',
                         color_discrete_sequence=['orange', 'yellow', 'Crimson'])  # Задайте цвета здесь
        fig_pie.update_traces(pull=[0.1, 0.1, 0.1])

        # Добавление интерактивности круговой диаграмме (выделение сегмента при клике)
        fig_pie.update_traces(textinfo='percent+label', hoverinfo='label+percent', hovertemplate='%{label}: %{percent:.1%}')
        fig_pie.update_layout(clickmode='event+select')

        # Вывод круговой диаграммы
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        # Создание случайных данных для столбчатой диаграммы
        np.random.seed(42)
        n = 10  # Количество данных
        income_levels = [f"Income Level {i}" for i in range(1, n + 1)]
        count_1 = np.random.randint(1, 50000, size=n)
        count_2 = np.random.randint(1, 60000, size=n)
        count_3 = np.random.randint(1, 40000, size=n)
        count_4 = np.random.randint(1, 80000, size=n)

        # Создаем датафрейм из случайных данных
        data = pd.DataFrame({"Income > 3000 000 < 7 000 000": count_1, "Income > 7 000 001 < 10 000 000": count_2,
                             "Income > 10 000 001 < 15 000 000": count_3, "Income >15 000 001 ": count_4})

        # Выводим случайные данные
        #st.write("Random Data:")
       # st.write(data, visible=False)  # Скрываем таблицу

        # Создание столбчатой диаграммы
        fig_bar = px.bar(data, title="Income Levels vs. Count")

        # Добавление интерактивности столбчатой диаграмме
        fig_bar.update_xaxes(type='category')
        fig_bar.update_traces(hovertemplate='Income Level: %{x}<br>Count: %{y}')

        # Вывод столбчатой диаграммы
        st.plotly_chart(fig_bar, use_container_width=True)

if __name__ == "__main__":
    main()
