import streamlit as st
import folium
from folium.plugins import MarkerCluster
import plotly.express as px
import pandas as pd

st.set_page_config(
    layout="wide"
)

# Заголовок для основной части приложения
st.title("Taxonomy to attract new customers")

# Создание карты с помощью Folium
m = folium.Map(location=[41.3082, 69.2598], zoom_start=12)

# Добавление маркеров и больших желтых кругов на карту
data = {
    "latitude": [41.344297, 41.327652, 41.290056, 41.324093, 41.350726, 41.296011, 41.228456],
    "longitude": [69.20479, 69.337834, 69.225326, 69.297973, 69.244027, 69.280788, 69.218039],
    "names": ["Beruniy", "Buyuk Ipak Yo'li", "Novsa", "Novomoskovskaya", "Olmazor", "Said Baraka", "Sergeli"]
}

marker_cluster = MarkerCluster().add_to(m)

for i, row in enumerate(data["latitude"]):
    folium.Marker(
        location=[data["latitude"][i], data["longitude"][i]],
        popup=f"<b>Название:</b> {data['names'][i]}<br><b>Latitude:</b> {data['latitude'][i]}<br><b>Longitude:</b> {data['longitude'][i]}",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(marker_cluster)

    folium.Circle(
        location=[data["latitude"][i], data["longitude"][i]],
        radius=1200,  # Увеличим радиус для желтых кругов
        color="yellow",
        fill=True,
        fill_color="yellow",
        fill_opacity=0.3,
    ).add_to(m)

# Добавляем легенду к карте
folium.LayerControl().add_to(m)

# Виджет Streamlit для выбора ресторанов DoDo Pizza
selected_points = st.sidebar.multiselect("DoDo Pizza Restaurants:", data["names"])

# Отображение выбранных точек на карте
if selected_points:
    for point in selected_points:
        index = data["names"].index(point)
        folium.Marker(
            location=[data["latitude"][index], data["longitude"][index]],
            popup=f"<b>Название:</b> {data['names'][index]}<br><b>Latitude:</b> {data['latitude'][index]}<br><b>Longitude:</b> {data['longitude'][index]}",
            icon=folium.Icon(color="green", icon="check"),
        ).add_to(m)

map_height = 800  # Уменьшим высоту карты, чтобы она лучше поместилась на странице
map_width = 1200  # Уменьшим ширину карты
map_html = f'<div style="display: flex; justify-content: center; align-items: center; height: {map_height}px; width: {map_width}px;">' + m.get_root().render() + '</div>'
st.components.v1.html(map_html, width=map_width, height=map_height)

st.markdown("<p style ='color:red;',> Big Data\ Taxonomy <p/>", unsafe_allow_html=True)



def main():
   #st.header("Segments for analysis")
    
    # Загрузка данных для столбчатой диаграммы
    df_bar = pd.read_csv("data/bar_chat.csv")

    # Виджет для настройки количества сегментов
    segments = st.sidebar.slider("Number of Segments", 1, 100)
    
    # Создание столбчатой диаграммы с желтым или оранжевым цветом
    fig_bar = px.bar(df_bar, x='adress', y='Record Count', title="Number of people in the location",
                         color='Record Count', color_continuous_scale='Plasma')  # Задайте цвета здесь
    fig_bar.update_coloraxes(colorbar_title='Count')
    
    # Добавление интерактивности столбчатой диаграмме
    fig_bar.update_xaxes(type='category')
    fig_bar.update_traces(hovertemplate='Location: %{x}<br>Count: %{y}')
    
    # Увеличьте размер диаграммы
    fig_bar.update_layout(width=400, height=600)
    
    # Добавление интерактивности с помощью clickmode (переключение на инструмент выбора)
    fig_bar.update_layout(clickmode='event+select')
    
    # Отображение столбчатой диаграммы в столбце слева с заголовком
    st.subheader("Location Data")
    st.plotly_chart(fig_bar, use_container_width=True)
    
    
if __name__ == "__main__":
    main()



