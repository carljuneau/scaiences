from playwright.sync_api import sync_playwright

html_path = r'c:\Users\etien\Documents\GitHub\scaiences\studies\llm-rob\Juneau 2026.html'
pdf_path  = r'c:\Users\etien\Documents\GitHub\scaiences\studies\llm-rob\Juneau 2026.pdf'

footer = (
    '<div style="font-size:9px;width:100%;text-align:center;color:#555;">'
    '<span class="pageNumber"></span> / <span class="totalPages"></span>'
    '</div>'
)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + html_path.replace('\\', '/'))
    page.pdf(
        path=pdf_path,
        format='A4',
        margin={'top': '0.75in', 'bottom': '0.85in', 'left': '0.75in', 'right': '0.75in'},
        print_background=True,
        display_header_footer=True,
        footer_template=footer,
        header_template='<div></div>',
    )
    browser.close()
    print('Saved:', pdf_path)
