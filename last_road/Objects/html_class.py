import os

from tags_class import tags

class html(tags):
    def __init__(self , path , project_name):
        super().__init__()
        self.path = path
        self.project_name = project_name
        self.structs_path = f"{self.path}/structs"
        self.tags_path = f"{self.path}/tags"
        os.makedirs(self.path , exist_ok=True)
        os.makedirs(self.structs_path , exist_ok=True)
        os.makedirs(self.tags_path , exist_ok=True)
        self.files_name = ["head.tg" , "header.tg" , "body.tg" , "footer.tg"]
        self.html_path = f"{self.path}/{self.project_name}.html"
        self.css_path = f"{self.path}/{self.project_name}_style.css"
        for i in self.files_name :
            with open(f"{self.path}/structs/{i}" , "w+") as file :
                file.write("")
        ############33
        self.partitions_path = f"{self.structs_path}/{self.partition}"
        self.tags_folder = f"{self.tags_path}/"
        #self.css_path = f"{self.tags_path}/"
    
    def html_config(self):
        with open(self.html_path , "w+") as html_file:
            html_file.write("<!DOCTYPE html>\n<html>\n<head>\n")
            with open(f"{self.path}/structs/head.tg" , "r") as head_file :
                html_file.write(f"{head_file.read()}\n</head>\n\n<body>\n")
            with open(f"{self.path}/structs/header.tg" , "r") as header_file :
                html_file.write(f"{header_file.read()}\n</header>\n\n")
            with open(f"{self.path}/structs/body.tg" , "r") as body_file :
                html_file.write(f"{body_file.read()}\n\n<footer>\n")
            with open(f"{self.path}/structs/footer.tg" , "r") as footer_file :
                html_file.write(f"{footer_file.read()}\n</footer>\n</body>\n\n")


app = html("web_office" , "zoo_web")

app.creat_tag("title" , "t1" , "id1" , "hello world" , "head" , "</>")
app.style({
        "width" : "20",
        "height" : "50",
        "color" : "red"
    }
)
app.creat_css()
app.add_tag()
app.html_config()