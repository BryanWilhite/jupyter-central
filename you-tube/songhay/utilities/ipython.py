from IPython import display

"""
According to “[How to Download YouTube Video Thumbnails](https://www.howtogeek.com/751633/how-to-download-youtube-video-thumbnails/),” for every video at `www.youtube.com/watch?v=<id>` there is a maximum-resolution thumbnail at `img.youtube.com/vi/<id>/maxresdefault.jpg`. The following function, `display_videos`, intends to take advantage of these conventions:
"""

def display_video(video_id, title, image_name):
    figure = ''.join([
        '<figure style="display: inline-block;">',
        f'<a href="https://www.youtube.com/watch?v={video_id}">',
        f'<img alt="{title}" src="https://img.youtube.com/vi/{video_id}/{image_name}" width="480" />',
        '</a>',
        '<br />',
        f'<small>{title}</small>',
        '</figure>',
    ])
    i_frame = display.YouTubeVideo(video_id)._repr_html_()

    return f'{figure}{i_frame}'

def display_videos(picks):
    html = list()
    for video_id, title in picks:
        image_name = 'maxresdefault.jpg'
        no_max_res = '[no-max-res]'
        if video_id.endswith(no_max_res):
            image_name = 'hqdefault.jpg'
            video_id = video_id.replace(no_max_res, '')
        html.append(display_video(video_id, title, image_name))
    return display.HTML(''.join(html))
