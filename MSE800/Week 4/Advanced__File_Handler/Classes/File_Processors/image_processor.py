import tensorflow as tf

class ImageProcessor:
    
    def __init__(self, file_path, extension):
        self.file_path = file_path
        self.extension = extension
        self.image_data = None

    def process_image(self):
        try:            
            self.image_data = tf.io.read_file(self.file_path)
            
            if self.extension in [".jpg", ".jpeg"]:
                image = tf.image.decode_jpeg(self.image_data, channels=3)
            elif self.extension  == ".png":
                image = tf.image.decode_png(self.image_data, channels=3)
            elif self.extension  == ".bmp":
                image = tf.image.decode_bmp(self.image_data)
            elif self.extension  == ".gif":
                image = tf.image.decode_gif(self.image_data)[0]  # GIFs return a 4D tensor (frames), use [0] for first frame
            else:
                print(f"Warning: Unsupported image format '{self.extension}'. Skipping processing file '{self.file_path}'")
                return

            print(f"\nDetails of the processed image): {self.file_path}\n")
            print(f"Shape (Height, Width, Channels): {image.shape}")
            print(f"Image Height: {image.shape[0]} pixels")
            print(f"Image Width: {image.shape[1]} pixels")
            print(f"Number of Channels: {image.shape[2]}")
            print(f"Image Data Type: {image.dtype}")
            
        except Exception as e:
            print(f"Error processing image file {self.file_path} : {e}")