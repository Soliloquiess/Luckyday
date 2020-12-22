import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

def make_pie_plot(label,target,gu_label,color):
    colors = sns.color_palette(color,len(label))

    labels_frequency = zip(label,target) 
    labels_frequency = sorted(labels_frequency,key=lambda x: x[1],reverse=True)
 
    sorted_labels = [x[0] for x in labels_frequency] ## 정렬된 라벨
    sorted_frequency = [x[1] for x in labels_frequency] ## 정렬된 빈도수

    plt.close()
    
    fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
    fig.set_facecolor('white') ## 캔버스 배경색을 하얀색으로 설정
    ax = fig.add_subplot() ## 프레임 생성
 
    pie = ax.pie(sorted_frequency, ## 파이차트 출력
       startangle=90, ## 시작점을 90도(degree)로 지정
       counterclock=False, ## 시계방향으로 그려짐
        colors = colors
        )
 
    total = np.sum(target) ## 빈도수 합
 
    threshold = 5
    sum_pct = 0 ## 퍼센티지
    count_less_5pct = 0 ## 5%보다 작은 라벨의 개수
    spacing = 0.1
    for i,l in enumerate(sorted_labels):
        ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2 ## 파이의 시작 각도와 끝 각도
        center, r = ax.patches[i].center, ax.patches[i].r ## 파이의 중심 좌표
    
    ## 비율 상한선보다 작은 것들은 계단형태로 만든다.
        if sorted_frequency[i]/total*100 < threshold:
            x = (r/2+spacing*count_less_5pct)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
            y = (r/2+spacing*count_less_5pct)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
            count_less_5pct += 1
        else:
            x = (r/2)*np.cos(np.pi/180*((ang1+ang2)/2)) + center[0] ## 텍스트 x좌표
            y = (r/2)*np.sin(np.pi/180*((ang1+ang2)/2)) + center[1] ## 텍스트 y좌표
    
    
    ## 퍼센티지 출력
        if i < len(label) - 1:
            sum_pct += float(f'{sorted_frequency[i]/total*100:.2f}')
            ax.text(x,y,f'{sorted_frequency[i]/total*100:.2f}%',ha='center',va='center',fontsize=12)
        else: ## 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
            ax.text(x,y,f'{100-sum_pct:.2f}%',ha='center',va='center',fontsize=12)
    
    plt.legend(pie[0],sorted_labels) ## 범례
    # plt.title(gu_label)
    # plt.show()
    return fig
    

    

def draw_plot(search,target,color):
    traffic_data = pd.read_csv('서울 통합 교통사고3.csv') 

    # 시군구에서 구만 분리해서 gus 리스트에 삽입
    gus=[]
    for item in traffic_data['시군구']:
        gus.append(item.split()[1])

    temp = traffic_data.copy()
    temp['구']=gus

    # 각 구별 법규위반을 사고번호를 기준으로 집계
    gu_target = temp.groupby(['구',target]).count()['사고번호'].unstack()
    gu_target = gu_target.fillna(0)

    gu_target_each_gu_value = []
    for i in range(len(gu_target.columns)): 
        gu_target_each_gu_value.append(gu_target.loc[search,:][i])

    output=io.BytesIO()
    FigureCanvasAgg(make_pie_plot(gu_target.columns,gu_target_each_gu_value,search,color)).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')