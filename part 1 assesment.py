def display_menu():
    print("Help")
    print("===")
    print("The following commands are recognised.")
    #Formatiing the menu to show align
    print('Display help {:>20}  wildlife> help'.format(''))
    print('Display animal species in a city   wildlife> species Cairns')
    print('Display venonmous species wildlife> species Cairns venomous')
    print('Display animal sightings in a city wildlife> sightings Cairns 1039')
    print('Exit the application {:>12}  wildlife> exit\n'.format(''))


def main():
    display_menu()
    while(True):
        comm = input().split(' ')
        print("\n")
        if(comm[0]=="exit"):
            exit(0)
        elif(comm[0]=="help"):
            display_menu()
        elif(comm[0]=="species"):
            
            if len(comm)>2:
                display_species(filter_venomous(search_species(comm[1])))
            else:
                display_species(search_species(comm[1]))
            
        elif(comm[0]=="sightings"):
            display_sightings(search_sightings(comm[2],comm[1]))
        else:
            print("ERROR: Unrecognized Command. Please check and try again.")
            display_menu()

def search_species(city):
    output= [ {"Species":{"AcceptedCommonName":"dolphin", "PestStatus":"Nil"}}, {"Species":{"AcceptedCommonName":"snake","PestStatus":"Venomous"}} ]
    
    return output

def display_species(species_list):
    index = 1
    for species in species_list:
        c_name = species["Species"]["AcceptedCommonName"]
        pest_status = species["Species"]["PestStatus"]
        print(f"Species {index}:")
        print(f"  Accepted Common Name: {c_name}")
        print(f"  Pest Status: {pest_status}")
        print()
        index += 1


def search_sightings(taxonid,city):
    sightings = [{"properties":{"StartDate":"1999-11-15","LocalityDetails":"Tinaroo"}}]
    return sightings
    

def display_sightings(sightings):
    for sighting in sightings:
        print(f"Date: {sighting['properties']['StartDate']}")
        print(f"Location: {sighting['properties']['LocalityDetails']}")
        print("------------------------\n")

# filter_venomous method 
def filter_venomous(species_list):
    return [specie for specie in species_list if specie['Species']['PestStatus'] == "Venomous"]

main()