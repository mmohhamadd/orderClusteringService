from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
from k_means_constrained import KMeansConstrained
from django.shortcuts import render
import folium
# Create your views here.
def maps(request):
    n = request.GET['n'] 
    colors = [
        'red', 'blue', 'green', 'purple', 'orange', 'darkred',
        'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue' 
    ]
    datas = pd.read_csv('sample2.csv')
    geos = datas[['lat','lng']]
    clf = KMeansConstrained(
        n_clusters=int(n),
        size_min=round(len(datas)/int(n) - 5),
        size_max=round(len(datas)/int(n) + 5),
        random_state=0
    )
    clf.fit_predict(geos)
    datas['cluster']=clf.labels_
    datas.groupby('cluster')['lat'].count()
    map = folium.Map(location=[datas.iloc[0]['lng'], datas.iloc[0]['lat']], zoom_start=12)
    for _, row in datas.iterrows():
        folium.CircleMarker(
            location=[row["lng"], row["lat"]],
            radius=12, 
            weight=2, 
            tooltip=row['name'],
            fill=True, 
            fill_color=colors[int(row["cluster"])],
            color=colors[int(row["cluster"])],
        ).add_to(map)


    map = map._repr_html_()
    context = {
        'map': map,
    }
    return render(request, 'maps/maps.html', context)