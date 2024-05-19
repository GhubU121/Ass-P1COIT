import requests

def get_species_list(coordinate, radius):

    base_url = "https://apps.des.qld.gov.au/species/?op=getspecieslist"
    lat, lon = coordinate["latitude"], coordinate["longitude"]
    params = {
        "kingdom": "animals",
        "circle": f"{lat},{lon},{radius}"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if "SpeciesSightingSummariesContainer" in data:
        return data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
    else:
        return None

def get_surveys_by_species(coordinate, radius, taxonid):

    base_url = "https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies"
    lat, lon = coordinate["latitude"], coordinate["longitude"]
    params = {
        "taxonid": str(taxonid),
        "circle": f"{lat},{lon},{radius}"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data.get("features", [])

def search_sightings(taxonid, coordinate, radius):
    surveys = get_surveys_by_species(coordinate, radius, taxonid)
    incidental_sightings = [s for s in surveys if s.get("properties", {}).get("SiteCode") == "INCIDENTAL"]
    return incidental_sightings

def earliest(sightings):
    return min(sightings, key=lambda x: x.get("properties", {}).get("StartDate"), default=None)

def sort_by_date(sightings):
    return sorted(sightings, key=lambda x: x.get("properties", {}).get("StartDate"))

def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(f"Date: {sighting.get('properties', {}).get('StartDate')}, Location: {sighting.get('properties', {}).get('LocalityDetails')}")

if __name__ == "__main__":
    coordinate = {"latitude": -16.92, "longitude": 145.777}
    radius = 100000
    taxonid = 860
    
    #list of species
species_list = get_species_list(coordinate, radius)
    print("Species List:", species_list)
    
    #surveys by species
surveys = get_surveys_by_species(coordinate, radius, taxonid)
    print("Surveys:", surveys)
    
    # For incidental sightings
incidental_sightings = search_sightings(taxonid, coordinate, radius)
    print("Incidental Sightings:", incidental_sightings)
    
    # Display and sort these sightings if any
if incidental_sightings:
    display_sightings(incidental_sightings)
else:
    print("No incidental sightings found.")