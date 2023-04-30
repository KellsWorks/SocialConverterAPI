from pytube import YouTube

class Youtube:
    
    def __init__(self):
        super(Youtube, self).__init__()
    
    def convert(url) :

        yt = YouTube(url)

        try:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if stream is not None:
                return stream.download(output_path=output_dir, filename=filename)
            else:
                return {'status': 'error', 'message': 'Could not find any streams with the desired properties.'}
        except Exception as e:
            return {'status': 'error', 'message': f'An error occurred: {str(e)}'}

    
    