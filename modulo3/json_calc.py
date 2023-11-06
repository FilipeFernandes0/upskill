import json

def read_json_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def extract_specific_values(data):
    values = [item["value"] for item in data["items"]]
    return values
def modify_values(data):
    for item in data["items"]:
        item["value"] *= 2
    
def generate_report(value):
    report = "report: \n"
    for i,value in enumerate(value, start=1):
        report += f"{i}.{value}\n"
    return report

file_path = "data.json"
data = read_json_data(file_path)

specificvalues= extract_specific_values(data)
print("valores especificos:", specificvalues)

modify_values(data)

report = generate_report(specificvalues)
print(report)