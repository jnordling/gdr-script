import json
import csv


def main():
    with open('api.txt') as json_file:
        with open('data.csv',"w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            data = json.load(json_file)
            submission = data["result"]
            print (len(submission))
            for s in submission:
                api_id = s["_id"]["$id"]
                created = s["created"]
                status = s["status"]
                resources = s["resources"]
                for r in resources:
                    resource_name = r["name"]
                    resource_type = r["resourceType"]
                    if 'coordinates' in r:
                        resource_coordinates = r["coordinates"]
                        if (resource_coordinates):
                            lat = r["coordinates"][0]
                            lng = r["coordinates"][1]
                            writer.writerow([api_id, created, status,resource_name,resource_type,lat,lng])

                            # print (resource_coordinates)

            


main()