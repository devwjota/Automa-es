from playwright.sync_api import sync_playwright

# A função 'sync_playwright' gerencia o ciclo de vida do Playwright
with sync_playwright() as p:
    # Inicia um navegador (chromium é o motor do Chrome/Edge)
    # headless=False significa que você verá a janela do navegador abrir
    navegador = p.chromium.launch(headless=False) 

    # Cria uma nova página (aba)
    pagina = navegador.new_page()

    # 1. Navega até o site do Google
    pagina.goto("https://www.google.com.br")

    # 2. Localiza a caixa de busca pelo seu título e a preenche
    # O Playwright espera a caixa de busca estar pronta antes de agir
    caixa_de_busca = pagina.get_by_title("Pesquisar")
    caixa_de_busca.fill("Playwright")

    # 3. Pressiona a tecla Enter
    caixa_de_busca.press("Enter")

    # 4. Espera a página de resultados carregar (implicitamente)
    # e tira uma foto da tela
    print("Tirando screenshot...")
    pagina.screenshot(path="resultado_playwright.png")

    # Fecha o navegador
    navegador.close()

print("Automação concluída! Verifique o arquivo 'resultado_playwright.png'.")