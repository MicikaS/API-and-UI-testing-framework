# smoke test
def test_is_page_loaded(login_page):
    assert login_page.is_page_loaded()


def test_bad_login(login_page):
    username = "MikaMikic"
    password = "Sifra123"
    assert login_page.login(username, password) == "Your username is invalid!\n×"


def test_login(login_page):
    username = "tomsmith"
    password = "SuperSecretPassword!"
    assert login_page.login(username, password) == "You logged into a secure area!\n×"
