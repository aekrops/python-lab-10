class Camera:
	type_of_zoom = 'optical'

	def __init__(self, resolution=None, memory_capacity_in_mb=None, zoom=None, producer=None, price_in_uah=None, color=None, model=None, number_of_megapixels=None):
		self._resolution = resolution
		self._memory_capacity_in_mb = memory_capacity_in_mb
		self._zoom = zoom
		self._producer = producer
		self._price_in_uah = price_in_uah
		self._color = color
		self._model = model
		self._number_of_megapixels = number_of_megapixels

	def __str__(self):
		resolution = f'Resolution: {self.resolution}\n'
		memory_capacity_in_mb = f'Memory capacity in megabytes: {self.memory_capacity_in_mb}\n'
		zoom = f'Zoom: {self.zoom}\n'
		producer = f'Producer: {self.producer}\n'
		price_in_uah = f'Price in UAH: {self.price_in_uah}\n'
		color = f'Color: {self.color}\n'
		model = f'Model: {self.model}\n'
		number_of_megapixels = f'Number of megapixels:{self.number_of_megapixels}\n'
		type_of_zoom = f'Type of zoom: {Camera.type_of_zoom}\n'
		return resolution + memory_capacity_in_mb + zoom + producer + price_in_uah + color + model + number_of_megapixels + type_of_zoom

	def __repr__(self):
		name = f"Resolution('{self.resolution}')\n"
		memory_capacity_in_mb = f"Memory capacity in megabytes('{self.memory_capacity_in_mb}')\n"
		zoom = f"Zoom('{self.zoom}')\n"
		producer = f"Producer('{self.producer}')\n"
		price_in_uah = f"Price in UAH('{self.price_in_uah}')\n"
		color = f"Color('{self.color}')\n"
		model = f"Model('{self.model}')\n"
		number_of_megapixels = f"Number of megapixels('{self.number_of_megapixels}')\n"
		type_of_zoom = f"Type of zoom('{Camera.type_of_zoom}')\n"
		return resolution + memory_capacity_in_mb + zoom + producer + price_in_uah + color + model + number_of_megapixels + type_of_zoom

	def __del__(self):
		print("Deleted " + self.__class__.__name__ + " | ID: " + str(id(self)))
		return

	@staticmethod
	def get_type_of_zoom():
		return Camera.type_of_zoom

	@property
	def resolution(self):
		return self._resolution

	@resolution.setter
	def resolution(self, resolution):
		self._resolution = resolution

	@property
	def memory_capacity_in_mb(self):
		return self._memory_capacity_in_mb

	@memory_capacity_in_mb.setter
	def memory_capacity_in_mb(self, memory_capacity):
		self._memory_capacity_in_mb = memory_capacity_in_mb

	@property
	def zoom(self):
		return self._zoom

	@zoom.setter
	def zoom(self, zoom):
		self._zoom = zoom

	@property
	def producer(self):
		return self._producer

	@producer.setter
	def producer(self, producer):
		self._producer = producer

	@property
	def price_in_uah(self):
		return self._price_in_uah

	@price_in_uah.setter
	def price_in_uah(self, price_in_uah):
		self._price_in_uah = price_in_uah

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, color):
		self._color = color

	@property
	def model(self):
		return self._model

	@model.setter
	def model(self, model):
		self._model = model

	@property
	def number_of_megapixels(self):
		return self._number_of_megapixels

	@number_of_megapixels.setter
	def number_of_megapixels(self, number_of_megapixels):
		self._number_of_megapixels = number_of_megapixels

