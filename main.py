from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def generate_markdown():
    title = request.args.get("title", "Title")
    description = request.args.get("description", "No description provided.")
    url = request.args.get("url", "https://example.com")
    image = request.args.get("image", "")
    author = request.args.get("author", "Unknown Author")
    footer = request.args.get("footer", "")

    markdown_parts = []

    if title:
        markdown_parts.append(f"[{title}]({url})")
    if description:
        markdown_parts.append(f"{description}")
    if author:
        markdown_parts.append(f"by {author}")
    if image:
        markdown_parts.append(f"![Image]({image})")
    if footer:
        markdown_parts.append(f"> *{footer}*")

    markdown_output = "\n\n".join(markdown_parts)

    return f"<pre>{markdown_output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
