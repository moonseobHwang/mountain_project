from pymongo import MongoClient
from folium import plugins
from folium.plugins import MarkerCluster
import folium
import pandas as pd

# mongodb database를 이용하여 folium 시각화 방법
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.mountain # mountain 데이터베이스에 접속, mountainscrap.py를 사용하여 DB 생성
df = pd.DataFrame(db.sampleCollection.find()) # dataFrame타입으로 전환 후 sampleCollection이라는 collection에 접속
df1 = pd.DataFrame(db.yaksu.find())
#print(df.dtypes) # dataframe columns type check
df['address_1']=df['address_1'].astype(float)
df['address_2']=df['address_2'].astype(float)
df1['Address_1']=df1['Address_1'].astype(float) # address_1 column type이 기존 object여서 float으로 변경
df1['Address_2']=df1['Address_2'].astype(float) # address_1 column type이 기존 object여서 float으로 변경
m = folium.Map(location=[36.70,127.90], zoom_start=8) # map을 열었을때의 시작 화면, list html과 연결하기
marker_cluster = MarkerCluster().add_to(m)
# iterrrows()함수보다 apply()함수(+lamda)가 data처리가 더 빠름
for index, row in df.iterrows(): # pandas for문, iterrows는 dataframe의 행을 나타냄
    tooltip = 'Click!'
    html = f"""
    <header>
        <h3>{row['class_']}</h3>
    </header>
    <body>
        <table>
            <tr>
                <td><img src ={row['img_data']} width='100' height='100'></td>
                <td>
                    <p style="font-size:15px">
                    &nbsp;
                    {row['address_1']}
                    {row['address_2']}
                    </p>
                    <p style="font-size:15px">
                    &nbsp;
                    날씨 : {row['weather_data']}
                    </p>
                    <p style="font-size:15px">
                    &nbsp;
                    풍속 : {row['wind_data']}
                    </p>
                </td>
            </tr>
        </table>
    """
    html = folium.Html(html,script=True, width=300, height=200) # popup을 html로 열고, dataframe에 각 열의 name 값 불러오기
    popup = folium.Popup(html=html, max_width='100%')
    folium.Marker([row['address_1'], row['address_2']], popup=popup,  icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(marker_cluster) # dataframe에 각 열의 위도,경도 값 불러오기

for index, row in df1.iterrows(): # pandas for문, iterrows는 dataframe의 행을 나타냄
    tooltip = 'Click!'
    html = f"""
    <header>
        <h3>{row['class_']}</h3>
    </header>
    <body>
        <table>
            <tr>
                <td>
                    <p style="font-size:15px">
                    &nbsp;
                    {row['Address_1']}
                    {row['Address_2']}
                    </p>
                    <p style="font-size:15px">
                    &nbsp;
                    날씨 : {row['weather_data_y']}
                    </p>
                    <p style="font-size:15px">
                    &nbsp;
                    오존 : {row['oz_data_y']}
                    </p>
                </td>
            </tr>
        </table>
    """
    html = folium.Html(html,script=True, width=300, height=150) # popup을 html로 열고, dataframe에 각 열의 name 값 불러오기
    popup = folium.Popup(html=html, max_width='100%')
    folium.Marker([row['Address_1'], row['Address_2']], popup=popup,  icon=folium.Icon(icon='info-sign', color='red'), tooltip=tooltip).add_to(marker_cluster) # dataframe에 각 열의 위도,경도 값 불러오기

minimap = plugins.MiniMap() # minimap 추가
m.add_child(minimap)

m.save('templates/maps.html') # html로 저장

# csv, pandas를 이용하여 folium 시각화 방법
# df = pd.read_csv('mtngps.csv', encoding='utf-8') # read csv file, makemtngps_csv.py와 연결해서 사용
# # df.shape # (100,3) 100개의 행과 3개의 열로 이루어졌다는 것을 확인
# # df.head() # 데이터 위에서부터  미리보기
# m = folium.Map(location=[36.70,127.90], zoom_start=8) # map을 열었을때의 시작 화면

# # iterrrows()함수보다 apply()함수(+lamda)가 data처리가 더 빠름
# for index, row in df.iterrows(): # pandas for문, iterrows는 dataframe의 행을 나타냄
#     tooltip = 'Click!'
#     html = f"""
#     <body>
#     <h1 id="name">{row['C_name']}</h1><br>
#     <id="mimage" img src='images/1.jpg' width='40' height='40'>
#     <h3 id="text">hi</h3><br>
#     </body>
#     """
#     #html = folium.Html(row['C_name'],script=True) # popup을 html로 열고, dataframe에 각 열의 name 값 불러오기
#     f_html = folium.Html(html,script=True) # popup을 html로 열고, dataframe에 각 열의 name 값 불러오기
#     popup = folium.Popup(html, max_width=500)
#     folium.Marker([row['C_gps1'], row['C_gps2']], popup=popup, icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(m) # dataframe에 각 열의 위도,경도 값 불러오기

# minimap = plugins.MiniMap() # minimap 추가
# m.add_child(minimap)

# m.save('templates/maps.html') # html로 저장

