import pandas as pd
import json
from pandas.core.frame import DataFrame 

# Open and load JSON file
f = open('/Users/rasmushenriksen/Desktop/BACHELOR-SOFTWARE/femte_og_sjette/femte_semester/Project/Python/src/Data_set/tnm.json')
data = json.load(f)
f.close()
data = json.dumps(data)
json_acceptable_string = data.replace("'", "\"")
d = json.loads(data)

## Extracting META data from TNM
meta_data = {}

for meta in d['meta_data']:
    meta_data = d['meta_data']

## Extraxting node and edge data from TNM
node_data = []
edge_data = []
edge_from_node_id = []
edge_to_node_id = []

# Node data
for node in d['nodes']:
    node_data.append(d['nodes'][node]['data'])

# Edge data
for node in d['nodes']:
    for edge in d['nodes'][node]['edges']:
        edge_data.append(d['nodes'][node]['edges'][edge]['data'])

# Edge from_node_id
for node in d['nodes']:
    for edge in d['nodes'][node]['edges']:
        edge_from_node_id.append(d['nodes'][node]['edges'][edge]['from_node_id'])

# Edge to_node_id
for node in d['nodes']:
    for edge in d['nodes'][node]['edges']:
        edge_to_node_id.append(d['nodes'][node]['edges'][edge]['to_node_id'])

# Adding from_node_id to the edge data 
for x in range(len(edge_from_node_id)):
    edge_data[x].update( {'from_node_id' : edge_from_node_id[x]})

# Adding to_node_id to the edge data 
for x in range(len(edge_to_node_id)):
    edge_data[x].update( {'to_node_id' : edge_to_node_id[x]})

#  ## Extracting node_ids and edge_ids from TNM
node_ids = []
edge_ids = []

for node in d['nodes']:
    node_ids.append(node)

for node in d['nodes']:
    for edge in d['nodes'][node]['edges']:
        edge_ids.append(d['nodes'][node]['edges'][edge]['to_node_id'])

## Create dictionaries with node_ids and edge_ids as keys and node_data and edge_data as values
nodes_dict = dict(zip(node_ids, node_data))
edges_dict = dict(zip(edge_ids, edge_data))

## Set up lists and keys for final dictionary
from_node_id = []
to_node_id = []
length = []
slope = []
type = []
type_max_speed = []
set_max_speed = []
# recommend_speed = []
mean_speed = []
daily_year = []
daily_july = []
daily_trucks = []
daily_10_axle = [] 
fuel_station = []
max_axle_load = []
max_height = []
max_length = []
max_weight = []


complete_dict = { 'from_node_id' : None, 'to_node_id': None, 'length' : None, 'slope' : None, 'type' : None, 
'type_max_speed' : None, 'set_max_speed' : None, 'recommended_speed' : None, 'mean_speed' : None, 'daily_year' : None, 
'daily_july' : None, 'daily_trucks' : None, 'daily_10_axle' : None, 'fuel_station' : None, 'max_axle_load' : None,
 'max_height' : None, 'max_length' : None, 'max_weight' : None}

keys = ['from_node_id', 'to_node_id', 'length', 'slope', 'type', 'type_max_speed', 'set_max_speed', 'mean_speed', 'daily_year',
 'daily_july', 'daily_trucks', 'daily_10_axle', 'fuel_station',
 'max_axle_load', 'max_height', 'max_length', 'max_weight' ]

values = [from_node_id, to_node_id, length, slope, type, type_max_speed, set_max_speed, mean_speed, daily_year, daily_july,
daily_trucks, daily_10_axle, fuel_station, max_axle_load, max_height, max_length, max_weight]

# Populate value-lists with values from dictionaries
for x in edge_ids:
    from_node_id.append(edges_dict[x]['from_node_id'])
    to_node_id.append(edges_dict[x]['to_node_id'])
    length.append(edges_dict[x]['length'])
    slope.append(edges_dict[x]['slope'])
    type.append(edges_dict[x]['type'])
    type_max_speed.append(edges_dict[x]['type_max_speed'])
    set_max_speed.append(edges_dict[x]['set_max_speed'])
    # recommend_speed.append(edges_dict[x]('recommend_speed'))
    mean_speed.append(edges_dict[x]['mean_speed'])
    daily_year.append(edges_dict[x]['daily_year'])
    daily_july.append(edges_dict[x]['daily_july'])
    daily_trucks.append(edges_dict[x]['daily_trucks'])
    daily_10_axle.append(edges_dict[x]['daily_10_axle'])
    fuel_station.append(edges_dict[x]['fuel_station'])
    max_axle_load.append(edges_dict[x]['max_axle_load'])
    max_height.append(edges_dict[x]['max_height'])
    max_length.append(edges_dict[x]['max_length'])
    max_weight.append(edges_dict[x]['max_weight'])

## Build final dictionary
for x in range(len(keys)):
    complete_dict[keys[x]] = values[x]

## Create pandas Datafram
df = pd.DataFrame(complete_dict)

### ENJOY THE VIEW
print(df)
