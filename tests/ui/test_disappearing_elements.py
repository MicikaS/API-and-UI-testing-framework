# smoke test
def test_page_loaded(disappearing_elements_page):
    assert disappearing_elements_page.is_page_loaded()


# smoke test
def test_buttons_exist(disappearing_elements_page):
    assert disappearing_elements_page.are_elements_visible()


def test_click_on_home(disappearing_elements_page):
    disappearing_elements_page.click_on_home()


def test_click_on_about(disappearing_elements_page):
    disappearing_elements_page.click_on_about()


def click_on_contact_us(disappearing_elements_page):
    disappearing_elements_page.click_on_contact_us()


def test_click_on_portfolio(disappearing_elements_page):
    disappearing_elements_page.click_on_portfolio()


def test_gallery_exist(disappearing_elements_page):
    assert disappearing_elements_page.gallery_exist()


def test_click_on_gallery(disappearing_elements_page):
    assert disappearing_elements_page.click_on_gallery()
