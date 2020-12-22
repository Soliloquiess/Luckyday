from flask import Flask, render_template, Response, request
import io

# 데이터 분석 및 시각화용
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

## 한글 깨짐 방지
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 기술 통계 그래프 그리는 모듈
from visualization import make_pie_plot, draw_plot

# 랜덤으로 그래프 나오는 부분 수정=>속도가 느려서 그런 것 같음/mysqldb 사용해보기
# 강남구 말고 강남 검색했을 때도 나오게 하기
# {% if not (search == '') and not (search.endswith('구')):
#     search = search + '구' %}

app = Flask(__name__)
traffic_data = pd.read_csv('서울 통합 교통사고3.csv') 

# 시군구에서 구만 분리해서 gus 리스트에 삽입
gus=[]
for item in traffic_data['시군구']:
    gus.append(item.split()[1])

temp = traffic_data.copy()
temp['구']=gus

@app.route('/')
def index():
    search = request.args.get("search", '')
    return render_template('main.html', gus = set(gus), search=search) # search는 사용자 입력

@app.route('/weather-plot-<search>.png')
def weather_plot(search):
    # 각 구별 법규위반을 사고번호를 기준으로 집계
    gu_weather = temp.groupby(['구','기상상태']).count()['사고번호'].unstack()
    gu_weather = gu_weather.fillna(0)

    gu_weather_each_gu_value = []
    for i in range(6): 
        gu_weather_each_gu_value.append(gu_weather.loc[search,:][i]) #여기서 강남 or 강남구

    output=io.BytesIO()
    FigureCanvasAgg(make_pie_plot(gu_weather.columns,gu_weather_each_gu_value,search,'light:b')).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/illegal-plot-<search>.png')
def illegal_plot(search):
    # 각 구별 법규위반을 사고번호를 기준으로 집계
    gu_illegal = temp.groupby(['구','법규위반']).count()['사고번호'].unstack()
    gu_illegal = gu_illegal.fillna(0)

    gu_illegal_each_gu_value = []
    for i in range(11): 
        gu_illegal_each_gu_value.append(gu_illegal.loc[search,:][i])
    
    output=io.BytesIO()
    FigureCanvasAgg(make_pie_plot(gu_illegal.columns,gu_illegal_each_gu_value,search,'ch:start=.2,rot=-.3')).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/roadInfo-plot-<search>.png')
def roadInfo_plot(search):
    # 각 구별 법규위반을 사고번호를 기준으로 집계
    gu_roadInfo = temp.groupby(['구','도로형태']).count()['사고번호'].unstack()
    gu_roadInfo = gu_roadInfo.fillna(0)

    gu_roadInfo_each_gu_value = []
    for i in range(11): 
        gu_roadInfo_each_gu_value.append(gu_roadInfo.loc[search,:][i])

    output=io.BytesIO()
    FigureCanvasAgg(make_pie_plot(gu_roadInfo.columns,gu_roadInfo_each_gu_value,search,'Blues')).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)