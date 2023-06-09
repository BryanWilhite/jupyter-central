from IPython import display

"""
According to “[How to Download YouTube Video Thumbnails](https://www.howtogeek.com/751633/how-to-download-youtube-video-thumbnails/),” for every video at `www.youtube.com/watch?v=<id>` there is a maximum-resolution thumbnail at `img.youtube.com/vi/<id>/maxresdefault.jpg`. The following function, `display_videos`, intends to take advantage of these conventions:
"""

def display_video(video_id, title, image_name):
    figure = ''.join([
        '<div id="figure-block" style="display: inline-block;margin:2rem;">',
        f'<a href="https://www.youtube.com/watch?v={video_id}">',
        f'<img alt="{title}" src="https://img.youtube.com/vi/{video_id}/{image_name}" width="480" />',
        '</a>',
        '<br />',
        f'<small>{title}</small>',
        '</div>',
    ])

    return figure

def display_videos(picks):
    html = list()
    for video_id, title in picks:
        res_name = 'maxresdefault'
        video_id_array = video_id.split(',')
        if len(video_id_array) > 1:
            video_id = video_id_array[0]
            res_name = video_id_array[1]
        html.append(display_video(video_id, title, f'{res_name}.jpg'))
    return display.HTML(''.join(html))
