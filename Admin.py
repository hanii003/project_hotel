from Staff import *
from Room import *
class Admin(Person):
    def __init__(self,unique_id,name,contact_info):
        super().__init(self,unique_id,name,contact_info)
        self.staff_members = []
    def update_contact_details(self,new_contact_info):
        self.contact_info = new_contact_info
    def creat_staff_account(self,staff_details):
        staff_member = Staff(staff_details["unique_id"],
                             staff_details["name"],
                             staff_details["contact_info"],
                             staff_details["role"]
                             )
        return staff_member
                             
    def romove_staff_member(self,staff_id):
        for staff_member in self.staff_members:
            if staff_member.unique_id == staff_id:
                self.staff_members.remove(staff_member)
                print("removed!")
            
    def update_staff_role(self,staff_id,new_role):
        for staff_member in self.staff_members:
            if staff_member.unique_id == staff_id:
                staff_member.role = new_role
                print("updated")
    def approve_maintenance_request(self,room_id,maintenance_type):
        pass
    def generate_payroll_report(self):
        pass
    
