import time

from selenium import webdriver

from automatisation_inventory import extract_product_data

webdriver = webdriver.Firefox()
webdriver.get("https://www.google.com/search?sca_esv=fd3dfaa5d0878a4a&q=rundhals+t+shirts&uds=ALYpb_ncDc7jTlmw6Mmq7NjuX5c-krZrbWIimbBhISByURS8lXak35PrAyIzq5H-EgOhuhkkXro_RpTHSVkw5PSxGlz6fO9AFcvFUuWVDuZseRQgO_Z10XxRDQLmCM7Jogr5iuWNIc6YKHFHPxi6TkIsmkC7-IbRtKP0MxY-QMUwVmrJmbmOXDaGxA97ysYNZBWjylzaAJFk&udm=3&sa=X&ved=2ahUKEwjaoqTvwJCVAxV1XfEDHY4QBE0QxKsJKAV6BAgjEAE&ictx=0&biw=1036&bih=731&dpr=1.25")
webdriver.set_window_position(-1000, 0)
webdriver.maximize_window()
time.sleep(30)

data = extract_product_data(webdriver)
print(data)

webdriver.quit()