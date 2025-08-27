import json
import plotly.express as px
from pathlib import Path
path=Path('eq_data_30_day_m1.geojson') 
contents=path.read_text(encoding='utf-8')
all_eq_data=json.loads(contents)
path=Path('readable_eq_data.geojson')
readable_contents=json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
all_eq_dicts=all_eq_data['features']
# print(len(all_eq_dicts))
lons=[f['geometry']['coordinates'][0] for f in all_eq_dicts]
lats=[f['geometry']['coordinates'][1] for f in all_eq_dicts]
mags=[f['properties']['mag'] for f in all_eq_dicts]
titles=[f['properties']['title']for f in all_eq_dicts]

title='Global Earthquakes'
fig=px.scatter_geo(lat=lats,lon=lons,title=title,size=mags,
                   color=mags,
                   color_continuous_scale='viridis',
                   labels={'color':'Magnitude'},
                   projection='natural earth',
                   hover_name=titles)
fig.show()
