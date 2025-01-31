import re
import unittest

from playwright.sync_api import Page, expect, sync_playwright


class TestSecretaria(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch(headless=True, slow_mo=1000)
        cls.context = cls.browser.new_context()
        cls.context.set_default_timeout(5_000)



    def setUp(self):
        self.page = self.context.new_page()

        self.page.goto("http://10.31.2.177:8000/admin/login/?next=/admin/")
        self.page.get_by_text("Pule o conteúdo principal Administração do Django Alternar tema (tema atual:").click()
        self.page.locator("html").click()
        self.page.get_by_text("Pule o conteúdo principal Administração do Django Alternar tema (tema atual:").click()
        self.page.get_by_label("Usuário:").click()
        self.page.get_by_label("Senha:").click()
        self.page.get_by_label("Usuário:").click()
        self.page.get_by_label("Usuário:").click()
        self.page.get_by_label("Usuário:").press("CapsLock")
        self.page.get_by_label("Usuário:").fill("T")
        self.page.get_by_label("Usuário:").press("CapsLock")
        self.page.get_by_label("Usuário:").fill("Tester")
        self.page.get_by_label("Usuário:").click()
        self.page.get_by_label("Usuário:").press("ArrowLeft")
        self.page.get_by_label("Usuário:").press("ArrowLeft")
        self.page.get_by_label("Usuário:").press("ArrowLeft")
        self.page.get_by_label("Usuário:").press("ArrowLeft")
        self.page.get_by_label("Usuário:").press("ArrowLeft")
        self.page.get_by_label("Usuário:").fill("tester")
        self.page.get_by_label("Senha:").click()
        self.page.get_by_label("Senha:").press("CapsLock")
        self.page.get_by_label("Senha:").press("CapsLock")
        self.page.get_by_label("Senha:").fill("Esc@laFPFtech1")
        self.page.get_by_role("button", name="Acessar").click()
        self.page.locator("#content-start").click()

    def test_authenticacao_valida(self) -> None:
        self.page.get_by_role("button", name="Acessar").click()
        self.page.get_by_role("link", name="Adicionar").click()
        self.page.get_by_label("Data nascimento:").click()
        self.page.get_by_label("Data nascimento:").fill("30/01/2026")
        self.page.get_by_label("Matricula:").click()
        self.page.get_by_role("button", name="Salvar", exact=True).click()
        self.page.get_by_role("group").locator("div").filter(has_text="Este campo é obrigatório. Nome:").get_by_role(
            "listitem").click()
        self.page.get_by_label("Nome:").click()
        self.page.get_by_label("Nome:").press("CapsLock")
        self.page.get_by_label("Nome:").fill("P")
        self.page.get_by_label("Nome:").press("CapsLock")
        self.page.get_by_label("Nome:").fill("Pedrinho")
        self.page.get_by_label("Cpf:").click()
        self.page.get_by_label("Cpf:").fill("0122130910")
        self.page.get_by_label("Matricula:").click()
        self.page.get_by_label("Matricula:").fill("1")
        self.page.locator("#aluno_form div").filter(has_text="Idade: -").nth(1).click()
        self.page.get_by_role("button", name="Salvar", exact=True).click()
        self.assertTrue(self.page.locator("xpath//tr[contais(,,'Pedrinho')]").is_visible())

    def test_pesquisar_aluno(self) -> None:
        pass

    def teardown(self) -> None:
        self.page.close()