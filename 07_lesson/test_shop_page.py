from shop_page import OnlineStorePage


def test_purchase_flow_firefox(driver):
    store_page = OnlineStorePage(driver)
    store_page.open()
    store_page.login()
    store_page.produkt_in_basket()
    store_page.checkout()

    total_price_text = store_page.placing_an_order(
        first_name="Марина",
        last_name="Кова",
        post_code="123456"
    )

    expected_sum = "58.29"
    assert expected_sum in total_price_text
    print("\n[58.29] Сумма верная: True")
