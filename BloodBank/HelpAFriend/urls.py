from django.urls import include, path

from HelpAFriend import views 

urlpatterns = [
		path(r'registration/',views.Registration_User),
		path(r'login/',views.Login_User),
		path(r'submit/',views.Submit),
		path(r'index/',views.Index),
		path(r'auth/',views.Auth_User),
		path(r'search/',views.Search_Page),
		path(r'search_donor/$',views.Search_Donor),
		path(r'post_request/',views.Post_Request),
		path(r'post_req/$',views.Post_Req),
		path(r'search_bank/$',views.Bank_List),
		path(r'bloodbank_registration/',views.BloodBank_Registration),
		path(r'submit_bloodbank/$',views.Submit_BloodBank),
		path(r'bloodbank_details/$',views.BloodBank_Details),
		path(r'update_units/$',views.Update_Units),
		path(r'edit_profile/$',views.Edit_Profile),
		path(r'update_details/$',views.Update_Details),
		path(r'user_home/$',views.User_Home),
		path(r'change_password/$',views.Change_Password),
		path(r'change_pass/$',views.Change_Pass),
		path(r'logout/$',views.Logout),
		path(r'edit_bb_profile/$',views.Edit_BB_Profile),
		path(r'update_bb_details/$',views.Update_BB_Details),
		path(r'bloodbank_home/$',views.BloodBank_Home),
		path(r'forgot_password/$',views.Forgot_Password),
		path(r'new_password/$',views.New_Password),
		path(r'enter_otp/$',views.Enter_Otp),
		path(r'generate_otp/$',views.Generate_Otp),
		path(r'verify_otp/$',views.Verify_Otp),
		path(r'update_password/$',views.Update_Password),
		path(r'aboutus/',views.AboutUS),
	]

