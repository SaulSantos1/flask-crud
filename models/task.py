class Task:
    def __init__(self,id,title,description,completed=False) -> None:
        self.__id = id
        self.__title = title
        self.__description = description
        self.__completed = completed
    
    def __str__(self) -> str:
        return f"Tarefa de ID {self.__id} cadastrado com sucesso"
    
    def getId(self):
        return self.__id
    
    def setId(self,id):
        self.__id = id

    def getTitle(self):
        return self.__title
    
    def setTitle(self,title):
        self.__title = title

    def getDescription(self):
        return self.__description
    
    def setDescription(self,description):
        self.__description = description

    def getCompleted(self):
        return self.__completed
    
    def setCompleted(self,completed):
        self.__completed = completed

    def to_dict(self):
        return {
            "id":self.__id,
            "title":self.__title,
            "description":self.__description,
            "completed":self.__completed
        }