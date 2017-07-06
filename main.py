from flask import Flask, render_template, request, send_file, send_from_directory
from azure.storage.file import FileService
from azure.storage.file import ContentSettings

app = Flask(__name__)
@app.route("/")
def hello():
        return render_template("upload.html")

@app.route("/number1",methods = ['POST'])
def num1():
  t = {}
  i = 1
  file_service = FileService(account_name='mystorge', account_key='0T4f/dzyV7AIw4a9bevK5ysML0qP55CEWEqJyJWXyr6fKRxowLq8tL7mep/MfSc//mcQggeH1+K79A4HUDug3w==')
  generator = file_service.list_directories_and_files('image1')
  for file_or_dir in generator:
      t[i] = file_or_dir.name
      i += 1
  return render_template("table.html" , t = t)

@app.route("/number2" ,methods = ['POST'])
def num2():
  file  = request.form['name']
  file += ".jpg"
  file_service = FileService(account_name='mystorge',account_key='0T4f/dzyV7AIw4a9bevK5ysML0qP55CEWEqJyJWXyr6fKRxowLq8tL7mep/MfSc//mcQggeH1+K79A4HUDug3w==')
  filename = 'out.jpg'
  file_service.get_file_to_path('image1', None, file, filename)
  return send_file(filename)

@app.route("/number3" ,methods = ['POST'])
def num3():
    file = request.form['filename']
    file += ".jpg"
    file_service = FileService(account_name='mystorge',account_key='0T4f/dzyV7AIw4a9bevK5ysML0qP55CEWEqJyJWXyr6fKRxowLq8tL7mep/MfSc//mcQggeH1+K79A4HUDug3w==')
    file_service.create_file_from_path('image1',None,file,file,content_settings=ContentSettings(content_type='image/png'))
    return "<h1> File Uploaded sucessfully</h1>"


if __name__ == "__main__":
         app.run()