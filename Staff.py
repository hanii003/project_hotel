class Staff(Person):
    def __init__(self,unique_id,name,contact_info,role):
        super().__init__(self,unique_id,name,contact_info)
        self.role = role
    def update_contact_details(self,new_contact_info):
        self.contact_info = new_contact_info
    def __str__(self):
        return f"ID : {self.unique_id},Name : {self.name},Caontact Info : {self.contact_info},Role : {self.role}"
    def book_guest(self,guest_id,room_id):
        pass
    def check_out_guest(self,guest_id):
        pass
    def mark_room_cleaned(self,room_id):
        pass
    def request_cleaning_supplies(self):
        pass
    def report_repair_done(self,room_id):
        pass
    def order_repair_materials(self,material_list):
        pass
