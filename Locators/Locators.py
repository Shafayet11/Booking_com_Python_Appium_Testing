from selenium.webdriver.common.by import By


class RegisterLocators():
    Click_register_button = (By.XPATH, "//android.widget.TextView[@text='Create your account']")
    Email_textbox = (By.ID, 'com.booking:id/identity_text_input_edit_text')
    click_continue = (By.ID, 'com.booking:id/identity_landing_social_button_text')
    password = (By.ID, 'com.booking:id/identity_text_input_edit_text')
    confirm_password = (By.XPATH, '(//android.widget.EditText)[2]')
    click_create_ac = (By.ID, 'com.booking:id/identity_landing_social_button_text')


class SignInLocators:
    click_SignIn_with_email = (By.XPATH, "//android.widget.TextView[@text='Sign in with email']")
    Insert_email = (By.ID, 'com.booking:id/identity_text_input_edit_text')
    continue_button = (By.ID, 'com.booking:id/identity_landing_social_button_text')
    Insert_password = (By.ID, 'com.booking:id/identity_text_input_edit_text')
    SignIn_Button_locator = (By.XPATH, '(//android.widget.TextView)[4]')
    Start_search = (By.ID, 'com.booking:id/genius_onbaording_bottomsheet_cta')


class StaysButtonLocator():
    stays_button = (By.XPATH, '(//android.widget.LinearLayout)[9]')
    stay_textbox_locator = (By.XPATH, '//android.widget.TextView[@text="Enter your destination"]')
    stay_textseacrh_locator = (By.ID, 'com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content')
    select_one = (By.XPATH, '(//android.view.ViewGroup)[2]')
    Select_Date = (By.XPATH, '(//android.widget.TextView)[6]')

    click_date = (By.XPATH, '//android.view.View[@content-desc="29 June 2022"]')
    click_another_date = (By.XPATH, '//android.view.View[@content-desc="30 June 2022"]')
    select_dates_locator = (By.XPATH, '(//android.widget.Button)[@text="Select dates"]')
    Person_type_locator = (By.XPATH, '(//android.widget.TextView)[@text="1 room · 2 adults · 0 children"]')
    Increase_rooms = (By.XPATH, '(//android.widget.Button)[2]')
    Increase_children = (By.XPATH, '(//android.widget.Button)[6]')
    select_child_age = (By.XPATH, '(//android.widget.TextView)[@text="10"]')
    Click_Apply = (By.XPATH, '(//android.widget.Button)[@text="APPLY"]')
    click_search = (By.XPATH, '(//android.widget.Button)[@text="Search"]')


class CarRentalLocator():
    signin_and_save = (By.XPATH, '(//android.widget.Button)[@text="Sign in to save"]')
    click_car_rental_locator = (By.XPATH, '(//android.widget.TextView)[@text="Car rental"]')
    click_pickup = (By.XPATH, '(//android.widget.EditText)[@text="Pickup location"]')

    select_location = (By.XPATH, '(//android.widget.LinearLayout)[5]')
    click_date = (By.XPATH, '(//android.widget.EditText)[2]')
    select_pick_date = (By.XPATH, '(//android.view.View)[@content-desc="28 June 2022"]')
    select_drop_date = (By.XPATH, '(//android.view.View)[@content-desc="30 June 2022"]')

    select_date = (By.ID, 'com.booking:id/facet_date_picker_confirm')
    go_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    click_search = (By.XPATH, '(//android.widget.Button)[@text="Search"]')


class TaxiLocators():
    signin_and_save = (By.XPATH, '(//android.widget.Button)[@text="Sign in to save"]')
    select_Taxi_tab = (By.XPATH, '(//android.widget.LinearLayout)[11]')
    select_pickup_loc = (By.XPATH,'(//android.widget.EditText)[@text="Enter pick-up location"]')
    select_destination_loc = (By.XPATH,'(//android.widget.EditText)[@text="Enter destination"]')
    select_location = (By.XPATH, '(//android.widget.RelativeLayout)[7]')

    select_dates = (By.XPATH, '(//android.widget.TextView)[4]')
    select_current_date = (By.ID, '(//android.widget.Button)[@text="Confirm"]')
    check_prices = (By.XPATH, '(//android.widget.Button)[@text="See prices"]')


class AttractionsLocator():
    select_Attractions_locator = (By.XPATH, '(//android.widget.LinearLayout)[12]')
    search_destination = (By.XPATH, '//android.widget.EditText')
