import sys
from datetime import datetime

def process_uber_data(input_file, output_file):
    region_data = {}


    weekday_mapping = {
        "Monday": "MON",
        "Tuesday": "TUE",
        "Wednesday": "WED",
        "Thursday": "THU",
        "Friday": "FRI",
        "Saturday": "SAT",
        "Sunday": "SUN"
    }

    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                region, date_str, vehicles, trips = parts

    
                try:
                    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
                    year = date_obj.year
                    month = date_obj.month
                    day = date_obj.day

    
                    day_name = date_obj.strftime("%A")
                    day_code=weekday_mapping.get(day_name, "Unknown")
                except ValueError:
                    year, month, day, day_name = "Unknown", "Unknown", "Unknown", "Unknown"

                key = f"{region},{day_code}"
                if key in region_data:
                    region_data[key][0] += int(vehicles)
                    region_data[key][1] += int(trips)
                else:
                    region_data[key] = [int(vehicles), int(trips)]

    
    with open(output_file, 'w', encoding='utf-8') as output:
        for key, values in region_data.items():
            region, day_name = key.split(',')
            vehicles, trips = values
            output.write(f"{region},{day_name} {vehicles},{trips}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python UBERStudent<Your ID>.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_uber_data(input_file, output_file)

