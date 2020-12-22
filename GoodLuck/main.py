from flask import Flask, render_template

# 데이터 분석용 
import pandas as pd

temp = pd.read_csv('서울 통합 교통사고.csv') 
# 시군구에서 군만 분리해서 gus 리스트에 삽입
gus=[]
for item in temp['시군구']:
    gus.append(item.split()[1][:-1])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html', gus = set(gus)) 

if __name__ == "__main__":
    app.run(debug=True)