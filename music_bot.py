import gradio as gr

# Hàm phát nhạc từ link YouTube
def play_music(youtube_url):
    # lấy ID video từ link
    import re
    m = re.search(r"(?:v=|be/|shorts/)([A-Za-z0-9_-]{11})", youtube_url)
    if not m:
        return "❌ Link không hợp lệ!", None
    video_id = m.group(1)

    # nhúng player YouTube
    embed_html = f"""
    <iframe width="560" height="315"
    src="https://www.youtube.com/embed/{video_id}?autoplay=1"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe>
    """
    return "▶️ Đang phát:", embed_html

# Tạo giao diện
with gr.Blocks() as demo:
    gr.Markdown("# 🎵 Music Bot")
    url_input = gr.Textbox(label="Nhập link YouTube")
    output_text = gr.Textbox(label="Trạng thái")
    output_player = gr.HTML()
    url_input.submit(play_music, inputs=url_input, outputs=[output_text, output_player])

demo.launch()