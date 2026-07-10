from fastapi import FastAPI
import json

app = FastAPI()

@app.get('/')
def home():
    return{"message":"Wellcome to Home Page"}

def load_data():
    with open('students.json')as f:
        data = json.load(f)
        return data

@app.get('/students')
def show_students():
    return load_data()

    
@app.get('/students/{roll}')
def get_student(roll):
    data = load_data()
    return data.get(roll)


def save_data(data):
    with open('students.json','w') as f:
        json.dump(data,f)


@app.post('/students/{roll}')
def add_student(roll,student):
    data = load_data()
    if roll in data:
        return {
            "message":"Student Already Exist",
            "Error":"404",
            "data":""
        }
    
    data[roll] = student
    save_data(data)
    return{
        "message":"User Created Successfully!!",
        "status": "200",
        "data":student
    }

@app.put('/students/{roll}')
def update_student(roll,student):   
    data = load_data()
    if roll not in data:
        return {
            "message":"Student Does not Exist"
        }

    data[roll] = student
    save_data(data)
    return{
        "message":"Student Updated Successfully!!",
        "Status":200,
        "data":student
    }

@app.delete('/students/{roll}')
def delete_student(roll):
    data = load_data()
    if roll not in data:
        return {
            "message":"Student Does not Exist",
            "status":'404',
            "data":""
        }    

    delete_student = data.pop(roll)
    save_data(data)
    return{
        "message":"Student deleted succcessfully!!",
        "status":"200",
        "data" : delete_student
    }
