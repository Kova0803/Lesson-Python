import allure
from LoginPage import LoginPage
from Mainshoppage import Mainshoppage
from CartPage import CartPage
from checkoutPage import checkoutPage


@allure.story("тестирование интернет-магазина одежды")
def test_purchase_flow_firefox(driver):
    # 1. Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()

    # 2. Добавление товара в корзину
    main_page = Mainshoppage(driver)
    main_page.produkt_in_basket()

    main_page.checkout()

    # 3. Переход к оформлению из корзины
    cart_page = CartPage(driver)
    cart_page.checkout()

    # 4. Оформление заказа
    checkout_page = checkoutPage(driver)
    total_price_text = checkout_page.placing_an_order(
        first_name="Марина", last_name="Кова", post_code="123456"
    )

    assert total_price_text == "Total: $58.29"
    print("\n[58.29] Сумма верная: True")
