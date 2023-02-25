import os

# running just with pytest in console
HEROKUAPP = "https://the-internet.herokuapp.com"

# running with docker
# HEROKUAPP = os.environ.get("HEROKUAPP")
HEROKUAPP_LOGIN = HEROKUAPP + "/login"
HEROKUAPP_DISSAPEARING = HEROKUAPP + "/disappearing_elements"
