# Generating Responsive Images

The [work here](./generating-responsive-images.ipynb) is a search for responsive-image strategies for my studio.

So far we have about three responsive-image information designs:

- Gallery Image Strategy
- Hero Image (and Portrait Hero Image) Strategy
- Index Background Strategy

## Gallery Image Strategy

The design goal of the ‘gallery’ image is the desire to display an image at a _maximum_ resolution, full-screen, landscape orientation. This desire could be satisfied in a full-screen hero image layout or the typical gallery presentation.

We start with a Full HD (1080p) image: `1920x1080`

From the starting image we generate the following:

| name | size | operation
|- |- |-
| `gallery-720p` | `1280x720` | resize
| `gallery-sd` | `640x480` | crop 720p
| `gallery-thumb` | `120x120` | crop SD

## Hero Image Strategy

One approach to a design based on the “hero” image is to start with a Full HD landscape and crop down, using rule-of-thirds vertical dimensions.

We start with a Full HD (1080p) image: `1920x1080`

From the starting image we generate the following with vertical, rule-of-thirds dimensions:

| name | size | operation(s)
|- |- |-
`hero-1080p` | `1920x640` | crop
`hero-720p` | `1280x240` | resize, crop

## Portrait Hero Image Strategy

Another approach to the “hero” image is the intent to lay it out with text, suggesting that this image will be in a portrait orientation, flowing with, say, text. This would be the typical 20<sup>th</sup> magazine layout of the print era.

We start with a Full HD (1080p) image: `1920x1080`

From the starting image we generate the following with horizontal, rule-of-thirds dimensions:

| name | size | operation(s)
|- |- |-
`hero-portrait-1080p` | `640x1080` | crop
`hero-portrait-720p` | `427x720` | resize, crop

## Index Background Strategy

The Index Background Strategy is very similar to the Gallery Image Strategy except that  portrait orientation must be taken into account. We can do this by starting with two different originals. One is portrait (`1080x1920`), the other landscape (HD):

| original | name | size | operation
|- |- |- |-
| `1920x1080` | `index-720p` | `1280x720` | resize
| `1920x1080` | `index-sd` | `640x480` | crop 720p
| `1080x1920` | `index-720x1280` | `720x1280` | resize
| `1080x1920` | `index-480x640` | `480x640` | crop 720x1280

## remarks about portrait screen sizes

According to [screensiz.es](https://screensiz.es/) as of the writing, the most popular screen size is the portrait of the Apple iPhone 8 Plus: `1080x1920`. This size also holds second place in the Apple iPhone 7 Plus.

According to a mobiforge.com report by Pawel Piejko, “[720×1280 is the most common mobile screen resolution in Q3 2016](https://mobiforge.com/news-comment/720x1280-is-the-most-common-mobile-screen-resolution-in-q3-2016-new-report).”

For more details, see “[studio status report: 2020-08](http://songhayblog.azurewebsites.net/entry/2020-08-30-studio-status-report-2020-08/).”

[Bryan Wilhite is on LinkedIn](https://www.linkedin.com/in/wilhite)🇺🇸💼
