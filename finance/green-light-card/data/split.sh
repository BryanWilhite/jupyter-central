csplit \
    --elide-empty-files \
    --prefix=2020- \
    -s \
    --suffix-format="%02d.tmp.csv" \
    2020-input.txt \
    /Date/ {*}\

csplit \
    --elide-empty-files \
    --prefix=2021- \
    -s \
    --suffix-format="%02d.tmp.csv" \
    2021-input.txt \
    /Date/ {*}\

# https://www.golinuxcloud.com/csplit-split-command-examples-linux-unix/#7_csplit_add_suffix

# https://www.linux.com/topic/desktop/splitting-and-re-assembling-files-linux/