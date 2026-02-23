from fastapi import FastAPI

app = FastAPI()

# Home page
@app.get("/")
def home():
    return {"message": "Student Result API is running"}

# Result prediction API
@app.get("/result")
def result(name: str, marks: int):

    percentage = marks

    if marks >= 90:
        grade = "A"
        status = "Excellent"
    elif marks >= 75:
        grade = "B"
        status = "Very Good"
    elif marks >= 50:
        grade = "C"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    return {
        "Student Name": name,
        "Marks": marks,
        "Percentage": percentage,
        "Grade": grade,
        "Status": status
    }