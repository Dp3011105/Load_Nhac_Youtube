# # import os
# # import io
# # import re
# # import shutil
# # import urllib.parse
# # from flask import Flask, Response, render_template, request, jsonify
# # from yt_dlp import YoutubeDL

# # app = Flask(__name__)

# # # Thư mục tạm để lưu file
# # TEMP_DIR = "temp"
# # if not os.path.exists(TEMP_DIR):
# #     os.makedirs(TEMP_DIR)

# # def download_youtube_audio(url):
# #     try:
# #         # Kiểm tra URL YouTube hợp lệ
# #         youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
# #         if not re.match(youtube_regex, url):
# #             raise Exception("URL YouTube không hợp lệ")

# #         # Cấu hình yt-dlp để tải âm thanh gốc
# #         ydl_opts = {
# #             'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio',  # Ưu tiên m4a, rồi webm
# #             'noplaylist': True,  # Chỉ tải video đơn
# #             'outtmpl': os.path.join(TEMP_DIR, '%(title)s.%(ext)s'),  # Lưu file tạm
# #             'quiet': True,
# #         }

# #         # Tải âm thanh và lấy thông tin
# #         with YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=True)
# #             # Lấy đường dẫn file thực tế từ yt_dlp
# #             file_path = info['requested_downloads'][0]['filepath']
# #             ext = info.get('ext', 'm4a')
# #             filename = os.path.basename(file_path)
# #             title = info.get('title', filename)

# #         # Kiểm tra sự tồn tại của file
# #         if not os.path.exists(file_path):
# #             raise Exception(f"File không tồn tại: {file_path}")

# #         # Đọc file vào buffer
# #         buffer = io.BytesIO()
# #         with open(file_path, 'rb') as f:
# #             buffer.write(f.read())

# #         # Xóa file tạm trên server
# #         try:
# #             os.remove(file_path)
# #         except Exception as e:
# #             print(f"Lỗi khi xóa file tạm: {str(e)}")

# #         # Kiểm tra buffer
# #         buffer.seek(0)
# #         if buffer.getbuffer().nbytes == 0:
# #             raise Exception("Không tải được dữ liệu âm thanh")

# #         return buffer, filename, ext, title
# #     except Exception as e:
# #         raise Exception(f"Lỗi khi tải âm thanh: {str(e)}")

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     if request.method == 'POST':
# #         youtube_url = request.form.get('youtube_url')
# #         if not youtube_url:
# #             return jsonify({'error': 'Vui lòng nhập URL YouTube'}), 400

# #         try:
# #             # Tải âm thanh vào bộ nhớ
# #             audio_buffer, filename, ext, title = download_youtube_audio(youtube_url)
# #             # Chọn mimetype dựa trên định dạng
# #             mimetype = 'audio/mp4' if ext == 'm4a' else 'audio/webm'
# #             # Mã hóa tên file để hỗ trợ ký tự Unicode
# #             encoded_filename = urllib.parse.quote(filename.encode('utf-8'))
# #             return Response(
# #                 audio_buffer.getvalue(),
# #                 mimetype=mimetype,
# #                 headers={
# #                     'Content-Disposition': f"inline; filename*=UTF-8''{encoded_filename}",
# #                     'X-Song-Title': urllib.parse.quote(title.encode('utf-8'))
# #                 }
# #             )
# #         except Exception as e:
# #             return jsonify({'error': str(e)}), 400

# #     return render_template('index.html')

# # @app.route('/get_title', methods=['POST'])
# # def get_title():
# #     youtube_url = request.form.get('youtube_url')
# #     if not youtube_url:
# #         return jsonify({'error': 'Vui lòng nhập URL YouTube'}), 400

# #     try:
# #         youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
# #         if not re.match(youtube_regex, youtube_url):
# #             raise Exception("URL YouTube không hợp lệ")

# #         ydl_opts = {
# #             'quiet': True,
# #             'noplaylist': True,
# #         }
# #         with YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(youtube_url, download=False)
# #             title = info.get('title', 'Unknown Title')
# #         return jsonify({'title': title})
# #     except Exception as e:
# #         return jsonify({'error': str(e)}), 400

# # if __name__ == '__main__':
# #     try:
# #         port = int(os.getenv('PORT', 5000))
# #         app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
# #     finally:
# #         # Xóa thư mục tạm khi tắt server
# #         shutil.rmtree(TEMP_DIR, ignore_errors=True)





# import os
# import io
# import re
# import shutil
# import urllib.parse
# from flask import Flask, Response, render_template, request, jsonify
# from yt_dlp import YoutubeDL

# app = Flask(__name__)

# # Thư mục tạm để lưu file
# TEMP_DIR = "temp"
# if not os.path.exists(TEMP_DIR):
#     os.makedirs(TEMP_DIR)

# def download_youtube_audio(url):
#     try:
#         # Kiểm tra URL YouTube hợp lệ
#         youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
#         if not re.match(youtube_regex, url):
#             raise Exception("URL YouTube không hợp lệ")

#         # Cấu hình yt-dlp để tải âm thanh gốc
#         ydl_opts = {
#             'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio',  # Ưu tiên m4a, rồi webm
#             'noplaylist': True,  # Chỉ tải video đơn
#             'outtmpl': os.path.join(TEMP_DIR, '%(title)s.%(ext)s'),  # Lưu file tạm
#             'quiet': True,
#         }

#         # Tải âm thanh và lấy thông tin
#         with YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             # Lấy đường dẫn file thực tế từ yt_dlp
#             file_path = info['requested_downloads'][0]['filepath']
#             ext = info.get('ext', 'm4a')
#             filename = os.path.basename(file_path)
#             title = info.get('title', filename)
#             thumbnail = info.get('thumbnail', '')

#         # Kiểm tra sự tồn tại của file
#         if not os.path.exists(file_path):
#             raise Exception(f"File không tồn tại: {file_path}")

#         # Đọc file vào buffer
#         buffer = io.BytesIO()
#         with open(file_path, 'rb') as f:
#             buffer.write(f.read())

#         # Xóa file tạm trên server
#         try:
#             os.remove(file_path)
#         except Exception as e:
#             print(f"Lỗi khi xóa file tạm: {str(e)}")

#         # Kiểm tra buffer
#         buffer.seek(0)
#         if buffer.getbuffer().nbytes == 0:
#             raise Exception("Không tải được dữ liệu âm thanh")

#         return buffer, filename, ext, title, thumbnail
#     except Exception as e:
#         raise Exception(f"Lỗi khi tải âm thanh: {str(e)}")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         youtube_url = request.form.get('youtube_url')
#         if not youtube_url:
#             return jsonify({'error': 'Vui lòng nhập URL YouTube'}), 400

#         try:
#             # Tải âm thanh vào bộ nhớ
#             audio_buffer, filename, ext, title, thumbnail = download_youtube_audio(youtube_url)
#             # Chọn mimetype dựa trên định dạng
#             mimetype = 'audio/mp4' if ext == 'm4a' else 'audio/webm'
#             # Mã hóa tên file để hỗ trợ ký tự Unicode
#             encoded_filename = urllib.parse.quote(filename.encode('utf-8'))
#             return Response(
#                 audio_buffer.getvalue(),
#                 mimetype=mimetype,
#                 headers={
#                     'Content-Disposition': f"inline; filename*=UTF-8''{encoded_filename}",
#                     'X-Song-Title': urllib.parse.quote(title.encode('utf-8')),
#                     'X-Song-Thumbnail': thumbnail
#                 }
#             )
#         except Exception as e:
#             return jsonify({'error': str(e)}), 400

#     return render_template('index.html')

# @app.route('/get_title', methods=['POST'])
# def get_title():
#     youtube_url = request.form.get('youtube_url')
#     if not youtube_url:
#         return jsonify({'error': 'Vui lòng nhập URL YouTube'}), 400

#     try:
#         youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
#         if not re.match(youtube_regex, youtube_url):
#             raise Exception("URL YouTube không hợp lệ")

#         ydl_opts = {
#             'quiet': True,
#             'noplaylist': True,
#         }
#         with YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(youtube_url, download=False)
#             title = info.get('title', 'Unknown Title')
#             thumbnail = info.get('thumbnail', '')
#         return jsonify({'title': title, 'thumbnail': thumbnail})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     try:
#         port = int(os.getenv('PORT', 5000))
#         app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
#     finally:
#         # Xóa thư mục tạm khi tắt server
#         shutil.rmtree(TEMP_DIR, ignore_errors=True)






import os
import io
import re
import shutil
import urllib.parse
from flask import Flask, Response, render_template, request, jsonify
from yt_dlp import YoutubeDL
import logging

app = Flask(__name__)

# Thiết lập logging để debug trên Replit
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thư mục tạm để lưu file
TEMP_DIR = "temp"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def download_youtube_audio(url):
    try:
        # Kiểm tra URL YouTube hợp lệ
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
        if not re.match(youtube_regex, url):
            raise Exception("URL YouTube không hợp lệ")

        # Cấu hình yt-dlp để tải âm thanh gốc
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio',  # Ưu tiên m4a, rồi webm
            'noplaylist': True,  # Chỉ tải video đơn
            'outtmpl': os.path.join(TEMP_DIR, '%(title)s.%(ext)s'),  # Lưu file tạm
            'quiet': True,
            'socket_timeout': 30,  # Thêm timeout để tránh treo trên Replit
            'retries': 3,  # Thử lại 3 lần nếu lỗi
        }

        # Tải âm thanh và lấy thông tin
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = info['requested_downloads'][0]['filepath']
            ext = info.get('ext', 'm4a')
            filename = os.path.basename(file_path)
            title = info.get('title', filename)
            thumbnail = info.get('thumbnail', '')

        # Kiểm tra sự tồn tại của file
        if not os.path.exists(file_path):
            raise Exception(f"File không tồn tại: {file_path}")

        # Đọc file vào buffer
        buffer = io.BytesIO()
        with open(file_path, 'rb') as f:
            buffer.write(f.read())

        # Xóa file tạm trên server
        try:
            os.remove(file_path)
            logging.info(f"Đã xóa file tạm: {file_path}")
        except Exception as e:
            logging.error(f"Lỗi khi xóa file tạm: {str(e)}")

        # Kiểm tra buffer
        buffer.seek(0)
        if buffer.getbuffer().nbytes == 0:
            raise Exception("Không tải được dữ liệu âm thanh")

        return buffer, filename, ext, title, thumbnail
    except Exception as e:
        logging.error(f"Lỗi khi tải âm thanh: {str(e)}")
        raise Exception(f"Lỗi khi tải âm thanh: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.form.get('youtube_url')
        if not youtube_url:
            return jsonify({'error': 'Vui lòng nhập URL YouTube'}), 400

        try:
            audio_buffer, filename, ext, title, thumbnail = download_youtube_audio(youtube_url)
            mimetype = 'audio/mp4' if ext == 'm4a' else 'audio/webm'
            encoded_filename = urllib.parse.quote(filename.encode('utf-8'))
            logging.info(f"Tải thành công: {title}")
            return Response(
                audio_buffer.getvalue(),
                mimetype=mimetype,
                headers={
                    'Content-Disposition': f"inline; filename*=UTF-8''{encoded_filename}",
                    'X-Song-Title': urllib.parse.quote(title.encode('utf-8')),
                    'X-Song-Thumbnail': thumbnail
                }
            )
        except Exception as e:
            logging.error(f"Lỗi endpoint /: {str(e)}")
            return jsonify({'error': str(e)}), 400

    return render_template('index.html')

@app.route('/get_title', methods=['POST'])
def get_title():
    youtube_url = request.form.get('youtube_url')
    if not youtube_url:
        return jsonify({'error': 'Vui lòng nhập URL YouTube'}), 400

    try:
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
        if not re.match(youtube_regex, youtube_url):
            raise Exception("URL YouTube không hợp lệ")

        ydl_opts = {
            'quiet': True,
            'noplaylist': True,
            'socket_timeout': 30,  # Thêm timeout
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get('title', 'Unknown Title')
            thumbnail = info.get('thumbnail', '')
        logging.info(f"Lấy tiêu đề thành công: {title}")
        return jsonify({'title': title, 'thumbnail': thumbnail})
    except Exception as e:
        logging.error(f"Lỗi endpoint /get_title: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    try:
        port = int(os.getenv('PORT', 8080))  # Mặc định port 8080 trên Replit
        app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
    except Exception as e:
        logging.error(f"Lỗi khi chạy server: {str(e)}")
    finally:
        # Xóa thư mục tạm khi tắt server
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        logging.info("Đã xóa thư mục tạm khi tắt server")
