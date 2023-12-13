# Add contants here
# Normal constant
# BASE_URL = "https://restful-booker.herokuapp.com/"
#
# # Function constant
# def base_url():
#     return "https://restful-booker.herokuapp.com/"

# this is within class
class APIConstants():
    @staticmethod
    def base_url():
         return "https://restful-booker.herokuapp.com/"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking/"

    @staticmethod
    def url_create_token():
       return "https://restful-booker.herokuapp.com/auth"


# Update, Put, Patch, Delete need booking id
# this is not static method becoz due to different booking id

    def url_patch_put_delete_booking(self,booking_id):
       return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)

# Or
# def base_url():
#     return "https://restful-booker.herokuapp.com/"
#
#
# def url_create_booking():
#      return "https://restful-booker.herokuapp.com/booking/"
#
#
# def url_create_token():
#     return "https://restful-booker.herokuapp.com/auth"
#
#     # Update, Put, Patch, Delete need booking id
#     # this is not static method becoz due to different booking id
#
# def url_patch_put_delete_booking(booking_id):
#     return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
