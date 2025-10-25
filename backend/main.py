
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File, HTTPException
from pdfplumber import open as pdf_open


app = FastAPI(title="Customer Sign up")
#credentials object
class Info(BaseModel):
    Name: str
    Mail: str
    Address:str
    phoneno:str
    password:str
    passwordchecker:str

    
#test request

@app.get("/")
async def root():
    return {"message": "Customer Sign up"}

@app.get("/fillinfo")
async def fillinfo(info:Info):
    
    if info.password!=info.passwordchecker:
        raise HTTPException(status_code=403,detail="Password do not match")
        
    with open("../textdb.txt", "r") as file6:
        l01=file6.read()
        if info.Mail in l01:
            raise HTTPException(status_code=403,detail="The mail is already registered")
    
    p='Name :'+ info.Name +'\n Email:'+ info.Mail + '\n Password :'+info.password
    print("Passing the password check and mail check")
    with open("../temp.txt","w") as file1:
        print("Temp data passed",p)
        l=file1.write(p)
        file1.close()
    with open("../temp.txt","r") as file5:
        l0=file5.read()
    
        print("Temmp data in the tep file",l0)
    #return "Save it " #when testing using FastAPI
    return l
    
@app.post("/save")
async def save():
    
    try:
    
        with open("../temp.txt","r") as file2:
        
            l=file2.read()
            print("The file has been read",l)
        with open("../textdb.txt","a+") as file3:
            
            file3.write('\n')
            l1=file3.write(l)

            file3.close()
            print("Data passed in the file",l)

            
            
        with open("../textdb.txt","r") as file4:
                
                
                l2=file4.read()
                print("The file has been written to the file",l2)
    except Exception as e:
        return {"message":e.args}

        
    return "The info has been saved"
    

@app.post("/upload")
async def uploadfile(file12: UploadFile):
    try:
        print("inside try except block")
        file_path=f"../saved_KYC_Files/{file12.filename}"
        with open(file_path, "wb") as f:
            e=file12.file.read()
            f.write(file12.file.read())
            f.close()
            print("Writing in the file path",e)
            print("File uploaded in path")
        with open(file_path,"r") as f1:
            
            print("File exists in path ")

        return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}

""" @app.post("/upload")
def upload(file12: UploadFile = File(...)):
    try:
        with open(file12.filename, 'wb') as f:
            while contents := file12.file.read(1024 * 1024):
                f.write(contents)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        file12.file.close()

    return {"message": f"Successfully uploaded {file12.filename}"} """