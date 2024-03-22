#!/bin/bash

# Check if filename argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

# Execute sed commands on the specified filename
sed -i '1s/^/import os\n/' "$filename"
sed -i 's/\( *.lcgeo_DIR.:\).*/\1 os.environ["lcgeo_DIR"],/' "$filename"
sed -i 's/algList.append(BgOverlayWW)/# algList.append(BgOverlayWW)/' "$filename"
sed -i 's/algList.append(BgOverlayWB)/# algList.append(BgOverlayWB)/' "$filename"
sed -i 's/algList.append(BgOverlayBW)/# algList.append(BgOverlayBW)/' "$filename"
sed -i 's/algList.append(BgOverlayBB)/# algList.append(BgOverlayBB)/' "$filename"
sed -i 's/algList.append(PairBgOverlay)/# algList.append(PairBgOverlay)/' "$filename"

