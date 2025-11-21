import os
from tempfile import TemporaryDirectory
from django.http import FileResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render
from yt_dlp import YoutubeDL


def index(request):
    return render(request, 'index.html')


def baixarVideos(request):
    url = request.GET.get('url')
    formato = request.GET.get('formato')

    if not url:
        return HttpResponseBadRequest("A URL é obrigatória.")
    
    if formato not in ["mp3", "mp4"]:
        formato = "mp3"  # fallback

    with TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, '%(title)s.%(ext)s')

        # Configurações padrão
        ydl_opts = {
            'outtmpl': output_path,
            'quiet': True,
            'no_warnings': True,
        }

        # MP3 → extrai só o áudio
        if formato == "mp3":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })

        # MP4 → baixa vídeo + áudio e converte pra MP4
        elif formato == "mp4":
            ydl_opts.update({
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                'merge_output_format': 'mp4'
            })

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
        except Exception as e:
            raise Http404(f"Erro ao baixar/convert: {e}")

        # acha o arquivo final
        final_file = None
        for file in os.listdir(tmpdir):
            if file.endswith(formato):
                final_file = os.path.join(tmpdir, file)
                break

        if not final_file:
            raise Http404("Falha ao gerar arquivo final.")

        filename = os.path.basename(final_file)
        response = FileResponse(open(final_file, 'rb'), as_attachment=True, filename=filename)
        return response
