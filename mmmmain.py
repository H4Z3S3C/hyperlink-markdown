from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def generate_markdown():
    # Get query parameters
    title = request.args.get("title", "Title")
    description = request.args.get("description", "No description provided.")
    url = request.args.get("url", "https://example.com")
    image = request.args.get("image", "")
    author = request.args.get("author", "Unknown Author")
    footer = request.args.get("footer", "")

    # Build Markdown response
    markdown_parts = []
    
    markdown_parts.append(f"**[{title}]({url})**")  # Title as a hyperlink
    markdown_parts.append(f"> {description}")  # Blockquote for description
    markdown_parts.append(f"_by {author}_")  # Italic author

    if image:
        markdown_parts.append(f"![Image]({image})")  # Image URL

    if footer:
        markdown_parts.append(f"> *{footer}*")  # Footer in italics

    markdown_output = "\n\n".join(markdown_parts)

    return f"<pre>{markdown_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
