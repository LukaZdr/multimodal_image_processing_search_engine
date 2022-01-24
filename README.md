<p align="center">
  <img src="https://user-images.githubusercontent.com/24440000/149975330-887e412e-9314-45e6-a404-05c1cb1ed537.png" width="50%">
</p>


An image search engine that uses CLIP to make the content of images searchable. Used datasets are [Unsplashed](https://unsplash.com/data) and [Coco](https://cocodataset.org/).
<p align="center">
  <img src="https://user-images.githubusercontent.com/24440000/149972485-d53ea8fc-417e-41e3-897d-a5a8c682a766.gif">
</p>

This example searches for "dog in traffic" in the coco dataset.

## Setup
### If you want to download preprocessed data:
Download the already preprocessed dataset here https://cloud.mafiasi.de/s/tLEiMdXYpnEfZma.

Unzip this zip file into the main dir of that directory. The repo should now look like the one shown under "Project structure".

### If you want to build the dataset yourself:
Run both ipynb from beginning to end. This may take some time as the coco dataset alone is over 25GB in size.
However, after completely running both notebooks your resulting Repo should look like the one shown in "Project structure".

### Running the app
To run the app first follow the instructions listed in the setup.

Afterwards run:
```
export FLASK_APP=mipse
flask run
```

## Project structure
```
├── README.md
├── coco_dataset
│   ├── features.npy
│   ├── photo_data.csv
│   └── photo_ids.csv
├── coco_dataset_preperation.ipynb
├── Evaluation.ipynb
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
