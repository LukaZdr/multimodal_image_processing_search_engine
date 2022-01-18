# multimodal_image_processing_search_engine(WIP)
A image search engine that uses CLIP to make the content of images searchable. Used datasets are [Unsplashed](https://unsplash.com/data) and [Coco](https://cocodataset.org/).

![2022-01-11-23-29-45_Trim_Trim](https://user-images.githubusercontent.com/24440000/149033047-574d067c-e549-44c6-91aa-e945511755d2.gif)


this example searches for "people dancing" in the coco dataset.

## Setup
### If you wnat to download proprocessed data:
Download the already preprocesed dataset here https://cloud.mafiasi.de/s/tLEiMdXYpnEfZma.

Unzip this zip file into the main dir of that directory. The repo should now look like the one shown under "Project struckture".

### If you want to build the dataset yourself:
run both ipynb from bigining to end. This may take quie some time as the coco dataset alone is over 25GB in size. After completly running both notebooks however your resulting Repo should look like the one shown in "Project struckture".

### Runing the app
To run the app first follow the instructions listed in the setup.

Afterwards run:
```
export FLASK_APP=mipse
flask run
```

## Project struckture
```
├── README.md
├── coco_dataset
│   ├── features.npy
│   ├── photo_data.csv
│   └── photo_ids.csv
├── coco_dataset_preperation.ipynb
├── mipse.py
├── search_engine.py
├── static
│   ├── css
│   │   └── main.css
│   └── images
│       ├── favicon.ico
│       └── logo.png
├── templates
│   ├── layout.html
│   └── main_page.html
├── unsplash_dataset
│   ├── features.npy
│   ├── photo_data.csv
│   └── photo_ids.csv
└── unsplash_dataset_preperation.ipynb
```
