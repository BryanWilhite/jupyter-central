# Generating Responsive Images

The [work here](./generating-responsive-images.ipynb) is a search for responsive-image strategies for my studio.

## the named layouts requiring responsive images

For current Studio Publications, there are five named layouts:

1. the Open Graph protocol metadata
2. the “hero” index splash
3. the “hero” index lists
4. the prose opening image
5. the prose inline image

## the categories of responsive images

There are four categories of responsive images:

1. 16:9 landscape (for “hero” index splash and prose)
2. 9:16 portrait (for inline-image prose)
3. 1:1 square (for index lists and [[Open Graph protocol]])
4. 16:(9/3) banner (for “hero” index splash and prose)

## the responsive breakpoints of images

This Studio has standardized on Bulma and will follow its breakpoint definitions \[📖 [docs](https://bulma.io/documentation/start/responsiveness/#breakpoints) \]:

| Bulma breakpoint name | Bulma width range | 16:9 dimensions within range                                                                                                            | squares            |
| --------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| mobile                | `0–768px`         | `160×90` (90p?)<br>`426×240` (240p)<br>`640×360` (nHD/360p)                                                                             | `160×160` (square) |
| tablet                | `769–1023px`      | `854×480` (480p)<br>`854×160` (banner)                                                                                                  |                    |
| desktop               | `1024–1215px`     | `1024×576` ([EDTV](https://en.wikipedia.org/wiki/Enhanced-definition_television))<br>                                                   | `360×360` (square) |
| widescreen            | `1216–1407px`     | `1280×720` (HD/720p)<br>`1280×240` (banner)<br>`1360×765` ([WXGA](https://en.wikipedia.org/wiki/Display_resolution_standards#1280x768)) |                    |
| full HD               | `>1408px`         | `1920×1080` (1080p)<br>`1920×360` (banner)<br>`2560×1440` (2K/1440p)                                                                    | `640×640` (square) |

According to “[Complete List of all 16:9 Resolutions — from SD to 16K UHD](https://www.game.guide/complete-list-of-all-16-9-resolutions)” the 240p and 360p resolutions come from YouTube. Also, Cloudinary has a [Responsive Image Breakpoints Generator](https://www.responsivebreakpoints.com/) in case I am missing something in my table above—and in the wisdom of Bulma.

## the response strategies for each layout, specifying image resolutions

| layout                                | full HD     | widescreen | desktop   | tablet     | mobile    |
| ------------------------------------- | ----------- | ---------- | --------- | ---------- | --------- |
| “hero” index splash                   | `2560×1440` | `1360×765` |           |            | `640×360` |
| index list (space time, space people) | `640×640`   |            | `360×360` |            |           |
| index list (visitors)                 |             |            |           |            | `160×160` |
| prose main image                      |             | `1280×720` |           | `1280×240` |           |
| inline-image prose                    |             | `720×1280` |           | `360×640`  |           |

The ‘index list (visitors)’ layout is not about responsively _resizing_ its square images; it will be about displaying more and more of the squares, responsively.

[Bryan Wilhite is on LinkedIn](https://www.linkedin.com/in/wilhite)🇺🇸💼
