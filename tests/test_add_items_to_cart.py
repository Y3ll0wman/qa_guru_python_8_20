import requests
from selene import browser, be, have


def test_add_items_to_cart(api_url, browser_chrome):
    # GIVEN
    results = requests.post(url=f"{api_url}/addproducttocart/details/74/1",
                            data={'product_attribute_74_5_26': '81',
                                  'product_attribute_74_6_27': '83',
                                  'product_attribute_74_3_28': '86',
                                  'addtocart_74.EnteredQuantity': '1'})

    cookies = results.cookies.get('Nop.customer')

    browser.open('/')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})

    # WHEN
    browser.open('/')
    browser.element('#topcartlink').should(be.clickable).click()

    # THEN
    browser.element('td.product').should(have.text('Build your own expensive computer'))
