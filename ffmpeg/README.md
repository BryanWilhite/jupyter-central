# `ffmpeg`: Hyper fast Audio and Video encoder

<https://ffmpeg.org/>

**wiki:** <https://trac.ffmpeg.org/>

This folder contains my notes on my use of `ffmpeg`. Currently, the assumptions here are:

- [ ] when [the docs](https://trac.ffmpeg.org/wiki/HowToBurnSubtitlesIntoVideo) say that the `subtitles` filter can “draw” subtitles, this means making a named subtitle ‘track’ that can be turned on and off in media players
- [ ] the `split` filter [📖 [docs](http://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit)] can take an `*.mp4` or `*.mkv` file as input and split it by timecode precisely without ‘loss’
- [ ] the `concat` filter [📖 [docs](http://ffmpeg.org/ffmpeg-filters.html#concat)] can take `*.mp4` or `*.mkv` files and concatenate them by timecode precisely without ‘damage’

## alternatives to the `split` and `concat` filters

“[FFMPEG - Trimming and combining MKV files](https://n-v-o.github.io/2021-06-23-FFMPEG/)” is an awesome article that shows how to split and concatenate media files without using filters.

## `meta.json`

`meta.json` is shared by all of the Jupyter notebooks to obscure magic strings for (bad) security purposes. The form of this file is currently:

```json
{
    "rootDirectory": ""
}
```

@[BryanWilhite](https://twitter.com/BryanWilhite)
