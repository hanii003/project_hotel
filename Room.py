class Room:
    def __init__(self,room_number,status,type_):
        self.room_number = room_number
        self.status = status
        self.type_ = type_
    def set_room_status(self,new_status):
        self.status = new_status
    def schedule_room_maintenance(self, maintenance_type) :
        pass
    def __str__(self):
        return f"Room Number : {self.room_number}, Status : {self.status},Type : {self.type_}"
