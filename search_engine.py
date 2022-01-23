import os
import pandas as pd
import numpy as np
import torch
from transformers import CLIPProcessor, CLIPModel
import math

class SearchEngine:
	def __init__(self, dataset):
		self.dataset = dataset
		self.device = "cuda" if torch.cuda.is_available() else "cpu"
		self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
		self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
		self.cwd = os.getcwd()
		self.dataset_path = os.path.join(self.cwd, dataset)
		self.photo_features = np.load(os.path.join(self.dataset_path, "features.npy"))
		self.photo_ids = pd.read_csv(os.path.join(self.dataset_path, "photo_ids.csv"))
		self.photo_ids = list(self.photo_ids['photo_id'])

	def compute_similarities(self, query, image_count, comparison_func):
		with torch.no_grad():
			# Encode and normalize the description using CLIP
			encoding = self.processor(text=query, return_tensors='pt', padding=True).to(self.device)
			text_features = self.model.get_text_features(**encoding)
			if comparison_func == "cosine":
				text_features /= text_features.norm(dim=-1, keepdim=True)

		# Retrieve the description vector and the photo vectors
		text_features = text_features.cpu().numpy()

		similarity_scores = []
		for i, feature in enumerate(self.photo_features):
			if comparison_func == "cosine":
				similarity_scores.append((text_features @ feature.T).item())
			elif comparison_func == "euclidean":
				similarity_scores.append(np.linalg.norm(text_features - feature))

		# Sort the photos by their similarity score
		if comparison_func == "cosine":
			best_photos = sorted(zip(similarity_scores, range(self.photo_features.shape[0])), key=lambda x: x[0], reverse=True)
		elif comparison_func == "euclidean":
			best_photos = sorted(zip(similarity_scores, range(self.photo_features.shape[0])), key=lambda x: x[0],
								 reverse=False)
		return best_photos[:image_count]


	def search(self, query, image_count = 10, return_url=True, comparison_func="cosine"):
		# Read the photos table
		photo_data = pd.read_csv(os.path.join(self.dataset_path, "photo_data.csv"), sep=',', header=0)

		# Load the features and the corresponding IDs
		results = self.compute_similarities(query, image_count, comparison_func)
		# Iterate over the top n results
		search_results = []
		for i in range(image_count):
			# Retrieve the photo ID
			idx = results[i][1]
			photo_id = self.photo_ids[idx]

			# Get all metadata for this photo
			photo_info = photo_data[photo_data["id"] == photo_id].iloc[0]

			description = photo_info["description"]
			if type(photo_info["description"]) is not str:
				description = 'description unavailable'

			if return_url:
				if self.dataset == "unsplash_dataset":
					url_arguments = "?w=640"
				else:
					url_arguments = ""
				url = photo_info["url"] + url_arguments
				search_results.append([url, description])
			else:
				search_results.append(description)
		return search_results
