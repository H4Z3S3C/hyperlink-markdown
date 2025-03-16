from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def generate_embed():
    title = request.args.get("title")
    description = request.args.get("description")
    image = request.args.get("image")
    url = request.args.get("url")
    author = request.args.get("author")
    colour = request.args.get("colour")

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta property="og:type" content="website">
    """

    if title:
        html_content += f'<meta property="og:title" content="{title}">\n'
        html_content += f'<title>{title}</title>\n'
    
    if description:
        html_content += f'<meta property="og:description" content="{description}">\n'
        html_content += f'<meta name="twitter:description" content="{description}">\n'
    
    if image:
        html_content += f'<meta property="og:image" content="{image}">\n'
        html_content += f'<meta name="twitter:image" content="{image}">\n'
    
    if url:
        html_content += f'<meta property="og:url" content="{url}">\n'
    
    if author:
        html_content += f'<meta name="twitter:card" content="summary_large_image">\n'
        html_content += f'<meta name="twitter:title" content="{title if title else "No Title"}">\n'

    if colour:
        html_content += f'<meta name="theme-color" content="{colour}">\n'

    html_content += """
    </head>
    <body>
    """

    if title:
        html_content += f"<h1>{title}</h1>\n"
    
    if description:
        html_content += f"<p>{description}</p>\n"
    
    if image:
        html_content += f'<img src="{image}" alt="Embed Image" style="max-width:100%;">\n'

    if author:
        html_content += f"<p><small>By {author}</small></p>\n"

    html_content += """
    </body>
    </html>
    """
    
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
