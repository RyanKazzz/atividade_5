import unittest

from playwright.sync_api import sync_playwright


class todo_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch(headless=False, slow_mo=1000)
        cls.context = cls.browser.new_context()
        cls.context.set_default_timeout(5_000)

    def test_criar_todo(self) -> None:

        self.page = self.context.new_page()
        self.page.goto("https://vanilton.net/web-test/todos/#/")
        self.page.get_by_placeholder("What needs to be done?").fill("meu Primeiro Todo")
        self.page.get_by_placeholder("What needs to be done?").press("Enter")
        self.assertEqual(self.page.locator(".view label").inner_text(), "meu Primeiro Todo")


    def tearDown(self) -> None:
        self.page.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.context.close()
        cls.browser.close()
        cls.p.stop()


if __name__ == '__main__':
    unittest.main()
