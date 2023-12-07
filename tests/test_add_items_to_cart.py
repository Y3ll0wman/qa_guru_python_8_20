import requests
from allure import step

from selene import browser, be, have


class TestAddItemsToCart:
    product_details = browser.element('td.product')
    shopping_cart = browser.element('#topcartlink')
    unit_price = browser.element('.product-unit-price')
    product_subtotal = browser.element('.product-subtotal')
    order_total = browser.element('.product-price.order-total')

    def go_to_cart(self):
        with step('Open shopping cart'):
            self.shopping_cart.should(be.clickable).click()

    @staticmethod
    def open_browser_with_added_item(url=None, data=None):
        with step('Open browser with added item'):
            results = requests.post(url=url,
                                    data=data)

            cookies = results.cookies.get('Nop.customer')

            browser.open('/')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})

    def test_add_build_your_own_expensive_computer(self, api_url, browser_chrome):
        # GIVEN
        self.open_browser_with_added_item(url=f'{api_url}/addproducttocart/details/74/1',
                                          data={'product_attribute_74_5_26': '81',
                                                'product_attribute_74_6_27': '83',
                                                'product_attribute_74_3_28': '86',
                                                'addtocart_74.EnteredQuantity': '1'})

        # WHEN
        browser.open('/')
        self.go_to_cart()

        # THEN
        with step('product details check'):
            self.product_details.should(have.text('Build your own expensive computer'))
            self.product_details.should(have.text('Processor: Medium [+15.00]'))
            self.product_details.should(have.text('RAM: 2 GB'))
            self.product_details.should(have.text('HDD: 320 GB'))
            self.unit_price.should(have.text('1815.00'))
            self.product_subtotal.should(have.text('1815.00'))
            self.order_total.should(have.text('1815.00'))

    def test_add_14_1_inch_laptop(self, api_url, browser_chrome):
        # GIVEN
        self.open_browser_with_added_item(url=f'{api_url}/addproducttocart/catalog/31/1/1')

        # WHEN
        browser.open('/')
        self.go_to_cart()

        # THEN
        with step('product details check'):
            self.product_details.should(have.text('14.1-inch Laptop'))
            self.unit_price.should(have.text('1590.00'))
            self.product_subtotal.should(have.text('1590.00'))
            self.order_total.should(have.text('1590.00'))

    def test_add_computing_and_internet_book(self, api_url, browser_chrome):
        # GIVEN
        self.open_browser_with_added_item(url=f'{api_url}/addproducttocart/catalog/13/1/1')

        # WHEN
        browser.open('/')
        self.go_to_cart()

        # THEN
        with step('product details check'):
            self.product_details.should(have.text('Computing and Internet'))
            self.unit_price.should(have.text('10.00'))
            self.product_subtotal.should(have.text('10.00'))
            self.order_total.should(have.text('10.00'))

    def test_add_digital_slr_camera_12_2_mpixel(self, api_url, browser_chrome):
        # GIVEN
        self.open_browser_with_added_item(url=f'{api_url}/addproducttocart/details/18/1')

        # WHEN
        browser.open('/')
        self.go_to_cart()

        # THEN
        with step('product details check'):
            self.product_details.should(have.text('Digital SLR Camera - Black'))
            self.unit_price.should(have.text('670.00'))
            self.product_subtotal.should(have.text('670.00'))
            self.order_total.should(have.text('670.00'))

    def test_add_black_and_white_diamond_heart(self, api_url, browser_chrome):
        # GIVEN
        self.open_browser_with_added_item(url=f'{api_url}/addproducttocart/catalog/14/1/1')

        # WHEN
        browser.open('/')
        self.go_to_cart()

        # THEN
        with step('product details check'):
            self.product_details.should(have.text('Black & White Diamond Heart'))
            self.unit_price.should(have.text('130.00'))
            self.product_subtotal.should(have.text('130.00'))
            self.order_total.should(have.text('130.00'))
