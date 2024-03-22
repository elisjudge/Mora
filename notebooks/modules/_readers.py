import json

def read_json_lines(filepath:str):
   """ This generator function opens json file and reads lines one by one """
   with open(filepath, 'r', encoding="UTF-8") as json_file:
      data = json.load(json_file)
      for line in data:
          try:
              yield line
          except Exception as e:
              print(f"Error: {e}")
              continue
          

def read_json_file(filepath:str):
    """ Loads entire file into memory"""
    with open(filepath, 'r', encoding="UTF-8") as json_file:
      return json.load(json_file)
    
          
