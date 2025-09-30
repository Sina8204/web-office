import os

class tags():
    def __init__(self):
        self.tag_name = ""
        self.Class = None
        self.id = None
        self.partition = ""
        self.partitions_path = ""
        self.tags_folder = ""
        self.css_path = ""
        self.close = ""
        self.__style = {}
    
    def creat_tag (self , name : str , Class = None , id = None  , text = "" , partition = "", close ="</>"):
        self.tag_name = name
        self.Class = Class
        self.id = id
        self.partition = partition + ".tg"
        self.partitions_path += f"{self.partition}"
        self.tags_folder += f"{self.tag_name}"
        self.close = close
        #
        with open (self.tags_folder , "w") as file :
            file.write(f"<{self.tag_name}")
            if self.Class != None :
                file.write(f" class='{self.Class}'")
            if self.id != None :
                file.write(f" id='{self.id}'")
            file.write(f">{text}")
            if self.close == "</x>" :
                file.write(f"</{self.tag_name}>\n")
            elif self.close == "</>" :
                file.write(f"\n</{self.tag_name}>\n")
            else :
                file.write(f"\n")
    #######################################################
    def style(self , style : dict , call_type = None):
        call_by_class = f".{self.Class}"
        call_by_id = f"#{self.id}"
        call_by_class_and_id = f".{self.Class} > #{self.id}"
        call_by_id_and_class = f"#{self.id} > .{self.Class}"
        match call_type:
            case "class" : self.__style = {"call": call_by_class }
            case "id" : self.__style = {"call": call_by_id}
            case "class_id" : self.__style = {"call": call_by_class_and_id}
            case "id_class" : self.__style = {"call": call_by_id_and_class}
            case _ : self.__style = {"call": self.tag_name}
        self.__style.update(style)
        print(self.__style)
    #######################################################
    def creat_css(self):
        #self.css_path += f"{self.partition}.css"
        with open(self.css_path , "w") as file :
            file.write(f"{self.__style["call"]}" + "{\n")
            for i in self.__style.keys():
                if i == "call":
                    continue
                file.write(f"\t{i}: " + self.__style[i] + ";\n")
            file.write("\t}\n")
    #######################################################
    def add_tag (self):
        self.creat_css()
        with open(self.tags_folder , "r") as file:
            self.tag_html = file.read()
        # with open(self.css_path , "r") as file:
        #     self.tag_css = file.read()
        with open (self.partitions_path , "a+") as file:
            file.write(self.tag_html)
        # with open (self.css_path , "a+")as file:
        #     file.write(self.tag_css + "\n\n")
        
        
# test = tags()
# test.creat_tag(name="title" , Class="ti", id="id1", partition="head" , close="</x>")
# test.style(
#     {
#         "width" : "20",
#         "height" : "50",
#         "color" : "red"
#     }
#     , call_type="class_id"
# )
# if input("do you want to enter : ") == "y":
#     test.add_tag()
# else:
#     pass