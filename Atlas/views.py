"""
Atlas Views Configuration
"""

from django.shortcuts import render
from .models import Kingdoms, Locations
import json
from collections import defaultdict

from django.conf import settings
from django.core.files.storage import get_storage_class
storage_class = get_storage_class(settings.STATICFILES_STORAGE)


# Adjusting view of map as per the kingdom location
def find_view_value(pk):
    if pk=="1":
        return([10,14,6])
    elif pk=="2":
        return([12,8,7])
    elif pk=="3":
        return([35,18,6])
    elif pk=="5":
        return([25,18,5])
    elif pk=="6":
        return([-7,18,6])
    elif pk=="7":
        return([0,20,6])
    elif pk=="8":
        return([14,20,6])
    elif pk=="9":
        return([7,10,6])
    elif pk=="10":
        return([5,22,6])
    else:
        return([0,10,5])

# Main Landing page. Contains all the kingdom data.
def home(request):
    data = storage_class().open('Geojson_data/kingdoms_data.json')
    #data = open('static/Geojson_data/kingdoms_data.json')
    geodata = json.load(data)
    kingdoms=Kingdoms.objects.all()

    context={}
    layer_format={
            "type": "Feature",
            "properties": {
                "id":'',
                "name": '',
                "popupContent": ''
            },
            "geometry": {}
    }

    for kingdom in kingdoms:
        layer_format["properties"]["id"] = kingdom.id
        layer_format["properties"]["name"] = kingdom.name
        layer_format["properties"]["popupContent"] = kingdom.claimedby
        layer_format["geometry"] = geodata[str(kingdom.id)]
        context[kingdom.name]=json.dumps(layer_format)

    data.close()
    return render(request,'Atlas/home.html',{"context":context})

# Getting all the locations in a kingdom.
def visit_kingdom(request,pk):
    context = defaultdict(list)
    
    view_value = find_view_value(pk)
    
    context["view_value"] = view_value
    context["kingdom_num"] = pk
    
    
    location_data = storage_class().open('Geojson_data/locations_data.json')
    geodata = json.load(location_data)

    layer_format={
            "type": "Feature",
            "properties": {
                "name": '',
                "location_type": '',
                "awoiaf_url": '',
                "popupContent": ''
            },
            "geometry": {}
    }

    castles = Locations.objects.filter(location_type="Castle", kingdom_id=pk)
    cities = Locations.objects.filter(location_type="City", kingdom_id=pk)
    landmarks = Locations.objects.filter(location_type="Landmark", kingdom_id=pk)
    regions = Locations.objects.filter(location_type="Region", kingdom_id=pk)
    ruins = Locations.objects.filter(location_type="Ruin", kingdom_id=pk)
    towns = Locations.objects.filter(location_type="Town", kingdom_id=pk)

    for castle in castles:
        layer_format["properties"]["name"] = castle.name
        layer_format["properties"]["location_type"] = castle.location_type
        layer_format["properties"]["awoiaf_url"] = castle.awoiaf_url
        layer_format["properties"]["popupContent"] = castle.summary
        layer_format["geometry"] = geodata[str(castle.id)]
        context["castles"].append(json.dumps(layer_format))
    
    for city in cities:
        layer_format["properties"]["name"] = city.name
        layer_format["properties"]["location_type"] = city.location_type
        layer_format["properties"]["awoiaf_url"] = city.awoiaf_url
        layer_format["properties"]["popupContent"] = city.summary
        layer_format["geometry"] = geodata[str(city.id)]
        context["cities"].append(json.dumps(layer_format))

    for landmark in landmarks:
        layer_format["properties"]["name"] = landmark.name
        layer_format["properties"]["location_type"] = landmark.location_type
        layer_format["properties"]["awoiaf_url"] = landmark.awoiaf_url
        layer_format["properties"]["popupContent"] = landmark.summary
        layer_format["geometry"] = geodata[str(landmark.id)]
        context["landmarks"].append(json.dumps(layer_format))
    
    for region in regions:
        layer_format["properties"]["name"] = region.name
        layer_format["properties"]["location_type"] = region.location_type
        layer_format["properties"]["awoiaf_url"] = region.awoiaf_url
        layer_format["properties"]["popupContent"] = region.summary
        layer_format["geometry"] = geodata[str(region.id)]
        context["regions"].append(json.dumps(layer_format))

    for ruin in ruins:
        layer_format["properties"]["name"] = ruin.name
        layer_format["properties"]["location_type"] = ruin.location_type
        layer_format["properties"]["awoiaf_url"] = ruin.awoiaf_url
        layer_format["properties"]["popupContent"] = ruin.summary
        layer_format["geometry"] = geodata[str(ruin.id)]
        context["ruins"].append(json.dumps(layer_format))

    for town in towns:
        layer_format["properties"]["name"] = town.name
        layer_format["properties"]["location_type"] = town.location_type
        layer_format["properties"]["awoiaf_url"] = town.awoiaf_url
        layer_format["properties"]["popupContent"] = town.summary
        layer_format["geometry"] = geodata[str(town.id)]
        context["towns"].append(json.dumps(layer_format))
    
    location_data.close()        
    
    kingdom_data = storage_class().open('Geojson_data/kingdoms_data.json')
    geodata = json.load(kingdom_data)

    kingdoms = Kingdoms.objects.filter(id=pk)
    kingdom_note = {}

    layer_format={
            "type": "Feature",
            "properties": {
                "name": '',
                "awoiaf_url": '',
                "popupContent": ''
            },
            "geometry": {}
    }

    for kingdom in kingdoms:
        kingdom_note["name"] = layer_format["properties"]["name"] = kingdom.name
        kingdom_note["awoiaf_url"] = layer_format["properties"]["awoiaf_url"] = kingdom.awoiaf_url
        layer_format["properties"]["popupContent"] = "Read More below." 
        kingdom_note["summary"] = kingdom.summary
        kingdom_note["claimedby"] = kingdom.claimedby
        layer_format["geometry"] = geodata[str(kingdom.id)]
        context["kingdom_geodata"] = json.dumps(layer_format)
    kingdom_data.close()

    context["kingdom_note"] = kingdom_note

    return render(request,'Atlas/kingdom.html',context)
