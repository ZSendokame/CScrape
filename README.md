# CScrape
Web scraping from the terminal is useful, you have access to any script or binary there. But, sometimes,<br>
cURL and Regex is not enough.

# Install
```
pip install git+https://github.com/ZSendokame/CScrape.git
```

# Use
```sh
python -m cscrape --url https://alansierra.pages.dev/blog/  # URL to scrape
                  --select "a > h2"  # CSS Selector to use
                  --oneliner "'\n'.join([tag.text for tag in nodes])"  # Optional oneliner
                  --params "{'json': {'message': 'visit Alans website.'}}"  # Modify request parameters (Requests)

# -> Returns

# Cambio de dominio
# Estoy Transcribiendo LLPSI
# Horario escolar KISS
# Consejos para tus dotfiles
# Software que uso
# Así funciona esta web
```